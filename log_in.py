import student_menu
import teacher_menu
import member_list
import admin_menu


def log(name):
    if name == '0':
        return "1"
    elif name == "q" or name == 'Q':
        return "0"
    elif name == "admin":
        return admin_menu.menu()
    elif member_list.status(name) == '0':
        student_menu.hello(name)
    elif member_list.status(name) == '1':
        return teacher_menu.menu(teacher_menu.hello(name))

    else:
        print("Имя введено неверно или Вы не зарегистрированы. \n "
              "Введите снова или обратитесь к преподавателю")
        return '1'