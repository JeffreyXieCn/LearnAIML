# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Python Basics

# %%
print("Hello World!")


# %%
#This is a comment
print("Learning Python in Jupyter")


# %%
test = "Hello"
print(type(test))

Test = 5
print(type(Test))


# %%
n = 5
k = 2
Product = k * n

print(type(Product))
print(Product)

# %% [markdown]
# # Python Standard Data Types

# %%
"""Here I define
two numbers"""
num1 = 23
num2 = 2.3

print(type(num1))
print(type(num2))


# %%
# Strings
str1 = "My first string"
print(str1) #My first string
print(str1[0]) #M
print(str1[3:8]) #first
print(str1[3:]) #first string
print(str1[-6:]) #string
print(str1 * 2) #My first stringMy first string
print(str1 + ' Test') #My first string Test
print(type(str1)) #<class 'str'>

str2 = "It's my pleasure to see you"
print(str2)

str3 = 'This is "My String"'
print(str3)


# %%
a = 3
b = 4
x = a + b
print(x)

x1 = 'a = %s, b = %s' % (a, b)
print(x1)

x2 = 'a: {}; b: {}'.format(a, b)
print(x2)

x3 = f'a is {a}; b is {b}'
print(x3)

# %% [markdown]
# ## Lists

# %%
list1 = [ 'abcd', 123, 10.2, 'EXAMPLE', 70.2 ]
list2 = [456, 'OTHER']

print(list1)
print(list2)

print(list1[0])
print(list1[1:3])
print(list1[1:2])
print(list1[1:1])
print(list1[2:])
print(list1[-2])
print(list1[-2:])
print(list1 * 2)
print(list1 + list2)

print(type(list1))
print(type(list1[1]))

print(list1[0][1])
print(type(list1[0][1]))


# %%
list3 = [ 'abcd', 123, 10.2, 'EXAMPLE', 70.2 ]

tuple1 = ( 'abcd', 123, 10.2, 'EXAMPLE', 70.2 )


# %%
a = [1, 2 , 3]
b = a; # refer to the same object
c = list(a) # Copy the value
d = [i for i in a] # Copy the value
a.append(4)
print(a)
print(b) # A change to "a" has resulted a change to "b"
print(c)
print(d)


# %%
# Immutable objects in Python: tuple and string

# "Change" a value in a tuple
is_Tuple = ("Orange", "Jaune", "Blue")
print(is_Tuple)

# is_Tuple[1] = "Yellow" # 'tuple' object does not support item assignment

#Solution
tupleToList = list(is_Tuple)
tupleToList[1] = "Yellow"
is_Tuple = tuple(tupleToList)
print(is_Tuple)
print(type(is_Tuple))

str1 = "abcxefg"
print(str1)
#str1[3] = "d" # 'str' object does not support item assignment

#Solution
str2 = str1[:3] + "d" + str1[4:]
print(str2)

str1 = str2
print(str1)


