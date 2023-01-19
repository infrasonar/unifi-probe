from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..snmpquery import snmpquery

QUERIES = (
    MIB_INDEX['UBNT-UniFi-MIB']['unifiApSystem'],
    MIB_INDEX['UBNT-UniFi-MIB']['unifiRadioEntry'],
    MIB_INDEX['UBNT-UniFi-MIB']['unifiVapEntry'],
)


async def check_unifi(
        asset: Asset,
        asset_config: dict,
        check_config: dict):

    state = await snmpquery(asset, asset_config, check_config, QUERIES)
    for item in state.get('unifiRadio', []):
        item.pop('Index')
        item['name'] = item.pop('Name')
    for item in state.get('unifiVap', []):
        item.pop('Index')
        item['name'] = item.pop('Name')
    return state
