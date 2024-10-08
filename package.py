#Package class with all info
class Package:
    def __init__(self):
        self.id = None
        self.address = None
        self.deadline = None
        self.city = None
        self.zip = None
        self.weight = None
        self.status = None

    def insert(self, id_num: int, address: str, deadline: str, city: str, zipcode: str, weight: float, status: str= "at the hub"):
        self.id = id_num
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zip = zipcode
        self.weight = weight
        self.status = status

    def get_data(self):
        return [self.id, self.address, self.deadline, self.city, self.zip, self.weight, self.status]