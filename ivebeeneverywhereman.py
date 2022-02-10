loop = int(input())
count = [0] * loop

for i in range(loop):
    cities = int(input())
    array = []
    for j in range(cities):
        name = input()
        if (name not in array):
            array.append(name)
    
    count[i] = len(array)
    print(len(array))

