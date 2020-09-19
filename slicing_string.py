# Indexing
# Jumat 18 september 2020

a = len("Hello")
print(a) #5

# grab single characters from string
mystring = "Hello World"
print(mystring[2])
# reverse
print(mystring[-3])

#Slicing
mystring2 = "abcdefghijk"
print(mystring2[2:]) # cdefghijk
print(mystring2[:3]) # ab
print(mystring2[3:6]) # def

## How to use Step
print(mystring2[::2]) # acegik
## abcdefghijk
print(mystring2[2:7:2]) # ceg

##reverse to string
print(mystring2[::-1]) #kjihgfedcba