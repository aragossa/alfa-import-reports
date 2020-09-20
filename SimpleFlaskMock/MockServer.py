import os

from flask import Flask

app = Flask(__name__)


def read_json_file(filename):
    path_to_file = os.path.join('ResponseExamples', 'WildberriesResponses', filename)
    with open(path_to_file, 'r') as response:
        return response.read()


@app.route('/wildberries/<path:subpath>')
def report_incomes(subpath):
    if subpath == 'detailmart':
        return read_json_file('detailmart.json')
    elif subpath == 'incomes':
        return read_json_file('incomes.json')
    elif subpath == 'orders':
        return read_json_file('orders.json')
    elif subpath == 'sales':
        return read_json_file('sales.json')
    elif subpath == 'stocks':
        return read_json_file('stocks.json')


if __name__ == '__main__':
    app.run()
