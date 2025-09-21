# There are 4 built-in data types used to store collections of data, Tuples, List, Set, and Dictionary.
# A tuple is a collection which is ordered and unchangeable.
my_tuple = ("apple", "banana", "cherry", "apple", "cherry", 123, True, False, 3.14)
print(my_tuple)
print(my_tuple[6])
print(my_tuple[2:5])
print(type(my_tuple))
if "apple" in my_tuple:
    print("Yes, 'apple' is in the tuple")   
print(len(my_tuple))

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

# unpack a tuple
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")  
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)