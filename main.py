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

#This runs first and adds packages to truck objects
def load_truck(truck, lists):
    for pack in lists:
        truck.add_packages(pack)


#Delivers packages and removes them from truck object while updating package status
def deliver(truck):
    #Once they're out for delivery it changes the status of the packages to 'en route'
    for i in range(0, len(truck.packages)):
        truck.packages[i].status = 'en route'
        truck.packages[i].pick_up_time = truck.current_time
    deli_index = -1

    #Start of nearest neighbor algorithm, it has a time complexity of O(N^2), this while loop
    #is the outer loop that goes until we are out of packages
    while len(truck.packages) >= -1:
        nearest = 10000000

        # This is the inner loop that does most of the heavy lifting by seeing which next address
        # is the closest of all packages left in truck
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
            return
        elif len(truck.packages) > 0:
            truck.packages[deli_index].status = "Delivered"
            truck.packages[deli_index].delivery_time = truck.current_time
            truck.current_location = truck.packages[deli_index].address
            truck.packages.remove(truck.packages[deli_index])

#This function takes two addresses and finds the distance between the two
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


#This take the id of a package and a desired time and compares to the delivery and pick up time
#and returns the appropriate descriptor of where the package is
def lookUp(time, id):
    try:
        hour, minute = time.split(':')
        time = timedelta(hours=int(hour), minutes=int(minute))
        if time > hash_tab.search(id).delivery_time:
            return (f'Package ID: {id}, Address: {hash_tab.search(id).address}, Deadline: {hash_tab.search(id).deadline},'
                    f' City: {hash_tab.search(id).city}, Zipcode: {hash_tab.search(id).zip}, Weight: {hash_tab.search(id).weight} lbs,'
                    f' package delivered at: {hash_tab.search(id).delivery_time}')
        elif time > hash_tab.search(id).pick_up_time:
            return (f'Package ID: {id}, Address: {hash_tab.search(id).address}, Deadline: {hash_tab.search(id).deadline},'
                    f' City: {hash_tab.search(id).city}, Zipcode: {hash_tab.search(id).zip}, Weight: {hash_tab.search(id).weight} lbs,'
                    f' package en route')
        else:
            return (f'Package ID: {id}, Address: {hash_tab.search(id).address}, Deadline: {hash_tab.search(id).deadline},'
                    f' City: {hash_tab.search(id).city}, Zipcode: {hash_tab.search(id).zip}, Weight: {hash_tab.search(id).weight} lbs,'
                    f' package at delivery hub')
    except ValueError:
        return "It appears your value is invalid please try again!"


if __name__ == "__main__":
    #I created a list of package objects to start
    packs = [Package() for i in range(0, 40)]
    hash_tab = ChainingHashTable()
    i = 0

    #adding all information into package objects
    with open("packageCSV.csv") as pack:
        for line in pack:
            line = line.split(',')
            line[-1] = line[-1].strip()
            packs[i].insert(int(line[0]), line[1], line[5], line[2], line[4], int(line[6]), line[-1])
            i += 1

    #inserting values into hashtable
    for i in packs:
        hash_tab.insert(i.id, i)

    #Creating 3 truck objects that leave at different times to accommodate different times packages need to leave or arrive
    truck1 = Truck(hash_tab, 8)
    truck2 = Truck(hash_tab, 9, 5)
    truck3 = Truck(hash_tab, 10, 20)


    #manually inserted packages into trucks
    list1 = [packs[0], packs[3], packs[7], packs[12], packs[13], packs[14], packs[15], packs[18], packs[19], packs[20], packs[28], packs[29], packs[33], packs[38], packs[39]]
    list2 = [packs[2], packs[4], packs[5], packs[6], packs[17], packs[24], packs[25], packs[26], packs[27], packs[28], packs[30], packs[31], packs[34], packs[35], packs[36], packs[37]]
    list3 = [packs[8], packs[9], packs[10], packs[11], packs[21], packs[22], packs[23], packs[16], packs[1], packs[32]]

    #Loads packages into trucks
    load_truck(truck1, list1)
    load_truck(truck2, list2)
    load_truck(truck3, list3)

    #changes package statuses to en route, then changes status to deliver and removes from Truck
    #and then updates time and mileage for the truck
    deliver(truck2)
    deliver(truck1)
    deliver(truck3)


    #command line tool to make lookups easier
    while True:
        print("Welcome, please enter number for what you'd like!")
        print("1: Print all packages' delivery information and total mileage of trucks.")
        print("2: Print all information of a single package for a given time.")
        print("3: Print all information for all packages at a given time.")
        print("4: Exit program")
        try:
            user_in = int(input())
        except ValueError:
            print("User input invalid please enter 1, 2, 3 or 4")
            continue
        if user_in == 1:
            for i in range(len(hash_tab.table)):
                if len(hash_tab.table[i]) > 0:
                    print(hash_tab.search(i))
            print()
            print("Total mileage of all trucks:")
            print(truck1.mileage + truck2.mileage + truck3.mileage)
            print()
        elif user_in == 2:
            TIME = input("What time? (Please add time in HH:MM format)")
            ID = int(input("What is the package id number?"))
            print(lookUp(TIME, ID))
            print()
        elif user_in == 3:
            TIME = input("What time? (Please add time in HH:MM format)")
            for i in range(1, 41):
                print(lookUp(TIME, i))
            print()
        elif user_in == 4:
            print("Thank you for using WGUPS!")
            break
        else:
            print("User input invalid please enter 1, 2, 3 or 4")




