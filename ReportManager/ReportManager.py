import sys
from Utils.Logger.main_logger import get_logger

from ReportManager.WildberriesReport.WildberriesReport import WildberriesReport

log = get_logger("ReportManager")

class ReportManager:
    def __init__(self, args):
        self.args = args

    def run(self):
        if len(self.args) == 1:
            print ('Application usage:\n main.py -<report shortname1> -<report shortname1>\n    -w for Wildberries report\n    -f for flow report')
            sys.exit(2)
        else:
            for arg in self.args:
                if '-w' == arg:
                    self.run_wildberries()
                elif '-f'== arg:
                    self.run_flow()
                elif arg == 'main.py':
                    log.info('Starting application')
                else:
                    print ('main.py -<report shortname1> -<report shortname1>\n    -w for Wildberries report\n    -f for flow report')


    def run_wildberries(self):
        log.info('Running Wildberries report')
        WildberriesReport.run()

    def run_flow(self):
        log.info('Running Flow.Alfashoes report')