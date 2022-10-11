#Менеджер задач. Исходный код на Python
HELP = """Менеджер задач от Степанова В.Н. Используйте комманды:
add - добавить задачу
show - показать список активных задач
help - вывод этой информации
"""
tasks = []  #списки задач
today=[]
tomorrow=[]
other=[]
while True:
  command = input("Введите команду: ")
  if command == "add":
    task=input("    Введите задачу: ")
    date=input("    Дата (сегодня, завтра, иное ?: ")
    if date=="сегодня":
      today.append(task)
    elif date=="завтра":
      tomorrow.append(task)
    else:
      other.append(task)
    print("    Задача добавлена")
  elif command == "show":
    print("Сегодня: \n",today)
    print("Завтра: \n",tomorrow)
    print("Иные задачи: \n",other)
  elif command == "help":
    print(HELP)
  elif command == "exit":
    print("До свидания !")
    break
  else:
    print("    Неизвестная команда")
