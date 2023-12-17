import sys

sys.exit()

Running = True
user_list = []
user_input = None

list_name = input('What would you like to name your list?\n')

def clear():
    os.system('clear')

def add():
    item = input(f'What would you like to add to "{list_name}"?\n')
    if item:
        user_list.append(str(item))
    else:
        print('Invalid. Try again.')

def remove():
    if user_list:
        for i, item in enumerate(user_list, start = 1):
            print(f'{i}: {item}')
    else:
        print("There is nothing to remove!")
        return None
    try:
        index = int(input(f'Select a number to remove from "{list_name}".\n'))
    except:
        return None
    if (index <= len(user_list)):
        index -= 1
        del user_list[index]
        
def view():
    if not user_list:
        print('There is nothing in the list to view.')
        return None
    for i, item in enumerate(user_list, start = 1):
        print(f'{i}: {item}')
        
def alphabetize():
    if user_list:
        user_list.sort()
        print('Alphabetized!')
    else:
        print('There is nothing in the list to sort.')
    
def prompt():
    for i, option in enumerate(options, start = 1):
        print(f'{i}: {option}')
    user_input = input('Select a command.\n')
    try:
        number = int(user_input)
        user_input = options[(number-1)]
    except:
        pass
    if (user_input in commands):
        commands[user_input]()
    
def length():
    print(f'The length of your list is {len(user_list)}')

commands = {
    "add": add,
    "remove": remove,
    "view": view,
    "alphabetize": alphabetize,
    "length": length,
    "clear": clear
}

options = [key for key in commands.keys()]

while Running is True:
    prompt()
