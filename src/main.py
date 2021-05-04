import client
from model.open_interest import RESOURCE_NAME_OPEN_INTEREST, OpenInterestRequestParams
from type import Failure

binance_client = client.BinanceApiClient()

if isinstance(result := binance_client.get_open_interest(
    RESOURCE_NAME_OPEN_INTEREST,
    OpenInterestRequestParams(
        'BTCUSDT'
    )
), Failure):
    result.exit()
else:
    result.print_data()
