

def hello(fio):
    # Узнать ФИО, ID.

    with open('member_list.csv', 'r', encoding="cp1251") as members:
        for line in members:
            family = line[line.find('$F:') + 3: line.find('$N:')]
            name = line[line.find('$N:') + 3: line.find('$S:')]
            surname = line[line.find('$S:') + 3: line.find('$st:')]
            id = line[line.find('$ID:') + 3: line.find('$F:')]
            if fio == family + name[:1] + '.' + surname[:1] +'.':
                print("Здравствуйте, {} {}".format(name, surname))
                return id



def menu(id):
    command = 0
    while command != "q" or command != "q":
        print("Menu: \n 1 - добавить студента \n 2 - просмотр карточки студента \n 3 - просмотреть Ваше расписание \n"
              "4 - добавить занятие в расписание \n 5 - добавить домашнее задание")
        command = input("Введите номер команды: ")
        if command == '1':
            teacher_commands.add_student()
        elif command == '2':
            teacher_commands.view_student()
        elif command == '3':
            teacher_commands.take_time_table(id)
        elif command == '4':
            teacher_commands.add_class(id)
        elif command == '5':
            teacher_commands.add_home_work()
            admin_commands.view(input("'all' - все, или введите фамилию: "))
