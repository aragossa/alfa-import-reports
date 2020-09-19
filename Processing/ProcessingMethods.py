import json
import requests

from Utils.Logger.main_logger import get_logger


class ProcessingMethods:

    def __init__(self, workbook, url, report_name, headers):
        self.__url = url
        self.__report_name = report_name
        self.__row_cursor = 1
        self.__headers = headers
        self.__log = get_logger(self.__report_name)
        self.workbook = workbook


    # def log(self):
    #     return get_logger(self.__report_name)

    def __get_wildberries_info(self):
        self.__log.info(f"Sending GET request to {self.__url}")
        response = requests.get(self.__url).text
        return response

    def __get_json(self):
        return json.loads(self.__get_wildberries_info())

    def __add_worksheet(self):
        return self.workbook.add_worksheet(self.__report_name)

    def __write_row(self, row, ws):
        col_cursor = 0
        for item in row.values():
            ws.write(self.__row_cursor, col_cursor, item)
            col_cursor += 1

    def __write_headers(self, ws):
        col_cursor = 0
        for item in self.__headers:
            ws.write(0, col_cursor, item)
            col_cursor += 1

    def main_processor(self):
        self.__log.info(f'Processing report {self.__report_name}')
        ws = self.__add_worksheet()
        self.__write_headers(ws=ws)
        data = self.__get_json()
        for row in data:
            self.__write_row(row=row, ws=ws)
            self.__row_cursor += 1
        return ws
