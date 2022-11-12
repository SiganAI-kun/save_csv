import csv

path = 'test_module.csv'
mode = 'w'
output_list = [[0, 1, 2, 3], [10, 11, 12, 13], [20, 21, 22, 23], [30, 31, 32, 33]]

with open(path, mode) as f:
	writer = csv.writer(f)
	writer.writerows(output_list)

with open(path) as f:
    print(f.read())
# 0,1,2,3

# 10,11,12,13

# 20,21,22,23

# 30,31,32,33