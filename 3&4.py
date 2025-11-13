def linear(ecom,n):
    num = int(input(" enter the id to find:"))
    for i in range(n): 
        if ecom[i]== num :
            print("found")
            break
    
    else:
        print("not found")
        
    
def  bianary(ecom):
    num = int(input(" enter the id to find:"))
    
    low = 0
    high = len(ecom) - 1
    
    while low <= high:
        mid = (low + high)// 2
        if ecom[mid] == num :
            print("found")
            break
        elif ecom[mid] < num :
            low = mid + 1
        elif ecom[mid]> num :
            high = mid - 1
    else:
        print("not found")
                        

n =  int(input("enter the num of employeee :"))
ecom = []

for i in range(n):
    emp = int(input(f"enter the id of employee {i+1}:"))
    ecom.append(emp)

print(emp)    
ecom.sort() 
print("SORTED ACC IDS:", ecom)

while True :
    print('''
    ++++++++++++ Display Menu +++++++++++++     
    1) linear search
    2) bianary search     
        
    ''')
    ch = int(input("choice:"))
    
    if ch == 1:
        linear(ecom,n)
    
    elif ch == 2:
        bianary(ecom)  
    elif ch == 3:
        break
    else :
        print("invalid  choice !!!")     
         