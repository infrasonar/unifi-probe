from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery

QUERIES = (
    (MIB_INDEX['UBNT-UniFi-MIB']['unifiApSystem'], False),
    (MIB_INDEX['UBNT-UniFi-MIB']['unifiRadioEntry'], True),
    (MIB_INDEX['UBNT-UniFi-MIB']['unifiVapEntry'], True),
)


async def check_unifi(
        asset: Asset,
        asset_config: dict,
        check_config: dict):

    snmp = get_snmp_client(asset, asset_config, check_config)
    state = await snmpquery(snmp, QUERIES)
    for item in state.get('unifiRadioEntry', []):
        item.pop('unifiRadioIndex')
        item['name'] = item.pop('unifiRadioName')
    for item in state.get('unifiVapEntry', []):
        item.pop('unifiVapIndex')
        item['name'] = item.pop('unifiVapName')
    return state
