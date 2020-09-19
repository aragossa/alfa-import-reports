from datetime import datetime

from Utils.ConfigReader.ConfigReader import read_config
from Processing.Headers.table_headers import stocks_headers_list
from Processing.ProcessingMethods import ProcessingMethods


class ReportStocks(ProcessingMethods):
    def __init__(self, workbook):
        self.report_name = 'Склад'
        super().__init__(workbook=workbook,
                         url=self.__url_builder(),
                         report_name=self.report_name,
                         headers=self.__get_headers())

    def __url_builder(self):
        # TODO fix request url
        app_mode = read_config('application').get('mode')
        if app_mode == 'prod':
            api_key = read_config('wildberries').get('api')
            now = datetime.now()
            date_form = f'{now.year:04d}-{now.month:02d}-{now.day-1:02d}'
            url = f'https://suppliers-stats.wildberries.ru/api/v1/supplier/stocks?dateFrom={date_form}&key={api_key}'
        else:
            url = 'http://127.0.0.1:5000/wildberries/stocks'
        return url

    def __get_headers(self):
        return stocks_headers_list
