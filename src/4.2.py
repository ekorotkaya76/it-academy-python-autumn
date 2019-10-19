#Use a list comprehension to construct the list ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].

lst1 = [y + x for y in 'ab' for x in 'bcd']
print(lst1)

#Use a slice on the above list to construct the list ['ab', 'ad', 'bc'].
lst1 = [y + x for y in 'ab' for x in 'bcd']
print(lst1[0:5:2])

#Use a list comprehension to construct the list ['1a', '2a', '3a', '4a'].
lst1 = [y + x for y in '1234' for x in 'a']
print(lst1)

#Simultaneously remove the element '2a' from the above list and print it.
lst1 = [y + x for y in '1234' for x in 'a'].pop(1)
print(lst1)

#Copy the above list and add '2a' back into the list such that the original is still missing it.
