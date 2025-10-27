try:
    age=int(input('Enter your age:'))
except:
    print("Please enter correct number ot data")

if age%2==0:
    print("age number is even")
else:
    print("age number is odd")
