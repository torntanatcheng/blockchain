
"""Write a program which asks the user three times for a transaction amount, a recipient, sender information and saves it in an array.
Display the array at the end. It should have a structure like [[1,2,3],[1,2,3],[1,2,3]] (The third sender information)"""
# CMD + / to comment all code

history = [['', ['0', 'genesis' , '0']]]

def userInterface():

    choice = ''
    while choice != 'quit':

        print("\n[add] Enter add to a transaction")
        print("[edit] Enter edit to edit the blockchain")
        print("[print] Enter print to print blockchain")
        print("[genesis] Enter genesis to add genesis block")
        print("[quit] Enter quit program")
        choice = input("What do you want to do? \n")

        if choice == 'add':
            addTransaction()
            print(history)
        elif choice == 'print':
            printblock()
        elif choice == 'genesis':
            addGenesis()
        elif choice == 'edit':
            edit()
        elif choice == 'check':
            check()
        elif choice == 'quit':
            print("Thank you, come again!")

def addTransaction():

    for x in range(1):
        transaction = int(input("Whatchu wanna wanna send mother fucker? \n"))
        recipient = input("Who dis bish you talking to? \n")
        sender = input("Who da fuck are you? \n")
        history.append([history[-1], [transaction, recipient, sender]])

def addGenesis():

    history.append(['0', 'genesis' , '0'])
    print(history)

def printblock():
    print(history)

def edit():

    choice = int(input("What do you want to change?"))
    history[choice] = input("What do you want change it to")

def check():
    x = 1
    while x < len(history) and history[x][0] == history[x - 1]:
    # x < len(history): Make sure you don't exceed the range of the array.
    # history[x][0] == history[x - 1]: Check if the blockchain hasn't been hacked.
    # history[x][0]: Checking the previous reference of the current block history.
    # history[x - 1]: To check the previous block
        x += 1

    if x == len(history):
        print('You good dawg')
    else:
        print('You have been hacked')

userInterface()

#HOMEWORK: EXTEND YOUR PROGRAM WITH THE FOLLOWING
# - Terminal Interface
#     - Add Transaction
#     - Print the Blockchain
#     - Hack/Edit Blockchain
#     - Add Genesis Block
#     - Quit the Program
#     - Implement a function that checks the integrity of the blockchain. Start from the end and
#       check to see if it's the same as the previous block
#     - Add a summary of the previous block in the new block [['0', 'genesis' , '0']],
#     [previous_block, [transaction]],..]
#     - Create functions for everything