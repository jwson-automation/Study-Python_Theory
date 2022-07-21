#!C:\Users\jwson\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.7
# print("hello,world")
x = input('Could I ask your age?')
birth = int(x)

birthday=input('Have you already had your birthday?(y/n)')

if birthday=='y':
    print('Us age: ',birth-1)
else:
    print('Us age: ',birth-2)