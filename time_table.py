import member_list


def print_day(date):
    today_classes = ['0' for i in range(4)]
    with open('time_table.csv', 'r', encoding="cp1251") as table:
        for line in table:
            if len(line) > 0:

                date_from_table = line[line.find('$Date:') + 6: line.find('$N:')]
                if date_from_table == date:
                    # number_of_class = int(line[line.find('$N:') + 3: line.find('$D:')])
                    number_of_class = int(line[line.find('$N:') + 3])
                    disp = line[line.find('$D:') + 3: line.find('$T:')]
                    teacher = member_list.get_fio(int(line[line.find('$T:') + 3: line.find('$A:')]))
                    auditorium = line[line.find('$A:') + 3: line.find('$G:')]
                    group = line[line.find('$G:') + 3:line.find('$H:')]
                    home_work = line[line.find('$H:') + 3:]
                    today_class = "{}: {}. преподаватель: {}, ауд. {}, группа: {}, ДЗ: {}".format(str(number_of_class), disp, teacher, auditorium, group, home_work)
                    # print(today_class)
                    today_classes[number_of_class - 1] = today_class
        print("Расписание на {}: ".format(date))
        for i in range (len(today_classes)):
            print(today_classes[i])



def add_class(id):
    date = input("Введите дату в формате дд.мм: ")
    print_day(date)
    number_of_class = input("Введите номер пары: ")
    disp = input("Введите наименование дисциплины: ")
    auditorium = input("Введите номер аудитории: ")
    group = input("Введите группу: ")
    home_work = '-'
    new_class = str('$N:{}$D:{}$T:{}$A:{}$G:{}$H:{}'
                    ''.format(number_of_class, disp, id, auditorium, group, home_work))
    record_class(date, new_class)
    return True


def record_class(date, new_class):
    with open('time_table.csv', 'a', encoding="cp1251") as table:
        table.writelines('\n$Date:{}{}'.format(date, new_class))


def view_teacher(id):
    date = input("Введите дату в формате дд.мм: ")
    print_day(date)
#
# def view_table(date):
