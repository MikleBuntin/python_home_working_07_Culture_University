

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
    group = input("Введите группу: ")
    new_member = str('$ID:{}$F:{}$N:{}$S:{}$st:0$gr:{}'.format(max_id + 1, family, name, surname, group))

    with open('member_list.csv', 'a') as m_list:
        # m_list.write(new_member)

        for line in m_list:
            member_id = line[line.find('$ID:') + 4: line.find('$ID:') + 6]
            if member_id == max_id + 1:
                family = line[line.find('$F:') + 3: line.find('$N:')]
                name = line[line.find('$N:') + 3: line.find('$S:')]
                surname = line[line.find('$S:') + 3: line.find('$st:')]
                print("Студент {} {} {} в группу {} добавлен.".format(family, name, surname, group))


def status(name):
    with open('member_list.csv', 'r') as m_list:
        for line in m_list:
            if line.rfind('$F:') > 0:
                family = line[line.find('$F:') + 3: line.find('$N:')]
                name = line[line.find('$N:') + 3: line.find('$S:')]
                surname = line[line.find('$S:') + 3: line.find('$st:')]
                f_i_o = family + name[:1] + '.' + surname[:1] + '.'
                if f_i_o == name:
                    return line[line.find('$st:') + 4: line.find('$gr:')]






                # member_id = line[line.find('$ID:') + 4: line.find('$ID:') + 6]
                # family = line[line.find('$F:') + 3: line.find('$N:')]
                # name = line[line.find('$N:') + 3: line.find('$S:')]
                # surname = line[line.find('$S:') + 3: line.find('$st:')]
                # status = line[line.find('$st:') + 4: line.find('$gr:')] # 0 - student; 1 - teacher
                # group = line[line.find('$gr:') + 4: line.find('$gr:')]




