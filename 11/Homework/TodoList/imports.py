import os

class BadPriorityError(Exception):
# Priority have to be between 1 to 100 included
    pass

class BadIdError(Exception):
# Id have to be between 1 to 15 included
    pass

class BadNameError(Exception):
# Name have to be more then 7 symbvols
    pass

def checkID(id):  # Checking ID and if it wrong format raising error.
    if int(id) >= 1 or int(id) <= 15:
        return None
    else:
        raise BadIdError('Id have to be between 1 to 15 included')

def checkName(name):  # Checking Name and if it wrong format raising error.
    if len(name) < 7:
        raise BadNameError('Name have to be more then 7 symbvols')

def checkPriority(prior):  # Checking Priority and if it wrong format raising error.
    if int(prior) >= 1 or int(prior) <= 100:
        return None
    else:
        raise BadPriorityError('Priority have to be between 1 to 100 included')

def Dzen():
    print('''
    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    ''', end ='')

def help():  # Help box
    print('''
    Use 'Add task' to add task.
    Use 'Show task' to show task by id.
    Use 'Change task' to change task by id.
    Use 'Check task' to know about exitstence of task with id.
    Use 'Save' to save data to file.
    Use 'Show all' to view all tasks.
    Use 'Delete all' to delete all task.
    Use 'Dzen' to see a Dzen.
    Use 'exit' to stop program.
    ''', end='')

class Task:

    def __init__(self, name_of_file):
        self.__task_list = {}  # Defining name of dictionary, that we will be using next for containing tasks.
        self.__file_name = name_of_file
        try:
            stream = open(name_of_file, 'r')  # Reading file for collecting data.

            for line in stream.readlines():
                num_task, name_task, priority = line.strip().split('|--|')
                self.__task_list[num_task] = name_task + '|--|' + priority
            stream.close()
        except:  # If we cannot open file we will create one.
             stream = open(name_of_file, 'x')
             stream.close()


    def add(self):
        id = input('ID: ')  # Asking for ID, will be using that in dictionary like a key.
        checkID(id)  # Checking up ID.
        name = input('Name: ')  # Asking name.
        checkName(name)  # Checking up name.
        prior = input('Prior: ')  # Asking priority.
        checkPriority(prior)  # Checkin up priority.

        if id in self.__task_list:  # if ID already in list.
            print('Task with this ID exitsts.')
            name_of_task, prior_of_task = self.__task_list[id].split('|--|')  # Collecting data from dictionary.
            print(id + '|' + name_of_task + '|' + prior_of_task)  # Showing task with ID from user.

            que = input('\nDo you want to replace it?(y/n)')
            if que == 'y':
                print('\n', id + '|' + name + '|' + prior + '\n')  # Printing final task to know all info is right.
                que = input('All info right?(y/n)')
                if que == 'n':
                    Task.add()  # If something wrong recall method.
                elif que == 'y':
                    self.__task_list[id] = name + '|--|' + prior
                
            elif que == 'n': 
                Task.add()  # If answer is NO, recall method.

        else:
            print('\n', id + '|' + name + '|' + prior + '\n')
            que = input('All info right?(y/n)')
            if que == 'n':
                Task.add()  # If something wrong recall method.
            elif que == 'y':
                self.__task_list[id] = name + '|--|' + prior
        
    
    
    def show(self):
        id = input('ID: ') 
        checkID(id) 
        try:  # If ID exits we print task.
            name_of_task, prior_of_task = self.__task_list[id].split('|--|')
            print(id + '|' + name_of_task + '|' + prior_of_task)
        except:  # If not, inform user.
            print('ID not found!')
    

    def change(self):
        id = input('ID: ') 
        checkID(id)
        try:
            name_of_task, prior_of_task = self.__task_list[id].split('|--|')  # Collecting data from dictionary to imform user with curren data of a task.
            print(id + '|' + name_of_task + '|' + prior_of_task, '\n\n')  # Printing old task to be replaced.

            name, prior = input('Input(name|--|prior):').split('|--|')  # Asking data.

            print('\n', id + '|' + name + '|' + prior + '\n')
            que = input('All info right?(y/n)')  # Asking about rightness of info.
            if que == 'n':
                Task.change(id)
            elif que == 'y':
                self.__task_list[id] = name+'|--|'+prior
        except KeyError:
            print('ID not found!')


    def check(self):
        id = input('ID: ')  # Asking and checking ID.
        checkID(id)
        if id in self.__task_list:
            print('ID exists')
        else:
            print('ID not found!')


    def save_file(self):  # This solution disable losing of data in an emergince closing of program.
        os.remove(self.__file_name)  # Deleting file.
        stream = open(self.__file_name, 'x')  # Creating new one and write tasks in it.

        for id in self.__task_list:
            name_of_task, prior_of_task = self.__task_list[id].split('|--|')  # Getting info from dictionary.
            stream.write(id + '|--|' + name_of_task + '|--|' + prior_of_task)  # Writing data at file.
        stream.close()
        print('Data saved!\n\n\n')


    def see_all(self):
        for i in self.__task_list:
            name_of_task, prior_of_task = self.__task_list[i].split('|--|')
            print(i, name_of_task, prior_of_task)

    def deleting_all(self):
        print('Are you sure to delete all?')
        que = input('Input - Yes, I am TOTALLY sure!\nInput: ')
        if que == 'Yes, I am TOTALLY sure!':
            self.__task_list = {}
            os.remove(self.__file_name)
            stream = open(self.__file_name, 'x')
            stream.close()
            print('All deleted!')