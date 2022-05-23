import random
import time


def task1(_length):
    print("Random keys count: ", pow(2, _length))


def task2(length):
    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    mystr = ""
    for i in range(0, length):
        mystr += random.choice(chars)

    return "0x" + mystr


def task3_brute_force(hex_key):
    value = int(hex_key, 0)
    start_time = time.time()
    i = 0
    while True:
        if i == value:
            print("--- Key " + hex_key + " found, it took %s seconds ---" % (time.time() - start_time))
            break
        else:
            i += 1


bits = int(input("Print key length (bits): "))

# 1
task1(bits)

# 2
key = task2(bits // 4)
print("Random key value: ", key)

# 3
task3_brute_force(key)
