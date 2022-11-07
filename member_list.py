

def status(fio):
    fio = fio.replace(' ', '.')
    fio = fio.split('.')
    with open('member_list.csv', 'r') as m_list:
        for line in m_list:
            if line.rfind('$F:') > 0:
                family = line[line.find('$F:') + 3: line.find('$N:')]
                name = line[line.find('$N:') + 3: line.find('$S:')]
                surname = line[line.find('$S:') + 3: line.find('$st:')]
                # print(family, name, surname)
                if family == fio[0] and name[:1] == fio[1] and surname[:1] == fio[2]:
                    return line[line.find('$st:') + 4: line.find('$com:')]


def get_new_id():
    with open('member_list.csv', 'r') as m_list:
        max_id = 0
        for line in m_list:
            if line != '':
                member_id = int(line[line.find('$ID:') + 4: line.find('$F:')])
                if member_id > max_id:
                    max_id = member_id
    return max_id + 1


def get_id(fio):
    with open('member_list.csv', 'r', encoding="cp1251") as members:
        for line in members:
            family = line[line.find('$F:') + 3: line.find('$N:')]
            name = line[line.find('$N:') + 3: line.find('$S:')]
            surname = line[line.find('$S:') + 3: line.find('$st:')]
            id = line[line.find('$ID:') + 3: line.find('$F:')]
            if fio == family + ' ' + name[:1] + '.' + surname[:1] + '.':
                # print("Здравствуйте, {} {}".format(name, surname))
                return id

def get_fio(id):
    with open('member_list.csv', 'r', encoding="cp1251") as members:
        for line in members:
            if id == int(line[line.find('$ID:') + 4: line.find('$F:')]):
                family = line[line.find('$F:') + 3: line.find('$N:')]
                name = line[line.find('$N:') + 3: line.find('$S:')]
                surname = line[line.find('$S:') + 3: line.find('$st:')]
                print(family + ' ' + name[:1] + '.' + surname[:1] + '.')
                return family + ' ' + name[:1] + '.' + surname[:1] + '.'

def get_name(id):
    with open('member_list.csv', 'r', encoding="cp1251") as members:
        for line in members:
            if id == int(line[line.find('$ID:') + 4: line.find('$F:')]):
                # family = line[line.find('$F:') + 3: line.find('$N:')]
                name = line[line.find('$N:') + 3: line.find('$S:')]
                # surname = line[line.find('$S:') + 3: line.find('$st:')]
                return name