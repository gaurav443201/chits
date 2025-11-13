# Division hash function method

def hash_function(k, size):
    return k % size

# Insert key in hash table
def insert(k):
    index = hash_function(k, size)
    for _ in range(size):
        if table[index] == -1:
            table[index] = k
            print("inserted")
            return
        elif table[index]== k:
            print("already ex")  
            return
        else:
            index = (index +1) % size
    print("HASH TABLE IS FULL")
    
# Search key in hash table
def search(k):
    index = hash_function(k, size)
    for _ in range(size):
        if table[index] == -1:
            break
        elif table[index]==k:
            print("found")
            return
        else:
            index = (index+1)%size
    print("not found")        

# Delete key from hash table
def delete(k):
    index = hash_function(k, size)
    for _ in range(size):
        if table[index] == -1:
            break
        elif table[index] == k:
            table[index ]= -1
            print("deleted")
            return
        else :
            index = (index+1)%size
              
    print("not found")  
# Display hash table
def display():
    index = hash_function(k, size)
    for i in range(size):
        print("index", i , ":",table[i])


size = int(input("ENTER SIZE OF HASH TABLE: "))
table = [-1] * size

while True:
    print("""
==== MENU ===
1. INSERT
2. SEARCH
3. DELETE
4. DISPLAY
5. EXIT
""")
    choice = input("ENTER YOUR CHOICE: ")

    if choice == "1":
        k = int(input("ENTER KEY TO INSERT: "))
        insert(k)
    elif choice == "2":
        k = int(input("ENTER KEY TO SEARCH: "))
        search(k)
    elif choice == "3":
        k = int(input("ENTER KEY TO DELETE: "))
        delete(k)
    elif choice == "4":
        display()
    elif choice == "5":
        print("THANK YOU !!!!")
        break
    else:
        print("INVALID CHOICE! PLEASE ENTER (1–5).")
