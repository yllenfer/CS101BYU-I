message = input("Enter a number to count to: ")
num = int(message)
for i in range(1,num+1):
    print(i)

print("Now we are going to count down: ")
for i in reversed(range(1,num+1)):
    print(i)
