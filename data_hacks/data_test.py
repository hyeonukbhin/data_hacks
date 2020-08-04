import random
import csv

f = open("data3.txt", 'w')

for i in range(1000):
    data = str(random.randint(0, 10000))
    # f.write(data)

    f.write(data+ "\n")

f.close()
