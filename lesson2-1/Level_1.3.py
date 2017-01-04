import random
random.seed()

full_list = []
unique_list = []

for i in range(0, 50):
    full_list.append(random.randint(0,10))

print full_list

for i in range(0, 20):
    if full_list[i] not in unique_list:
        unique_list.append(full_list[i])

print unique_list