
t = [list(item) for item in zip(*[iter(table_list[0])]*chunk)]

for item in table_list:
    fixed_list=[]
    chunk = 8
    item = item[1:]
    fixed_list.append(zip(*[iter(item)]*chunk))


for tup in zipped:
    df_list = []
    yr = tup[0]
    chunk = 8
    df = pd.DataFrame([list(item) for item in zip(*[iter(tup[1][1:])]*chunk)])
    df_list.append(df)




# df = pd.DataFrame(fixed_list).T
# In [118]: df
# Out[118]:
#                                                      0
# 0    (Hamilton, Bermuda, 132.32, 120.87, 126.82, 12...
# 1    (San Francisco, CA, United States, 103.36, 121...
# 2    (New York, NY, United States, 100.00, 100.00, ...
# 3    (Honolulu, HI, United States, 99.72, 64.46, 82...
# 4    (Washington, DC, United States, 96.18, 72.17, ...
# 5    (Anchorage, AK, United States, 93.85, 42.50, 6...
# 6    (Allentown, PA, United States, 92.69, 34.27, 6...
# 7    (Albany, NY, United States, 90.13, 28.97, 60.7...
# 8    (Stamford, CT, United States, 89.25, 64.20, 77...
