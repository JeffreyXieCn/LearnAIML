msg = "Hello World"
print(msg)

str0 = "Elementary, my dear Watson."
print(str0.rindex(' '))
print(len(str0))
print(str0[str0.rindex(' ') + 1 : len(str0) - 1])

str1 = "one, two, three, four, five"
print(type(str1))
print(", appears:", str1.count(","))

# Split a string into pieces
str2 = str1.split(',')
print(type(str2))
print(str2)

# ... without the whitespaces
str3 = str1.split(', ')
print(str3)
# or
str3 = [x.strip() for x in str1.split(',')]
print(str3)

list1 = [70, 25, 99, 100, 88]
list2 = list(list1)
list2.append(66)
list2.append(54)
list2.append(99)
print(list1)
print(list2)

list3 = list(list1)
list3.extend([66, 54, 99])
print(list1)
print(list3)

range1 = range(1, 10, 2)
for i in range1:
  print(i)