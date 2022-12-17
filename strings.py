#simple string
strings="hi"
print(strings)

#multiline string

multi="""
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua
"""

print(multi)

#strings are Array

sample="Hello World"
print(sample[8])

for i in (sample):
    print(i)

print(len(sample))
print("Hello" in sample)
print("Hello" not in sample)
print(sample.capitalize())
print(sample.endswith("r"))

#Slice from the start
print(sample[:6])

#Slice To the End
print(sample[3:])

#Negative Indexing
print(sample[-6:-1])

#Split String
print(sample.split("."))

#concat








