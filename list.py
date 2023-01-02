fruits=['apple','orange','grapes','guava','jackfruit']
anyType=[1,True,'Hello']

print(fruits)
print(len(fruits))
print(fruits[2])
print(anyType)
# print(type(anyType))
print(fruits[-2])
print(fruits[1:3])
print(fruits[2:])
print(fruits[:1])
print(fruits[-2:-1])

if 'apple' in fruits:
    print("Its here")
fruits[2]='craneberry'
print(fruits)

fruits[1:4]=['strawberry','watermelon']
fruits.insert(6, 'pineapple')
fruits.append('lemon')
tropical=['guyabano','banana']
fruits.extend(tropical)

print(fruits)








