#Login section asking the user to login and checking to see if the username and password match the stored username and passwords that are in user.txt
#If Password does not match then user should try again
with open('user.txt', 'r') as file:
    username_password = file.readlines()
    while True:
        logged_in = False
        print('Please enter the following details:')
        username = input('Username:')
        password = input('Password:')
        for i in username_password:
            split_data = i.strip().split(", ")
            cor_user = split_data[0].strip("\n")
            cor_pass = split_data[1].strip("\n")
            if password == cor_pass and username == cor_user:
                logged_in = True
                break
            elif password != cor_pass and cor_user != username:
                continue
        else:
            print('User does not exist please enter the correct username and Password')
        if logged_in:
            print("Logged in")
            break

while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
d - display statistics
e - Exit
: ''').lower()
# Only allowing the admin to register new users if the user is not admin then error message will be desplayed
    if menu == 'r':
        if username == 'admin':
            with open('user.txt', 'a+') as file:
                print('Please enter the following details to create a new account:')
                new_username = input('Username: ')
                new_password = input('Password: ')
                password_confirmation = input('Please confirm your Password: ')
                while True:
                    if new_password == password_confirmation:
                        print('Well done you have registered sucessfully')
                        file.write(f"\n{new_username}, {new_password}")
                        break
                    else:
                        print('Please enter the correct password:')
                        password_confirmation = input('Please confirm your Password: ')
        else:
            print('Only admin is allowed to register new users ')
#If the user inputs a then it will allow them to add a task
    elif menu == 'a':
        with open('tasks.txt', 'a+') as file:
            print('Please enter the following information about the tasks:')
            task_username = input('The person\'s username: ')
            task_title = input('The task title: ')
            task_description = input('Description of the task: ')
            task_duedate = input('Task Due Date: ')
            current_date = input('Current date: ')
            task_complition = 'No'
            file.write(f"\n{task_username}, {task_title}, {task_description}, {task_duedate}, {current_date}, {task_complition} ")
# If user inputs va then it allows them to view all tasks
    elif menu == 'va':
        with open('tasks.txt', 'r+') as file:
            for line in file:
                split_data = line.split(', ')
                peoples_names = f"""Name: {split_data[0]}\nTask: {split_data[1]}\nTask Description: {split_data[2]}\nTask Due Date: {split_data[3]}
                \nCurrent date: {split_data[4]}\nIs the task complete: {split_data[5]}"""
                print(peoples_names)
#If user inputs vm it allows them to only view their tasks
    elif menu == 'vm':
        with open('tasks.txt', 'r+') as file:
            for line in file:
                task_username, task_title, task_description, task_duedate, current_date, task_complition = line.split(", ")
                if username ==  task_username:
                    print(f'''Name: {task_username}\nTask: {task_title}\nTask Description: {task_description}
                    \nTask Due Date: {task_duedate}\nCurrent date: {current_date}\nIs the task complete: {task_complition}''')
#only allows user to view statistics
    elif menu == 'd' and username == 'admin':
            task_num = 0
            user_num = 0
            with open('tasks.txt', 'r') as task_title:
                for line in task_title:
                    task_num += 1
            print(f'\nTotal number of task: {task_num}')

            with open('user.txt', 'r') as username:
                for line in username:
                    user_num +=1
            print(f'\nTotal number of users: {user_num}')
#Allows user to leave once done
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
# Asks user to reenter their choice if they have selected the wrong option
    else:
        print("You have made a wrong choice, Please Try again")
