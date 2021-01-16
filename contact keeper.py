def menu(contacts):
    a=input("Type 1 to add a contact and 2 to retrieve:")
    if a=='1':
        name=input("Enter the name and number to add:")
        no=input()
        add_contact(contacts,name,no)
    elif a=='2':
        name=input("Enter name to retrieve its contact:")
        print(retrieve(contacts,name))
    else:
        print("Not an available option.Try again")
def add_contact(contacts,name,no):
    try:
        contacts[name]+=[no]
    except KeyError:
        contacts[name]=[no]
def retrieve(contacts,name):
    return contacts[name]
contacts={}
n=input("Welcome, press any key to start exploring our contact keeper. Type 'quit' to quit. ")
while n!='quit':
    menu(contacts)
    n=input("Press any key to continue. Type 'quit' to quit:")
