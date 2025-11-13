def addcall(queue,callid,time):
    queue.append([callid, time])
    print("call added ",callid,"at", time , "min"  )

def  answercall(queue):
    if len(queue)==0:
        print("no call found")
    else :
        call= queue.append(0)    
        print("Answered call from:", call[0])

def viewqueue(queue)  :
    print("current call queue")
    for call in queue:
        print("Customer ID:", call[0], "| Time:", call[1], "min")   

def isempty(queue):
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Queue is not empty.")



queue = []

while True :
    print("""
Menu:____________
1) Add Call
2) Answer Call
3) View Queue
4) Check if Queue Empty
5) Exit
    """)
    ch = int(input("enter your choice:"))
    if ch == 1:
        callid= input("enter the customer id :")
        time = input("enter the call time :")
        addcall(queue,callid,time)
    elif ch == 2:
        answercall(queue)
        
    elif ch == 3:
        viewqueue(queue)    
    elif ch == 4:
        isempty(queue)
    elif ch == 5:
        break
    else :
        print("invalid choice")           
        