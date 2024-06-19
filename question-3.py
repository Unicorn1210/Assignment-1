x=int(input("Enter the number to claculate it's factorial:"))
factrl=1
if x==1 or 0:
    print("The factorial is 1")
else:
    for i in range(1, x+1):
        factrl*=i
    print("The factorial is", factrl)