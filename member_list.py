

def add():
    with open('member_list.csv', 'r') as m_list:
        max_id = 0
        for line in m_list:
            member_id = line[line.find('$ID:') + 4: line.find('$ID:') + 6]
            if member_id > max_id:
                max_id = member_id

        max_id + 1


def status(name):
    with open('member_list.csv', 'r') as m_list:
        for line in m_list:
            if line.rfind('$F:') > 0:






                # member_id = line[line.find('$ID:') + 4: line.find('$ID:') + 6]
                # family = line[line.find('$F:') + 3: line.find('$N:')]
                # name = line[line.find('$N:') + 3: line.find('$S:')]
                # surname = line[line.find('$S:') + 3: line.find('$st:')]
                # status = line[line.find('$st:') + 4: line.find('$gr:')] # 0 - student; 1 - teacher
                # group = line[line.find('$gr:') + 4: line.find('$gr:')] # 01...99 берем из groups.csv




