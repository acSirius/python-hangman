import random

a_file = open('countries.txt', 'r')
list_of_lists = [(line.strip()).split() for line in a_file]
a_file.close()

print(random.choice(list_of_lists))