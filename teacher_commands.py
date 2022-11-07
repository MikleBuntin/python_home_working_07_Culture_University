import member_list
import time_table

def add_student(id):
    new_id = member_list.get_new_id()
    family = input("Введите фамилию: ")
    name = input("Введите имя: ")
    surname = input("Введите отчество: ")
    comment = input("Введите группу: ")
    new_member = str('\n $ID:{}$F:{}$N:{}$S:{}$st:0$com:{}'.format(new_id, family, name, surname, comment))

    with open('member_list.csv', 'a') as m_list:
        m_list.write(new_member)

    print("Студент {} {} {} в группу {} добавлен.".format(family, name, surname, comment))

    # with open('member_list.csv', 'r') as m_list:
    #     for line in m_list:
    #         member_id = line[line.find('$ID:') + 4: line.find('$ID:') + 6]
    #         if member_id == new_id:
    #             family = line[line.find('$F:') + 3: line.find('$N:')]
    #             name = line[line.find('$N:') + 3: line.find('$S:')]
    #             surname = line[line.find('$S:') + 3: line.find('$st:')]
    #             comment = line[line.find('$com:') + 5:]
    #


# def view_student():


def get_time_table(id):
    time_table.view_time_table(id)



def add_class(id):
    if time_table.add_class(id):
        print("занятие добавлено.")
    else:
        return '0'


def add_home_work(id):
    if time_table.add_home_work(id):
        print("занятие добавлено.")
    else:
        return '0'
