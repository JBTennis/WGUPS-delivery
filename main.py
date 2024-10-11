#011540261
from datetime import timedelta
from package import Package
from truck import Truck
from hash import ChainingHashTable

#Start of global variables
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
#end of global variables

def load_truck(truck, list):
    for pack in list:
        truck.add_packages(pack)


def deliver(truck):
    #Once they're out for delivery it changes the status of the packages to 'en route'
    for i in range(0, len(truck.packages)):
        truck.packages[i].status = 'en route'
        truck.packages[i].pick_up_time = truck.current_time
    deli_index = -1

    #Start of nearest neighbor algorithm, it has a time complexity of O(N^2) this while loop
    #is the outer loop that goes until we are out of packages
    while len(truck.packages) >= -1:
        nearest = 10000000

        # This is the inner loop that does most of the heavy lifting by seeing which next address
        # is the closest
        for i in range(0, len(truck.packages)):
            if nearest > distanceBetween(truck.current_location, truck.packages[i].address):
                nearest = distanceBetween(truck.current_location, truck.packages[i].address)
                deli_index = i

        #Once we've gone through the whole list we want to return to the hub
        if len(truck.packages) < 1:
            nearest = distanceBetween('4001 South 700 East', truck.current_location)
            deli_index = None

        #This updates our mileage ticker and our time ticker for every address visited
        truck.current_time += timedelta(hours=nearest / truck.speed)
        truck.mileage += nearest

        #This returns us to the hub, I've already added the time and mileage above
        if len(truck.packages) < 1:
            truck.current_location = '4001 South 700 East'
            input("All deliveries made and truck returning to hub")
            return

        elif len(truck.packages) > 0:
            truck.packages[deli_index].status = "Delivered"
            truck.packages[deli_index].delivery_time = truck.current_time
            truck.current_location = truck.packages[deli_index].address
            truck.packages.remove(truck.packages[deli_index])

#This function finds the actual distance of the two based of the distanceCSV file
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


    #Because the CSV file doesn't go all the way up for a lot of the indexes the bigger number
    #Should always be the left number otherwise we wouldn't get a return
    return float(location[max(first, second)] [min(first, second)])

def lookUp(time, id):
    hour, minute = time.split(':')
    time = timedelta(hours=int(hour), minutes=int(minute))
    if time > hash_tab.search(id).delivery_time:
        return f'package delivered at {hash_tab.search(id).delivery_time}'
    elif time > hash_tab.search(id).pick_up_time:
        return f'package en route'
    else:
        return f'package at delivery hub'


if __name__ == "__main__":
    #what_time = input("What time are you looking for? (Please add your time in HH:MM format)")
    #what_pack = int(input("What was your package id number?"))
    packs = [Package() for i in range(0, 40)]
    hash_tab = ChainingHashTable()
    i = 0
    with open("packageCSV.csv") as pack:
        for line in pack:
            line = line.split(',')
            line[-1] = line[-1].strip()
            packs[i].insert(int(line[0]), line[1], line[5], line[2], line[4], int(line[6]), line[-1])
            i += 1
    for i in packs:
        hash_tab.insert(i.id, i)


    truck1 = Truck(hash_tab, 8)
    truck2 = Truck(hash_tab, 9, 5)
    truck3 = Truck(hash_tab, 10, 20)

    list1 = [packs[0], packs[12], packs[13], packs[14], packs[15], packs[19], packs[35], packs[36], packs[29], packs[28], packs[33], packs[20], packs[39]]
    list2 = [packs[2], packs[5], packs[17], packs[24], packs[25], packs[27], packs[30], packs[31], packs[35]]
    #list3 = [packs[1], packs[3], packs[4], packs[5], packs[6], packs[7], packs[8], packs[9], packs[10], packs[24], packs[27], packs[31], packs[32]]

    load_truck(truck1, list1)
    load_truck(truck2, list2)
    #load_truck(truck3, list3)

    deliver(truck2)
    deliver(truck1)
    deliver(truck3)
    #print({truck1.mileage + truck2.mileage + truck3.mileage})


    #print(lookUp(what_time, what_pack))

    for key in hash_tab.table:
        if len(key) > 0:
            print(key[0][1])

    print(truck1.current_time, truck1.mileage)


