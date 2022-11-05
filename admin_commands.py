def get_new_id():
    with open('member_list.csv', 'r') as m_list:
        max_id = 0
        for line in m_list:
            if line != '':
                member_id = int(line[line.find('$ID:') + 4: line.find('$F:')])
                if member_id > max_id:
                    max_id = member_id
    return max_id + 1

def add():
    new_id = get_new_id()
    family = input("Введите фамилию: ")
    name = input("Введите имя: ")
    surname = input("Введите отчество: ")
    status = input("Введите статус (0 - студент, 1 - преподаватель: ")
    if status == 0:
        comment = input("Введите группу: ")
    elif status == 1:
        comment = input("Введите дисциплины через запятую: ")
    else:
        comment = input("Введите комментарий: ")
    new_member = str('$ID:{}$F:{}$N:{}$S:{}$st:{}$com:{} \n'.format(new_id, family, name, surname, status, comment))

    with open('member_list.csv', 'a', encoding="cp1251") as m_list:
        m_list.write(new_member)

    print("Готово!")

    # with open('member_list.csv', 'a', encoding="cp1251") as m_list:
    #     for line in m_list:
    #         member_id = line[line.find('$ID:') + 4: line.find('$F:')]
    #         if member_id == new_id:
    #             family = line[line.find('$F:') + 3: line.find('$N:')]
    #             name = line[line.find('$N:') + 3: line.find('$S:')]
    #             surname = line[line.find('$S:') + 3: line.find('$st:')]
    #             print("Студент {} {} {} в группу {} добавлен.".format(family, name, surname, comment))

def view(fio): # атрибуты all, fio
    if fio == 'all':
        with open('member_list.csv', 'r', encoding="cp1251") as members:
            for line in members:
                family = line[line.find('$F:') + 3: line.find('$N:')]
                name = line[line.find('$N:') + 3: line.find('$S:')]
                surname = line[line.find('$S:') + 3: line.find('$st:')]
                status = int(line[line.find('$st:') + 4: line.find('$com:')])
                comm = None
                if status == 0:
                    status = 'Студент'
                    comm = 'группа: '
                elif status == 1:
                    status = 'Преподаватель'
                    comm = 'дисциплины: '

                comment = line[line.find('$com:') + 5:]
                print("{}: {} {} {}; {}{}".format(status, family, name, surname, comm, comment))
    else:
        with open('member_list.csv', 'r', encoding="cp1251") as m_list:
            for line in m_list:
                family = line[line.find('$F:') + 3: line.find('$N:')]
                if fio == family:
                    name = line[line.find('$N:') + 3: line.find('$S:')]
                    surname = line[line.find('$S:') + 3: line.find('$st:')]
                    status = int(line[line.find('$st:') + 4: line.find('$com:')])
                    if status == 0:
                        status = 'Студент'
                        comm = 'группа: '
                    elif status == 1:
                        status = 'Преподаватель'
                        comm = 'дисциплины: '

                    comment = line[line.find('$com:') + 5:]
                    print("{}: {} {} {}; {}{}".format(status, family, name, surname, comm, comment))