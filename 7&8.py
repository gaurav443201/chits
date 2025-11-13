def selection(com,n):
    for i in range(n):
        min_ind = i
        for j in range( i +1, n):
            if com[j]< com[min_ind]:
                min_ind = j
        com[i], com[min_ind] =  com[min_ind] , com[i]
    print(com)   
    
    
    print(com[-1:-6:-1])
         

def bubble(com,n) :
    for i in range(n):
        for j in range(0,n-i-1):
            if com[j] > com[j+1]:
                 com[j] ,com[j+1] = com[j+1] ,com[j]
    print(com)      



n =  int(input("enter the num of employeee :"))
ecom = []

for i in range(n):
    emp = int(input(f"enter the salaries of employee {i+1}:"))
    ecom.append(emp)

print(emp)    

while True :
    print('''
    ++++++++++++ Display Menu +++++++++++++     
    1) selection sort
    2) bubble sort   
    3) exit    
    ''')
    ch = int(input("choice:"))
    
    if ch == 1:
        selection(ecom,n)
    elif ch == 2:
        bubble(ecom,n)  
    elif ch == 3:
        break
    else :
        print("invalid  choice !!!")     
         