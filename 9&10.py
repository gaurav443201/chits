def linear(roll,n):
    for i in range(n):
        min_ind = i
        for j in range(i+1,n):
            if roll[j]< roll[min_ind]:
                min_ind =j
        roll[j],roll[min_ind]  =roll[min_ind] , roll[j]      
    print(roll)



def binary(roll,n):
    for i in range(n):
        for j in range(0,n-i-1):
            if roll[j+1]> roll[j]:
                roll[j+1], roll[j] = roll[j] ,roll[j+1]
    print(roll)




n =  int(input("enter the num of student :"))
roll = []

for i in range(n):
    emp = int(input(f"enter the roll no. of student {i+1}:"))
    roll.append(emp)


while True :
    print('''
    ++++++++++++ Display Menu +++++++++++++     
    1) selection sort
    2) bubble sort   
    3) exit 
    ''')
    ch = int(input("choice:"))
    
    if ch == 1:
        linear(roll,n)
    
    elif ch == 2:
        binary(roll,n)  
    elif ch == 3:
        break
    else :
        print("invalid  choice !!!")      