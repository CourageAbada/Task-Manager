# Task-Manager
This code is a simple task management system that allows users to log in, add tasks, view all tasks, view their tasks, and view statistics.

Login
The system starts by asking the user to log in with their username and password. It checks if the entered username and password match the stored usernames and passwords in the user.txt file. If the password does not match, the user is prompted to try again until they provide the correct credentials.

Task Management
Once the user is logged in, they are presented with a menu where they can choose from the following options:

r: Registering a user (only admin)
a: Adding a task
va: View all tasks
vm: View my task
d: Display statistics (only admin)
e: Exit
Registering a User
If the user selects the r option, they are prompted to enter the details for the new user's account. Only the admin is allowed to register new users. Once the admin enters the details, the system stores them in the user.txt file.

Adding a Task
If the user selects the a option, they are prompted to enter details about the task, including the task title, description, due date, and whether the task is complete or not. The system stores this information in the tasks.txt file.

Viewing All Tasks
If the user selects the va option, the system displays all the tasks stored in the tasks.txt file.

Viewing My Tasks
If the user selects the vm option, the system displays only the tasks assigned to the logged-in user.

Displaying Statistics
If the user selects the d option, the system displays the total number of tasks and users in the system. Only the admin is allowed to view this information.

Exiting
If the user selects the e option, the system ends and the user logs out.

Usage
To use this task management system, simply run the code in a Python environment. The system will prompt the user to enter their credentials, and they can then choose from the available options. Note that some options are only available to the admin user.

The system stores user information in the user.txt file and task information in the tasks.txt file. Be sure to keep these files in the same directory as the code.
