import student_menu
input teacher_menu


def log(name):
    if main_list.status(name) == 0:
        student_menu.hello(name)
    elif name in teachers:
        teacher_menu.hello(name)
    else:
        print("Имя введено неверно или Вы не зарегистрированы. \n "
              "Введите снова или обратитесь к преподавателю")