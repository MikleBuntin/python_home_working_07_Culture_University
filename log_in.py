import student_menu
input teacher_menu
import member_list


def log(name):
    if member_list.status(name) == 0:
        student_menu.hello(name)

    elif name in teachers:
        teacher_menu.hello(name)
    else:
        print("Имя введено неверно или Вы не зарегистрированы. \n "
              "Введите снова или обратитесь к преподавателю")