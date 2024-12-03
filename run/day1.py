from collections import deque

def read_file():
    with open("./run/day1_1.txt", 'r') as file:
        data = file.readlines()
    data = list(map(lambda x: x.replace("\n", " "), data))
    data = " ".join(data).split(" ")
    data = list(map(lambda x: int(x) if x != "" else -1, data))
    data = list(filter(lambda x: x > -1, data))
    return data

def part1():
    data = read_file()

    list1 = deque(data[0::2])
    list2 = deque(data[1::2])
    total = 0
    while len(list1) > 0:
        total += abs(min(list1) - min(list2))
        list1.remove(min(list1))
        list2.remove(min(list2))
        
    print(f"part1: {total}")

def part2():
    data = read_file()

    cache = {}
    
    list1 = deque(data[0::2])
    list2 = deque(data[1::2])
    total = 0
    for val1 in list1:
        if val1 in cache:
            total += cache[val1] * val1
            continue
        count = 0
        for val2 in list2:
            if val1 == val2:
                count += 1
        cache[val1] = count
        total += count * val1
        
    print(f"part2: {total}")
    
if __name__ == "__main__":
    part1()
    part2()

