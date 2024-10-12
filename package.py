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
        self.info = None
        self.pick_up_time = None
        self.delivery_time = None

    def insert(self, id_num: int, address: str, deadline: str, city: str, zipcode: str, weight: float, extra_info, status: str= "at the hub"):
        self.id = id_num
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zip = zipcode
        self.weight = weight
        self.status = status
        self.info = extra_info



    def __str__(self):
        return f'Package ID: {self.id}, Address: {self.address}, Deadline: {self.deadline}, Status: {self.status}, Picked Up: {self.pick_up_time}, Delivered: {self.delivery_time}'
