import member_list


def print_day(date):
    with open('time_table.csv', 'r', encoding="cp1251") as table:
        for line in table:
            if len(line) > 0:
                date_from_table = line[line.find('$D:') + 3: line.find('$N:')]
                if date_from_table == date:
                    print("Расписание на {}: \n ".format(date))
                    while line != '':
                        number_of_class = line[line.find('$N:') + 3: line.find('$D:')]
                        disp = line[line.find('$D:') + 3: line.find('$T:')]
                        teacher = member_list.get_fio(line[line.find('$T:') + 3: line.find('$A:')])
                        auditorium = line[line.find('$A:') + 3: line.find('$G:')]
                        group = line[line.find('$G:') + 3:line.find('$H:')]
                        home_work = line[line.find('$H:') + 3:]
                        print("{}: {}. преподаватель: {}, ауд. {}, группа: {}, ДЗ: {}. \n"
                              "".format(number_of_class, disp, teacher, auditorium, group, home_work))
                        line = line[3:]
                        line = line[line.find('$N:') - 1:]
                    return '1'

def add_class(id):
    date = input("Введите дату в формате дд.мм: ")
    print_day(date)
    number_of_class = input("Введите номер пары: ")
    disp = input("Введите наименование дисциплины: ")
    # teacher = member_list.get_fio(id)
    auditorium = input("Введите номер аудитории: ")
    group = input("Введите группу: ")
    home_work = '-'
    new_class = str('$N:{}$D:{}$T:{}$A:{}$G:{}$H:{}'
                    ''.format(number_of_class, disp, id, auditorium, group, home_work))
    record_class(date, new_class)


def record_class(date, new_class):
    number_of_class = new_class[new_class.find('$N:') + 3: new_class.find('$D:')]
    new_line = ''
    with open('time_table.csv', 'r', encoding="cp1251") as table:
        for line in table:
            if len(line) > 0:
                date_from_table = line[line.find('$D:') + 3: line.find('$N:')]
                if date_from_table == date:
                    start = line
                    end = line
                    number = line[line.find('$N:') + 3: line.find('$D:')]
                    while number != number_of_class:
                        line = line[3:]
                        line = line[line.find('$N:') + 3:]
                        number = line[line.find('$N:') + 3: line.find('$D:')]
                    start = start[:start.find(line)]
                    end = end[:start.find(line) + len(line)]
                    # new_line = start + new_class + end
                    new_line = start[:start.find(line)] + new_class + end[:start.find(line) + len(line)]

        with open('time_table.csv', 'w', encoding="cp1251") as table:
            for line in table:
                if len(line) > 0:
                    date_from_table = line[line.find('$D:') + 3: line.find('$N:')]
                    if date_from_table == date:





        m_list.write(new_member)

    print("Готово!")


def view_teacher(id):


def view_table(date):
