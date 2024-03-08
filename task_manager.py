import os
from datetime import datetime, date
import sys

# Program designed as task manager, able to register users and tasks to then track.
# Information on tasks include: name of assigned user, description of the task, the date it was set, the date it needs to be completed and the status of completion.
# Manage these tasks by editing and marking the completion of tasks. Furthermore, tasks can be interchanged with different users.
# Overview reports can be generated, shows the statistics of the task manager and for each user.
# Original pseudocode from inital code file has not been changed.

DATETIME_STRING_FORMAT = "%Y-%m-%d"


def reg_user():
    '''Add a new user to the user.txt file'''
    while True:
        # - Request input of a new username
        new_username = input("New Username: ")
        
        # - Request input of a new password
        if new_username in username_password:
            
            print("This Username is already in use. Please choose a different username. ")
            
            continue
        
        # - Request input of a new password
        new_password = input("New Password: ")
                             
        # - Request input of password confirmation.                     
        confirm_password = input("Confirm Password: ")
        
        # - Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
            username_password[new_username] = new_password
            with open("user.txt", "w") as out_file:
                user_data = [f"{k};{username_password[k]}" for k in username_password]
                out_file.write("\n".join(user_data))
            return "New user added"
        
        # - Otherwise you present a relevant message.
        else:
            return "Passwords do not match"


def add_task():
    '''Allow a user to add a new task to task.txt file
        Prompt a user for the following: 
         - A username of the person whom the task is assigned to,
         - A title of a task,
         - A description of the task and 
         - the due date of the task.'''
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        return "User does not exist. Please enter a valid username"
    
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print("Invalid datetime format. Please use the format specified")
    
    # Then get the current date.
    curr_date = date.today()
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False}

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"]
            
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    return "Task successfully added."


def view_all():
    '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
    '''
    
    # Empty list created for task information (tasks_disp) so it does not return NoneValue error when -1 is inputted initially.
    tasks_disp = []
    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        tasks_disp.append(disp_str)
    return tasks_disp


def view_mine():
    '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
    '''
    tasks_disp = []
    for i, t in enumerate(task_list):
        if t['username'] == curr_user:
            disp_str = "-" * 80 + "\n" + f"Task {len(tasks_disp)+1}: \t\t {t['title']}\n" + "-" * 80 + "\n"
            disp_str += f"Assigned to: \t\t {t['username']}\n"
            disp_str += f"Date Assigned: \t\t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t\t\t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description:\t {t['description']}\n"
            disp_str += f"Task Completion: \t {'Complete' if t['completed'] else 'Incomplete'}\n"
            tasks_disp.append((i, disp_str))

    for task_indx, task_disp in tasks_disp:
        print(task_disp)

    while True:
        task_input = input("Select the number of the task you would like to edit, or enter -1 to return to the menu: ")
        if task_input == "-1":
            return []
        else:
            task_num = int(task_input)
            task_indx = task_num -1
            if 0 <= task_indx < len(tasks_disp):  
                edit_task = input("Press E to edit the task or M to mark the task's completion: ")
                print(f"Selected Task: {task_num }")  
                if edit_task == "M":
                    completion_input = input("Is this task complete? (Yes or No): ")
                    if completion_input.upper() == "YES":
                        task_list[task_num]['completed'] = True
                        print("Task is complete")
                    elif completion_input.upper() == 'NO':
                        task_list[task_num]['completed'] = False
                        print("Task is incomplete")
                    with open("tasks.txt", "w") as task_file:
                        for t in task_list:
                            str_attrs = [
                                t['username'],
                                t['title'],
                                t['description'],
                                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                                "Yes" if t['completed'] else "No"]
                            task_file.write(";".join(str_attrs)+ "\n")
                elif edit_task == 'E':
                    new_user = input("Enter the new name that the task is assigned to: ")
                    new_date = input("Enter the new date that it is due: ")
                    try:
                        new_date = datetime.strptime(new_date, DATETIME_STRING_FORMAT)
                        task_list[task_num]['username'] = new_user
                        task_list[task_num]['due_date'] = new_date
                        print("Tasks updated.")
                        
                        with open("tasks.txt", "w") as task_file:
                            for t in task_list:
                                str_attrs = [
                                t['username'],
                                t['title'],
                                t['description'],
                                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                                "Yes" if t['completed'] else "No"]
                            task_file.write(";".join(str_attrs)+ "\n")
                        
                    except ValueError:
                        print("Invalid date format. Please type the date in YYYY-MM-DD format.")
            else:
                print("Invalid task number. Please enter a valid task number.")

       

def display_statistics():
    '''If the user is an admin they can display statistics about number of users
            and tasks.'''
    if curr_user == 'admin':
        num_users = len(username_password)
        num_tasks = len(task_list)
        
        with open("user.txt", 'r') as user_file:
            num_users = sum(1 for line in user_file if line.strip())  
        
  
        with open("tasks.txt", 'r') as task_file:
            num_tasks = sum(1 for line in task_file if line.strip()) 
            
        stats_info = "-" * 80 + "\n" + f"Number of users: {num_users}\n" + "-" * 80 + "\n" + f"Number of tasks: {num_tasks}" + "\n" + "-" * 80 
        return stats_info
    else:
        return "You do not have permission to view statistics"

def generate_reports():
    ''' Takes values from user.txt and tasks.txt and outputs the statistics into text_overview.txt and user_overview.txt'''
     
    complete_tasks = sum(1 for task in task_list if task['completed'])
    incomplete_tasks = sum(1 for task in task_list if not task['completed'])
    total_tasks = complete_tasks + incomplete_tasks
    incomplete_perc = (incomplete_tasks/total_tasks)*100
    overdue_tasks = sum(1 for task in task_list if not task['completed'] and task['due_date']< datetime.now())
    overdue_perc = (overdue_tasks/total_tasks)*100
    
    with open("text_overview.txt","w") as text_overview_file:
        text_overview_file.write("=" * 80 + "\n" + "Task Overview Report" + "\n" + "=" * 80 + "\n" )
        text_overview_file.write(f"Total number of tasks: {total_tasks}\n" + "\n" )
        text_overview_file.write(f"Completed Tasks: {complete_tasks}\n" + "\n")
        text_overview_file.write(f"Incomplete Tasks: {incomplete_tasks}\n" + "\n")
        text_overview_file.write(f"Percentage of incomplete tasks: {incomplete_perc}\n" + "\n")
        text_overview_file.write(f"Overdue tasks: {overdue_tasks}\n" + "\n")
        text_overview_file.write(f"Percentage of overdue tasks: {overdue_perc}\n" + "-" * 80 )
        
        
        
        
    user_tasks = {}
    for task in task_list:
        if task['username'] in user_tasks:
            user_tasks[task['username']]['total'] += 1
            if task['completed']:
                user_tasks[task['username']]['completed']+=1
        else:
            user_tasks[task['username']] = {'total': 1, 'completed': 1 if task['completed'] else 0}
    
    with open("user_overview.txt", "w") as user_file:
        user_file.write("=" * 80 + "\n" + "User Overview Report\n" + "=" * 80 + "\n" + "\n" + "\n")
        for username,i in user_tasks.items():
            num_user_tasks = i['total']
            user_perc = (num_user_tasks/ total_tasks)
            user_complete = i['completed']
            user_perc_complete = (user_complete / num_user_tasks ) *100
            user_perc_incomplete = 100 - user_perc_complete
            user_file.write(f"Username: {username}\n" + "-" * 80 + "\n" )
            user_file.write(f"Number of tasks: {num_user_tasks}\n" + "\n")
            user_file.write(f"Percentage of total tasks: {user_perc}\n" + "\n")  
            user_file.write(f"Percentage of complete tasks: {user_perc_complete}\n" + "\n")
            user_file.write(f"Percentage of incomplete tasks: {user_perc_incomplete}\n" + "\n")
            user_file.write("-" * 80 + "\n")
            
            
            
    return "Report generated"
        

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}
    
    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False
    
    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:
    
    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        print(reg_user())
        
    elif menu == 'a':
        print(add_task())
        
    elif menu == 'va':
        tasks = view_all()
        for tasks_disp in tasks:
            print(tasks_disp)
                
    elif menu == 'vm':
        tasks = view_mine()
        for tasks_disp in tasks:
            print(tasks_disp)
            
    elif menu == 'ds':
        print("-" * 80 + "\n" + "Task Manager Statistics: " + "\n")
        print(display_statistics())
    
    elif menu == 'gr':
        print(generate_reports())
        
    elif menu == 'e':
        print('Goodbye!!!')
        sys.exit()
        
    else:
        print("You have made a wrong choice, Please Try again")
