import os

my_file = 'data/myfile.txt'
my_file = os.path.join('data', 'myfile.txt')

f = open(my_file)
lines = f.readlines()
for line in lines:
    print(line)
f.close()

with open(my_file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line)

