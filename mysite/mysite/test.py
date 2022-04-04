
num = 6
for i in range(2, num+550):
    counter = 1
    for u in range(1, counter):
        if num % u == 0:
            counter += 1
        else:
            print(counter)


