class Task():

    def __init__(self,id,name, desc):
        self.task_id = id
        self.task_name = name
        self.task_desc = desc

    def __str__(self):
        return str(self.task_id) + "," + self.task_name + "," + self.task_desc

taskList = []
# id = 0
def addTask(name, desc):
    id = 1
    task = Task(id,name, desc)
    print(task)
    taskList.append(task)
    return taskList