from datetime import timedelta

class Truck:

    def __init__(self, hash_table, hours=8, minutes=0,):
        self.current_location = '4001 South 700 East'
        self.packages = []
        self.mileage = 0.0
        self.current_time = timedelta(0, 0, 0, 0, minutes, hours, 0)
        self.speed = 18
        self.hash_table = hash_table


    def add_packages(self, package):
        self.packages.append(package)

    def __str__(self):
        return f'{self.packages}'
