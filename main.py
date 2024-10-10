#011540261
from package import Package
from truck import Truck

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



# HashTable class using chaining.
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=50):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table.
    def insert(self, key, item):  # does both insert and update
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)

        # search for the key in the bucket list
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                return kv[1]  # value
        return None

    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

"""
def distanceBetween(addy1, addy2):
    for i in range(len(addys)):
        if addy1 == addys[i][2]:
            first = int(addys[i][0])
        elif addy2 == addys[i][2]:
            second = int(addys[i][0])



    return location[max(first, second)] [min(first, second)]"""


if __name__ == "__main__":
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
        hash_tab.insert(i.id, i.get_data()[0:])

    truck1 = Truck()
    truck2 = Truck()
    truck3 = Truck()
    print(truck1.current_time)
    truck2_list = [packs[36], packs[37], packs[35], packs[2], packs[17], packs[6]]
    truck1_list = [packs[0], packs[1],packs[2], packs[3], packs[4], packs[7], packs[8], packs[9], packs[11], packs[12], packs[13], packs[14], packs[15], packs[16]]
    for package in truck1_list:
        truck1.add_packages(package)
    print(packs[1].status)
    truck1.deliver()
    print(truck1.current_time)
    print(truck1.mileage)

    for pack in packs:
        print(pack.get_data())



