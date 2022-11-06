import member_list
import admin_commands
import time_table


def menu():
    print("Привет, admin!")
    command = 0
    while command != "q" or command != "q":
        print("Menu: \n 1 - добавить пользователя \n 2 - просмотр карточки пользователя \n 3 - просмотр расписания преподавателя")
        command = input("Введите команду: ")
        if command == "1":
            admin_commands.add_member()
        elif command == "2":
            admin_commands.view(input("'all' - все, или введите фамилию: "))
        elif command == "3":
            id = admin_commands.get_id(input('Введите Ф.И.О. в формате "Иванов А.В.": '))
            time_table.view_teacher(id)
