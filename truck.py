class Truck:
    location = []

    with open("distanceCSV.csv") as distance:

        for line in distance:
            line = line.split(',')
            line[26] = line[26].strip()
            location.append(line)
    addys = []

    with open("addressCSV.csv") as _:
        for line in _:
            line = line.split(',')
            line[-1] = line[-1].strip()
            addys.append(line)

    def __init__(self, hours=8, minutes=0):
        self.current_location = '4001 South 700 East'
        self.packages = []
        self.mileage = 0.0
        self.current_time = timedelta(hours, minutes)
        self.speed = 18

    def add_package(self, package):
        self.packages.append(package)

    def deliver(self):
        nearest = float('inf')
        deli_pack = None
        for package in self.packages:
            if nearest > distanceBetween(self.current_location, package.address):
                nearest = distanceBetween(self.current_location, package.address)
                deli_pack = package

        time_add = nearest / self.speed

        self.current_time += time_add
        self.mileage += nearest
        deli_pack.status = 'Delivered'
        self.current_location = deli_pack.address
        self.packages.remove(deli_pack)
