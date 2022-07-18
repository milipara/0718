from unittest import result


word = "banana"
# print(word)
result = {}

for char in word:
    print(char)
    if char not in result:
        result[char] = 1
    else:
        result[char] = result[char] + 1


#result = {}
#result['a'] = 0
#print(result)

#my_list = []
#my_list.append(1)
#print(my_list)