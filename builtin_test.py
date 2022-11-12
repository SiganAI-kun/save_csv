path = 'test_builtin.csv'
mode = 'w'
output_list = [[0, 1, 2, 3], [10, 11, 12, 13], [20, 21, 22, 23], [30, 31, 32, 33]]

with open(path, mode) as f:
    for i in range(len(output_list)):
        output = [str(index) for index in output_list[i]]
        output = ','.join(output)
        f.write(output + '\n')

with open(path) as f:
	print(f.read())
# 0,1,2,3
# 10,11,12,13
# 20,21,22,23
# 30,31,32,33