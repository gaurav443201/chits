def linear(roll, n):
    std =int(input("Enter thr roll to find :"))
    for i in range(n):
        if roll[i] == std:
            print("found")
            break
    else :
        print("not found")        
    
    
def binary(roll):
    std =int(input("Enter thr roll to find :"))
    low = 0 
    high = len(roll) - 1
    
    while low <= high :
        mid= (high +low)//2
        if roll[mid] == std:
            print("found")
            break
        elif roll[mid] < std:
            low = mid +1
        elif roll[mid] > std:
            high = mid - 1        
    else :
        print("not found ")

n =  int(input("enter the num of student :"))
roll = []

for i in range(n):
    emp = int(input(f"enter the roll no. of student {i+1}:"))
    roll.append(emp)

print(emp)    
roll.sort() 
print("SORTED ACC IDS:", roll)

while True :
    print('''
    ++++++++++++ Display Menu +++++++++++++     
    1) linear search
    2) bianary search     
        
    ''')
    ch = int(input("choice:"))
    
    if ch == 1:
        linear(roll,n)
    
    elif ch == 2:
        binary(roll)  
    elif ch == 3:
        break
    else :
        print("invalid  choice !!!")      