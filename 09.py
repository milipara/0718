from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = dict()

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count[fruit] = 0
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)