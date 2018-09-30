import controller

print("Task Manager Application")

while True:
    print("""
    1. Add Task
    2. Read Task
    3. Delete Task
    4. Update Task
    5. Search Task
    6. Sort Task
    """)

    userCh = input("Enter your choice : ")

    operations = {
        "1" : controller.addTask,
        "2" : controller.readTask
    }

    if userCh == "1":
        taskName = input("Enter task name : ")
        taskDesc = input("Enter task desc : ")
        operations.get(userCh)(taskName, taskDesc)