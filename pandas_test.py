import pandas as pd

input_path = 'original.csv'
data = pd.read_csv(input_path, header=None)
print(data)
#     0   1   2   3
# 0   0   1   2   3
# 1  10  11  12  13
# 2  20  21  22  23
# 3  30  31  32  33

output_path = 'test_pandas.csv'
data.to_csv(output_path, header=False)

with open(output_path) as f:
	print(f.read())
# 0,0,1,2,3
# 1,10,11,12,13
# 2,20,21,22,23
# 3,30,31,32,33

output_path_2 = 'test_pandas_2.csv'
data.to_csv(output_path_2, header=False, index=False)

with open(output_path_2) as f:
    print(f.read())
# 0,1,2,3
# 10,11,12,13
# 20,21,22,23
# 30,31,32,33