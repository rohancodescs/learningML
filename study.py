#dataset:

cities = [
    ["NY", 1000],
    ["NY", 4000],
    ["NY", 3200],
    ["DC", 6000],
    ["DC", 4000],
    ["DC", 2000],
]

def get_salaries(cities):
    hashmap = {}

    for i, j in cities:
        if i not in hashmap:
            hashmap[i] = [j, 1]
        else:
            hashmap[i][0] = hashmap[i][0] + j
            hashmap[i][1] = hashmap[i][1] + 1
    print(hashmap) #{'NY': [8200, 3], 'DC': [12000, 3]}

    #getting city average salaries
    for i in hashmap.items():
        print(f"City: {i[0]} Average Salary: {i[1][0] / i[1][1]}")

print(get_salaries(cities))
print("---------------------------------LEVEL 2------------------------------")



def get_high_low(cities):
    hashmap = {}

    for i, j in cities:
        if i not in hashmap:
            hashmap[i] = [j, 1]
        else:
            hashmap[i][0] = hashmap[i][0] + j
            hashmap[i][1] = hashmap[i][1] + 1
    highest = 0
    highestCity = ""
    lowest = None
    lowestCity = ""
    for city, data in hashmap.items():
        average = data[0] / data[1]
        if highest < average:
            highest = average
            highestCity = city
        if lowest is None or average < lowest:
            lowest = average
            lowestCity = city
            
    print(f"Highest COL: {highest}, City: {highestCity}")
    print(f"Lowest COL: {lowest}, City: {lowestCity}")
print(get_high_low(cities))