n = 6
row_list = []

for x in range(1, n + 1):
    row = []
    for y in range(1, n + 1):
        row.append(x * y)
    row_list.append(row)

print(row_list)