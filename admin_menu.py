
import member_list
import admin_commands

def menu():
    print("Привет, admin!")
    command = 0
    while command != "q" or command != "q":
        print("Menu: \n add - добавить пользователя \n view - просмотр карточки пользователя \n ")
        command = input("Введите команду: ")
        if command == "add":
            admin_commands.add()
        elif command == "view":
            admin_commands.view(input("'all' - все, или введите фамилию: "))
