# Division hash function method (Chaining)

def hash_function(key, size):
    return key % size

# Insert key-value pair
def insert(key, value):
    index = hash_function(key, size)
    place= [key, value]
    
    for i in table[index]:
        if i[0] == key :
            print("existed")
            return
        
    table[index].append(place)    
    print("inserted")
    
# Search key
def search(key):
    index = hash_function(key, size)
    for item in table[index]:
        if item[0]== key:
            print("existed")
            return
    print("not found")  
      
# Delete key
def delete(key):
    index = hash_function(key, size)
    for item in table[index]:
        if item[0]== key:
            table[index].remove(item)
            return
        
    print("key not found")    
    
# Display hash table
def display():
    for i in range(size):
        print("index",i,":", table[i] )

size =10

table =table = [[] for _ in range(size)]


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
        key = int(input("ENTER KEY TO INSERT: "))
        value = input("ENTER VALUE: ")
        insert(key, value)
    elif choice == "2":
        key = int(input("ENTER KEY TO SEARCH: "))
        search(key)
    elif choice == "3":
        key = int(input("ENTER KEY TO DELETE: "))
        delete(key)
    elif choice == "4":
        display()
    elif choice == "5":
        print("THANK YOU !!!!")
        break
    else:
        print("INVALID CHOICE! PLEASE ENTER (1–5).")
