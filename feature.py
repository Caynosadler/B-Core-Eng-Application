from categories import Client, ProductArea

class Feature:

    def __init__(self, client_priority):

        self.client_priority = client_priority

    @property
    def client_priority(self):
        return self.__client_priority

    @property
    def client(self):
        return self.__client

    @property
    def product_area(self):
        return self.__product_area

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def target_date(self):
        return self.__target_date
    
    @client_priority.setter
    def client_priority(self, client_priority):
        self.__client_priority = client_priority

    @client.setter
    def client(self, client):
        self.__client = Client(client)

    @product_area.setter
    def product_area(self, product_area):
        self.__prodcut_area = ProductArea(product_area)

    @title.setter
    def setter(self, title):
        self.__title = title

    @description.setter
    def description(self, description):
        self.__description = description

    @target_date.setter
    def target_date(self, target_date):
        self.__target_date = target_date
        

    
