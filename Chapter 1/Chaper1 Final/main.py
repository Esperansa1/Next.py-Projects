from functools import reduce 

# Q1
with open('names.txt', 'r') as names_file:
    print(reduce(lambda x, y : x if len(x) > len(y) else y, [name.strip() for name in names_file.readlines()]))


# Q2
with open('names.txt', 'r') as names_file:
    print(sum([len(name.strip()) for name in names_file.readlines()]))


# Q3
with open('names.txt', 'r') as names_file:
    names = names_file.readlines()
    min_length = min([len(name.strip()) for name in names])
    shortest_names = [name.strip() for name in names if len(name.strip()) == min_length]
    list(map(print, shortest_names))


# Q4
with open('names.txt', 'r') as names_file:
    with open('name_length.txt', 'w+') as length_file:
        list(map(lambda length : length_file.write(str(length)+"\n"), [len(name.strip()) for name in names]))


# Q5
with open('names.txt', 'r') as names_file:
    wanted_length = int(input("Enter the wanted length: "))
    list(map(print,[name.strip() for name in names if len(name.strip()) == wanted_length]))