def enterage(age):
    if age<0:
        raise ValueError("only positive integers are allowed")
    
    if age%2==0:
        print("age is even")
        
    else:
        print("age is odd")
        
        
try:
    num = int(input("Enter your age: "))
    
except ValueError:
    print("only positive integers are allowed")