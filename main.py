import json

import requests
import xlsxwriter

from Processing.Stocks import Stocks
from Processing.ProcessingMethods import ProcessingMethods


def get_wildberries_api_response():
    return requests.get(
        "https://suppliers-stats.wildberries.ru/api/v1/supplier/stocks?dateFrom=2020-03-25T21%3A00%3A00.000Z&key=MzdkZDgzY2EtYzA3Yy00N2FlLTlmNjMtYWRiMGNiNTk3ODA2").text


def read_json_file():
    with open("response.json", 'r') as resp:
        return resp.read()


def main():
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('Expenses01.xlsx')
    stocks = Stocks(workbook)
    ws = stocks.main_processor()
    workbook.close()


if __name__ == '__main__':
    main()
