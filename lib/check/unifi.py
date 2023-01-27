from asyncsnmplib.mib.mib_index import MIB_INDEX
from asyncsnmplib.exceptions import SnmpNoAuthParams, SnmpNoConnection
from asyncsnmplib.utils import InvalidConfigException, snmp_queries
from libprobe.asset import Asset
from libprobe.exceptions import CheckException, IgnoreResultException

QUERIES = (
    MIB_INDEX['UBNT-UniFi-MIB']['unifiApSystem'],
    MIB_INDEX['UBNT-UniFi-MIB']['unifiRadioEntry'],
    MIB_INDEX['UBNT-UniFi-MIB']['unifiVapEntry'],
)


async def check_unifi(
        asset: Asset,
        asset_config: dict,
        check_config: dict):

    address = check_config.get('address')
    if address is None:
        address = asset.name
    try:
        state = await snmp_queries(address, asset_config, QUERIES)
    except SnmpNoConnection:
        raise CheckException('unable to connect')
    except (InvalidConfigException, SnmpNoAuthParams):
        raise IgnoreResultException
    except Exception:
        raise
    for item in state.get('unifiRadioEntry', []):
        item.pop('unifiRadioIndex')
        item['name'] = item.pop('unifiRadioName')
    for item in state.get('unifiVapEntry', []):
        item.pop('unifiVapIndex')
        item['name'] = item.pop('unifiVapName')
    return state
