# Code by Giriraj Gautam

all_tasks=[]

# to add tasks in todo list
def add_task(task):
    all_tasks.append(task)


# to delete tasks from todo list
def delete_task(index):
    if 0 <= index < len(all_tasks):
        return all_tasks.pop(index)
    else:
        return None



# to view tasks in todo list
def view_tasks():   
    return all_tasks  
