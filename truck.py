from datetime import timedelta

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
class Truck:
#Added addresses and distances so they can be used to find distance between later

    def __init__(self,hours=8, minutes=0):
        self.current_location = '4001 South 700 East'
        self.packages = []
        self.mileage = 0.0
        self.current_time = timedelta(0, 0, 0, 0, minutes, hours, 0)
        self.speed = 18

    #I originally was adding packages one by one but I decided just adding a list of items is probably the more efficient way to do things
    def add_packages(self, package):
        self.packages.append(package)
        i = self.packages.index(package)
        self.packages[i].status = "en route"


    def deliver(self):
        deli_index = -1
        while len(self.packages) >= -1:
            nearest = 10000000

            # goes through every package in truck to see which delivery is closest
            for i in range(0, len(self.packages)):
                if nearest > distanceBetween(self.current_location, self.packages[i].address):
                    nearest = distanceBetween(self.current_location, self.packages[i].address)
                    deli_index = i

            if len(self.packages) < 1:
                nearest = distanceBetween('4001 South 700 East', self.current_location)
                deli_index = None


            self.current_time += timedelta(hours=nearest / self.speed)
            self.mileage += nearest

            #updates the clock
            if len(self.packages) < 1:                           #otherwise it takes it back to the hub
                self.current_location = '4001 South 700 East'
                input("All deliveries made and truck returning to hub")
                return

            elif len(self.packages) > 0:
                self.packages[deli_index].status = f'Delivered at {self.current_time}'
                self.current_location = self.packages[deli_index].address
                self.packages.remove(self.packages[deli_index])
                print(self.current_time)

def distanceBetween(addy1, addy2):
    first = -1
    second = -1
    try:
        for i in range(len(addys)):
            if addy1 == addys[i][2]:
                first = int(addys[i][0])
            if addy2 == addys[i][2]:
                second = int(addys[i][0])
    except IndexError:
        print("One or more address not in database")
        return 0



    return float(location[max(first, second)] [min(first, second)])