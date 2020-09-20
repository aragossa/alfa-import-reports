import sys

from ReportManager.ReportManager import ReportManager


def main():
    args = sys.argv
    report = ReportManager(args=args)
    report.run()


if __name__ == '__main__':
    main()
