import dataclasses

RESOURCE_NAME_OPEN_INTEREST = '/fapi/v1/openInterest'


@dataclasses.dataclass
class OpenInterestRequestParams:
    '''
    symbol: 通貨名
    '''
    symbol: str


@dataclasses.dataclass
class OpenInterestResponse:
    '''
    open_interest:
    symbol:
    time:
    '''
    open_interest: str
    symbol: str
    time: int

    def print_data(self) -> None:
        print("open_interest: ", self.open_interest)
        print("symbol: ", self.symbol)
        print("time: ", self.time)
