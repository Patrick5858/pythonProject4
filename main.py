
print("(The value of x is , x)")
print ('This is a \n'
       'check out this')
# Integers
x = 5
print('x is a type',type(x),'\n')
y = 1.234
print('x is a type',type(y), '\n')
z = 1.2333333345678
print('x is a type',type(z), '\n')
k = True
print('x is a type',type(k),'\n')
r = 'This is Kenya'
print('x is a type',type(r),'\n')
# List
mylist1 = ['Jane','John','Kim']
print(type(mylist1))
print(mylist1)
#Access Items
print(mylist1[0])
#Negative Indexing
print(mylist1[-1])
print(mylist1[0:2])
mylist2 = ['Kirinyaga', 'Embu','Nyeri','Kiambu', 'Nakuru']
print(mylist2[2:4])
#Tuples
mylist1.append('Rose')
print(mylist1)

print(len(mylist1))
#1D Array
myarray = [1,3,4,5,6]
print(type(myarray))
#2D array
myarray2 =[[1,3,4,5,6],
           ['f','h','y','w']]
print(type(myarray2))
#dictionary
mydictionary ={
       "Programe":"PA100",
"Age":23,
"County":"Embu"
         }
print(type(mydictionary))
print(mydictionary['Age'])
print(mydictionary['County'])
mydictionary.get('Age')
print(mydictionary.get('Age'))
mydictionary['Age']=34
print(mydictionary)


v1 =[3,5,6,7]
v2 = [9,3,5,2]
a1 =v1,v2

print(a1)
results =[x*y for x,y in zip(v1,v2)]
print(results)
w =9
y = 3
print(w>y)
print(w<y)
print(v1<v2)
print((w!=y))

#control structure
# If... else
years =23
if years >=18:
    print('You are an adult')
    print('you have', years, 'Years.')
else:

    print('You are an adult')
    print('you have', years, 'Years.')
n=int(input('Enter a number')
if n>=0:
    print('n',"is a positive number")
elif n==0:
    print(n, "is zero")
else:
    print(n,"is a negative number")
)


