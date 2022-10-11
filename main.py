#Менеджер задач. Исходный код на Python
HELP="""Менеджер задач от Степанова В.Н. Используйте комманды:
add - добавить задачу
show - показать список активных задач
help - вывод этой информации
"""
tasks=[] #список задач
while True:
  command=input("Введите команду: ")
  if command=="add":
    tasks.append(input("Введите задачу: "))
    print("    Задача добавлена")
  elif command=="show":
    print(tasks)
  elif command=="help":
    print(HELP)
  elif command=="exit": 
    print("До свидания !")
    break
