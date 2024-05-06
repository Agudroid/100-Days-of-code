file1_list = []
file2_list = []

with open('file1.txt', mode='r') as file:
    lines = file.readlines()
    print(lines)
    for line in lines:
        row = line.split()
        print(row)
        file1_list.append(row[0])

with open('file2.txt', mode='r') as file:
    lines = file.readlines()
    print(lines)
    for line in lines:
        row = line.split()
        print(row)
        file2_list.append(row[0])

result1 = [int(n) for n in file1_list if n in file2_list]
result2 = [n for n in file2_list if (n in file1_list) and (n not in result1)]
result1 += result2
print(result1)
