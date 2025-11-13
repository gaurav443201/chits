def add(queue, event):
    if event in queue :
        print("already exxist")
    else:
        queue.append(event)    
        print("event added")

def  process(queue):
    if event in queue :
        q= queue.pop(0)
        print(q,"event is processing.......")
    else:
        print("event not exist")    

def display(queue) :
    for i in queue:
        print(i)


def  cancel(queue):
    if event in queue :
        can = input("enter event to cancel :")
        queue.remove(can)
        print(can,"event is cancelled")
    else:
        print("event not exist")    




queue = []

while True :
    print("""
    1) add event
    2) processing event
    3) dislay    
    4) cancel event
    5) exit
    """)
    ch = int(input("enter your choice:"))
    if ch == 1:
        event= input("enter the event:")
        add(queue,event)
    elif ch == 2:
        process(queue)
        
    elif ch == 3:
        display(queue)    
    elif ch == 4:
        cancel(queue)
    elif ch == 5:
        break
    else :
        print("invalid choice")           
        