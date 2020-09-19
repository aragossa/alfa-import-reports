import json
import requests

from logger.main_logger import get_logger
from headers.table_headers import headers_dict, headers_list


class ProcessingMethods:

    log = get_logger("ProcessingMethods")

    def __init__(self, workbook, url, report_name):
        self.__url = url
        self.__report_name = report_name
        self.__row_cursor = 1
        self.workbook = workbook
        self.__filename = 'response.json'

    def __get_wildberries_info(self):
        return requests.get(self.__url).text

    def __get_json(self):
        return json.loads(self.__get_wildberries_info())

    def __add_worksheet(self):
        return self.workbook.add_worksheet(self.__report_name)

    def __write_row(self, row, ws):
        col_cursor = 0
        for item in row.values():
            ws.write(self.__row_cursor, col_cursor, item)
            col_cursor += 1

    def main_processor(self):
        get_logger(self.__report_name).info(f'Processing report {self.__report_name}')
        ws = self.__add_worksheet()
        data = self.__get_json()
        for row in data:
            self.__write_row(row=row, ws=ws)
            self.__row_cursor += 1
        return ws
