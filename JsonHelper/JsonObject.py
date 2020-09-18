from logger.main_logger import get_logger
from headers.table_headers import headers_dict, headers_list

class JsonObject:
    def __init__(self, json_object):
        self.lastChangeDate = json_object.get("lastChangeDate")
        self.supplierArticle = json_object.get("supplierArticle")
        self.techSize = json_object.get("techSize")
        self.barcode = json_object.get("barcode")
        self.quantity = json_object.get("quantity")
        self.isSupply = json_object.get("isSupply")
        self.isRealization = json_object.get("isRealization")
        self.quantityFull = json_object.get("quantityFull")
        self.quantityNotInOrders = json_object.get("quantityNotInOrders")
        self.warehouseName = json_object.get("warehouseName")
        self.inWayToClient = json_object.get("inWayToClient")
        self.inWayFromClient = json_object.get("inWayFromClient")
        self.nmId = json_object.get("nmId")
        self.subject = json_object.get("subject")
        self.category = json_object.get("category")
        self.daysOnSite = json_object.get("daysOnSite")
        self.brand = json_object.get("brand")
        self.SCCode = json_object.get("SCCode")
        self.Price = json_object.get("Price")
        self.Discount = json_object.get("Discount")
        self.log = get_logger("JsonObject")

    def write_row(self, ws, write_row):
        ws.write(write_row, 0, self.lastChangeDate)
        ws.write(write_row, 1, self.supplierArticle)




