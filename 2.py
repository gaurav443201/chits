def avg(lib,n):
    sum = 0
    for i in lib :
        sum += i 
    print(sum)
    avg = sum / n 
    print(avg)    
    
def high(lib):
    max = -1
    for i in lib :
        if i > max :
            max = i
        else :
            pass    
    print(max)   
     
def low(lib):
    min = lib[0]
    for i in lib :
        if i < min :
            min = i
        else :
            pass  
    print(min)
    
def count(lib) :
    count = 0 
    for i in lib :
        if i == 0:
            count+=1
    print(count)
            

def freq(lib):
    for marks in set(lib):
        print(marks ,"->", lib.count(marks))
        
    c = 0
    f = 0 
    for mark in set(lib):
        count = lib.count(mark)
        if count > c:
            c = count
            f = mark
    print("MOst frequent:",f, "is", c)           








#---------------------------------------------------------------------------
n = int(input("enter the number of students:"))
lib =[]

for i in range(n):
    stud= int(input(f"Enter marks of the stud {i +1} :"))
    lib.append(stud)
print(lib)    


while True :
    print("""Display menu 
    1) avg
    2) high
    3) low 
    4) count 
    5) freq
    6) exit
    """)
    ch = int(input("Enter your choice:"))
    if ch== 1:
        avg(lib,n)
    elif ch == 2:
        high(lib)
    elif ch == 3:
        low(lib)   
    elif ch== 4:
        count(lib)
    elif ch == 5:
        freq(lib)
    elif ch== 6:
        break 
    else :
        print("invalid choice !!!")    
        
        