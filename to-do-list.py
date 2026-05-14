to_do = []

while True:

    print('1-add task\n2-remove task\n3-show tasks\n4-quit list')

    choice = int(input('Enter your choice '))

    if choice ==1:
        task = input('Enter a task ')
        to_do.append(task)
    elif choice ==2:
        task = input("what task do you want to delete ")
        if task in to_do:
            to_do.remove(task)
            print("Successfully deleted task")
        else:
            print("task does not exist")
    elif choice==3:
        for task in to_do:
         print('.'+task)
    elif choice ==4:
         break
   