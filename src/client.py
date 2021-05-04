from typing import Union
import requests
from model.open_interest import OpenInterestRequestParams, OpenInterestResponse
from type import Failure

API_BASE_URL = "https://testnet.binancefuture.com"


class BinanceApiClient:

    def __init__(self, api_base_url: str = API_BASE_URL):
        self.api_base_url = api_base_url

    def get_open_interest(self, resource_name: str, params: OpenInterestRequestParams) -> Union[OpenInterestResponse, Failure]:
        try:
            response = requests.get(
                self.api_base_url + resource_name, params={
                    'symbol': params.symbol
                })
            response.raise_for_status()

            # TODO: mapper欲しい
            return OpenInterestResponse(
                response.json()['openInterest'],
                response.json()['symbol'],
                response.json()['time']
            )
        except Exception as e:
            return Failure('Get open interest error', e)
