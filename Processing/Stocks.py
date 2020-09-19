from Processing.ProcessingMethods import ProcessingMethods
from logger.main_logger import get_logger


class Stocks(ProcessingMethods):
    def __init__(self, workbook):
        # self.url = 'https://suppliers-stats.wildberries.ru/api/v1/supplier/stocks?dateFrom=2020-03-25T21%3A00%3A00.000Z&key=MzdkZDgzY2EtYzA3Yy00N2FlLTlmNjMtYWRiMGNiNTk3ODA2'
        self.url = 'https://run.mocky.io/v3/f4a1b58b-7cae-4837-b5ba-2505e5898412'
        self.report_name = 'Склад'
        super().__init__(workbook, self.url, self.report_name)


