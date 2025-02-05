todo_list = []

while True:
  if len(todo_list) == 0:
    print("Your to do list is empty")
  else:
    index = 1
    for task in todo_list:
      print(f"{index}. {task}")
      index += 1
  print ("Options:")
  print ("1) Add Task")
  print ("2) Remove Task")
  print ("3) Quit")
  choice = input("Please select an option: ")
  if choice == "1":
    new_task = input("What task would you like to add? ")
    todo_list.append(new_task)
    print("Task has been added")
  if choice == "2":
    if len(todo_list) == 0:
      print("To do list is empty")
    if len(todo_list) > 0:
      removal = input("What number task would you like to remove? ")
      todo_list.pop((int(removal)) - 1)
      print ("Removed last task")
  if choice == "3":
    print ("Quitting")
    break
