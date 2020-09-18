import json

import requests

def get_wildberries_api_response():
    return requests.get("https://suppliers-stats.wildberries.ru/api/v1/supplier/stocks?dateFrom=2020-03-25T21%3A00%3A00.000Z&key=MzdkZDgzY2EtYzA3Yy00N2FlLTlmNjMtYWRiMGNiNTk3ODA2").text

def read_json_file():
    with open("response.json", 'r') as resp:
        return resp.read()


def main():
    json_object = json.loads(read_json_file())
    for elem in json_object:
        print (elem.get('SCCode'))



if __name__ == '__main__':
    main()