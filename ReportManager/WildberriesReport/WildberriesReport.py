import os

import xlsxwriter

from Processing.ReportIncomes import ReportIncomes
from Processing.ReportOrders import ReportOrders
from Processing.ReportSales import ReportSales
from Processing.ReportStocks import ReportStocks


class WildberriesReport:

    @staticmethod
    def run():
        workbook = xlsxwriter.Workbook(os.path.join('Reports', 'WildberriesReport.xlsx'))
        stocks = ReportStocks(workbook)
        stocks.main_processor()
        sales = ReportSales(workbook)
        sales.main_processor()
        incomes = ReportIncomes(workbook)
        incomes.main_processor()
        orders = ReportOrders(workbook)
        orders.main_processor()
        workbook.close()