# Python Collections (Arrays)
# There are four collection data types in the Python programming language:
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
my_tuple = ("apple", "banana", "cherry", "apple", "cherry", 123, True, False, 3.14)
print(my_tuple)
print(my_tuple[6])
print(my_tuple[2:5])
print(type(my_tuple))
if "apple" in my_tuple:
    print("Yes, 'apple' is in the tuple")   
print(len(my_tuple))

# tuple methods: count(), index(), len(), min(), max(), sum(), sorted(), del
# print(len(tuple_example))
print(tuple_example.count(2))
print("Hello is at index:", tuple_example.index("Hello"))
print(min((1, 2, 3, 0, 4, 5)))
print(max((1, 2, 3, 4, 5)))
print(sum((1, 2, 3, 4, 5)))
print(sorted((3, 1, 4, 2, 5)))
# del tuple_example[0] # This will raise a TypeError
del tuple_example  # This will delete the entire tuple


# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(thistuple)

print('----Change Tuple Values----')
# Tuples are unchangeable, or immutable, but there are workarounds.
x = ("apple", "banana", "cherry")
# convert it to a list
y = list(x)
y[1] = "kiwi"
y.append("orange")
y.remove("apple")
x = tuple(y)
print(x)

# Add items
tuple1 = ("apple", "banana", "cherry")
tuple2 = ("orange",)
tuple2 += tuple1
print(tuple2)

# unpack a tuple, use * to collect the remaining values as a list
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")  
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

print('-----Loop Through the Index Numbers-----')
# Use the len() function to determine the length of the tuple
for i in range(len(fruits)):
    print(i)
    print(fruits[i])
    
i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1

print('-----Adding two tuples-----')
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

print('-----tuple Methods-----')
# count(), index()
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(f"{5} is repeated = {x} time(s)")
y = thistuple.index(8)
print(f"The first occurrence of {8} is at index = {y}")

# Sets
# A set is a collection which is unordered and unindexed. 
# In Python sets are written with curly brackets.
# Once a set is created, you cannot change its items, but you can add new items.

my_set = {"apple", "banana", "cherry"}
for x in my_set:
  print(x)
my_set.add("orange")
my_set.add("orange")
my_set.add("pear")
print(my_set)

# To add items from another set into the current set, use the update() method.
set1 = {"a", "b" , "c"} 
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
# To remove an item in a set, use the remove(), or the discard() method.
# The difference between remove() and discard() is that remove() will raise an error if the item to remove does not exist, and discard() will not.
set1.remove(2)  
set1.discard(5)
print(set1)

print('-----------Dictionary-----')
# As of Python version 3.7, dictionaries are ordered, not before.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

thedict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thedict))
# String, int, boolean, and list data types:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "is_new": True,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
