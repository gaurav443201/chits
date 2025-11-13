def create(char,undo, redo):
    undo.append(char)  
    redo.clear()
    print("change added:", undo)
    

def undo( undo, redo):
    if len(undo) == 0:
        print("noothing to undo")
    else :
        char = undo.pop()
        redo.append(char)
        print("undo succesfully")
        
        
def redo( undo, redo):
    if len(redo) == 0:
        print("noothing to redo")
    else:
        char= redo.pop()
        undo.append(char)
        print("redo SUCCESSFULLY")
        
def display(undo):
    print("current text:",undo)

u_st = []
r_st = []


while True :
    print("""
    1) make a change
    2) undo
    3) redo
    4) display doc
    5) exit
    """)
    ch = int(input("enter your choice:"))
    if ch == 1:
        char = input("enter the text:")
        create(char, u_st, r_st)
    elif ch == 2:
        undo( u_st, r_st)
    elif ch == 3:
        redo( u_st, r_st)
    elif ch == 4:    
        display(u_st)
    elif ch == 5:    
        break
    else :
        print("invalid  choice !!!")      