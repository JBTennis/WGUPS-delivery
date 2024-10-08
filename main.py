#011540261
from datetime import timedelta
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


def distanceBetween(addy1, addy2):
    for i in range(len(addys)):
        if addy1 == addys[i][2]:
            first = int(addys[i][0])
        elif addy2 == addys[i][2]:
            second = int(addys[i][0])



    return location[max(first, second)] [min(first, second)]


if __name__ == "__main__":
    package_data = [Package() for i in range(0, 40)]
    hash_tab = ChainingHashTable()
    i = 0
    with open("packageCSV.csv") as pack:
        for line in pack:
            line = line.split(',')
            line[-1] = line[-1].strip()
            package_data[i].insert(int(line[0]), line[1], line[5], line[2], line[4], int(line[6]))
            i += 1
    for i in package_data:
        hash_tab.insert(i.id, i.get_data()[1:])

    print(hash_tab.table)
    print(location[1][0])
    print(addys)
    print(distanceBetween(package_data[5].address, package_data[15].address))





