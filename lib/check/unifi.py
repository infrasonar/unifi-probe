from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..utils import get_data

QUERIES = (
    MIB_INDEX['UBNT-UniFi-MIB']['unifiApSystem'],
    MIB_INDEX['UBNT-UniFi-MIB']['unifiRadioEntry'],
    MIB_INDEX['UBNT-UniFi-MIB']['unifiVapEntry'],
)


async def check_unifi(
        asset: Asset,
        asset_config: dict,
        check_config: dict):

    state = await get_data(asset, asset_config, check_config, QUERIES)
    for item in state.get('unifiRadioEntry', []):
        item.pop('unifiRadioIndex')
        item['name'] = item.pop('unifiRadioName')
    for item in state.get('unifiVapEntry', []):
        item.pop('unifiVapIndex')
        item['name'] = item.pop('unifiVapName')
    return state
