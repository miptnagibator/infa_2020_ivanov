

file = open('top.txt', 'r')
data =[]

while True:
    a = file.readline()
    if a == "":
        break
    data.append(a)
for i in range(len(data)):
    a = data[i]
    a = a.split()
    data[i] = a


print(data)
file.close()



def sort_col(i):
    return int(i[1])


data.sort(key=sort_col)
print(data)