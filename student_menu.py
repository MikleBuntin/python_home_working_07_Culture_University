import member_list
import stunent_commands

def hello(fio):
    # member_list.get_name(member_list.get_id(fio))
    print("Привет, ", member_list.get_name(member_list.get_id(fio)))


def menu(id):
    command = 0
    while command != "q" or command != "q":
        print("Menu: \n 1 - просмотреть расписание \n 2 -  \n 3 -  \n"
              " 4 -  \n 5 -  \n Q - выход")
        command = input("Введите номер команды: ")
        if command == '1':
            stunent_commands.get_time_table(id)
        # elif command == '2':
        #     stunent_commands.
        # elif command == '3':
        #     stunent_commands.