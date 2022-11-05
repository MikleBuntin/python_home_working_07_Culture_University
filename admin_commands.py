def add():
    with open('member_list.csv', 'r') as m_list:
        max_id = 0
        for line in m_list:
            member_id = int(line[line.find('$ID:') + 4: line.find('$ID:') + 6])
            if member_id > max_id:
                max_id = member_id

    family = input("Введите фамилию: ")
    name = input("Введите имя: ")
    surname = input("Введите отчество: ")
    status = input("Введите статус (0 - студент, 1 - преподаватель: ")
    group = input("Введите группу: ")
    new_member = str('$ID:{}$F:{}$N:{}$S:{}$st:{}$gr:{}'.format(max_id + 1, family, name, surname, status, group))

    with open('member_list.csv', 'a') as m_list:
        # m_list.write(new_member)

        for line in m_list:
            member_id = line[line.find('$ID:') + 4: line.find('$ID:') + 6]
            if member_id == max_id + 1:
                family = line[line.find('$F:') + 3: line.find('$N:')]
                name = line[line.find('$N:') + 3: line.find('$S:')]
                surname = line[line.find('$S:') + 3: line.find('$st:')]
                print("Студент {} {} {} в группу {} добавлен.".format(family, name, surname, group))

