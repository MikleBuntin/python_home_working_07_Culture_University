
import member_list
import admin_commands

def menu():
    print("Привет, admin!")
    while command != "q" or command != "q":
        print("Menu: \n add - добавить пользователя \n view - просмотр карточки пользователя \n ")
        command = input("Введите команду: ")
        if command == "add":
            admin_commands.add()
        # elif command == "view":


# return "1"
