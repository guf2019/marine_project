from tkinter import *
# from window_funcs import *
from database.Mongodriver import MongoDriver


def start_state():
    MAIN_WINDOW_SETTINGS.RETURN_BUTTON.place_forget()
    MAIN_WINDOW_SETTINGS.LABEL_START.place(x=MAIN_WINDOW_SETTINGS.LABEL_START_X, y=MAIN_WINDOW_SETTINGS.LABEL_START_Y)
    MAIN_WINDOW_SETTINGS.BUTTON_START1.place(x=MAIN_WINDOW_SETTINGS.BUTTON_START1_X,
                                             y=MAIN_WINDOW_SETTINGS.BUTTON_START1_Y)
    MAIN_WINDOW_SETTINGS.BUTTON_START2.place(x=MAIN_WINDOW_SETTINGS.BUTTON_START2_X,
                                             y=MAIN_WINDOW_SETTINGS.BUTTON_START2_Y)
    MAIN_WINDOW_SETTINGS.LAST_STATE = start_state


def func_student():
    MAIN_WINDOW_SETTINGS.LABEL_START.place_forget()
    MAIN_WINDOW_SETTINGS.BUTTON_START1.place_forget()
    MAIN_WINDOW_SETTINGS.BUTTON_START2.place_forget()
    state_input_student_name()


def state_input_student_name():
    MAIN_WINDOW_SETTINGS.RETURN_BUTTON.place_forget()
    MAIN_WINDOW_SETTINGS.LABEL_INPUT_NAME.place(x=MAIN_WINDOW_SETTINGS.LABEL_INPUT_NAME_X-150, y=MAIN_WINDOW_SETTINGS.LABEL_INPUT_NAME_Y+300)
    MAIN_WINDOW_SETTINGS.INPUT_NAME.place(x=MAIN_WINDOW_SETTINGS.BUTTON_INPUT_NAME_X, y=MAIN_WINDOW_SETTINGS.BUTTON_INPUT_NAME_X)
    MAIN_WINDOW_SETTINGS.BUTTON_INPUT_NAME.place(x=MAIN_WINDOW_SETTINGS.BUTTON_INPUT_NAME_X, y=MAIN_WINDOW_SETTINGS.BUTTON_INPUT_NAME_Y)


def send_message():
    text = MAIN_WINDOW_SETTINGS.INPUT_NAME.get()
    _id = get_id()
    MAIN_WINDOW_SETTINGS.db_users.push({'id': _id, 'name': text, 'score': 0, })


def get_id():
    try:
        return MAIN_WINDOW_SETTINGS.db_users.get_last_item() + 1
    except:
        return 0


def func_teacher():
    MAIN_WINDOW_SETTINGS.LABEL_START.place_forget()
    MAIN_WINDOW_SETTINGS.BUTTON_START1.place_forget()
    MAIN_WINDOW_SETTINGS.BUTTON_START2.place_forget()
    state_teacher_password()


def state_teacher_password():
    MAIN_WINDOW_SETTINGS.RETURN_BUTTON.place_forget()
    MAIN_WINDOW_SETTINGS.INPUT_TEACHER_PASSWORD.place(x=MAIN_WINDOW_SETTINGS.INPUT_TEACHER_PASSWORD_X, y=MAIN_WINDOW_SETTINGS.INPUT_TEACHER_PASSWORD_Y)
    MAIN_WINDOW_SETTINGS.TEACHER_PASSWORD_BUTTON.place(x=MAIN_WINDOW_SETTINGS.TEACHER_PASSWORD_BUTTON_X, y=MAIN_WINDOW_SETTINGS.TEACHER_PASSWORD_BUTTON_Y)
    MAIN_WINDOW_SETTINGS.LAST_STATE = start_state


def auth_teacher():
    MAIN_WINDOW_SETTINGS.RETURN_BUTTON.place_forget()
    if MAIN_WINDOW_SETTINGS.PASSWORD == MAIN_WINDOW_SETTINGS.INPUT_TEACHER_PASSWORD.get():
        MAIN_WINDOW_SETTINGS.INPUT_TEACHER_PASSWORD.place_forget()
        MAIN_WINDOW_SETTINGS.TEACHER_PASSWORD_BUTTON.place_forget()
        MAIN_WINDOW_SETTINGS.LAST_STATE = auth_teacher
        MAIN_WINDOW_SETTINGS.INPUT_TEACHER_PASSWORD.delete(0, END)
        add_test()
    else:
        MAIN_WINDOW_SETTINGS.INPUT_TEACHER_PASSWORD.delete(0, END)


def add_test():

    MAIN_WINDOW_SETTINGS.RETURN_BUTTON.place(x=MAIN_WINDOW_SETTINGS.RETURN_BUTTON_X, y=MAIN_WINDOW_SETTINGS.RETURN_BUTTON_Y)


class MAIN_WINDOW_SETTINGS:
    MAIN_WINDOW = Tk()
    DEFAULT_HEIGHT = str(MAIN_WINDOW.winfo_screenheight())
    DEFAULT_WIDTH = str(MAIN_WINDOW.winfo_screenwidth())
    HEIGHT = '800'
    WIDTH = '1000'
    TITLE = 'Приложение для проведения тестирования'
    LAST_STATE = start_state

    ##### СТАРТОВОЕ СОСТОЯНИЕ ########
    LABEL_START = Label(MAIN_WINDOW, text='Выберите кто вы')
    LABEL_START_X = int(DEFAULT_WIDTH) // 2
    LABEL_START_Y = 0


    BUTTON_START1 = Button(MAIN_WINDOW, text='Ученик', command=func_student)
    BUTTON_START1_X = int(DEFAULT_WIDTH) // 6 * 2
    BUTTON_START1_Y = int(DEFAULT_HEIGHT) // 2

    LABEL_INPUT_NAME = Label(MAIN_WINDOW, text='Введите имя и фамилию через запятую:')
    INPUT_NAME = Entry(MAIN_WINDOW)
    BUTTON_INPUT_NAME = Button(MAIN_WINDOW, text='Oтправить', command=send_message)
    BUTTON_INPUT_NAME_X = int(DEFAULT_WIDTH) // 6 * 2
    BUTTON_INPUT_NAME_Y = int(DEFAULT_HEIGHT) // 2
    LABEL_INPUT_NAME_X = int(DEFAULT_WIDTH) // 2
    LABEL_INPUT_NAME_Y = 0

    BUTTON_START2 = Button(MAIN_WINDOW, text='Учитель', command=func_teacher)
    BUTTON_START2_X = int(DEFAULT_WIDTH) // 6 * 4
    BUTTON_START2_Y = int(DEFAULT_HEIGHT) // 2

    ##### СОСТОЯНИЕ УЧИТЕЛЯ PASSWORD########
    INPUT_TEACHER_PASSWORD = Entry(MAIN_WINDOW)
    INPUT_TEACHER_PASSWORD_X = int(DEFAULT_WIDTH) // 2
    INPUT_TEACHER_PASSWORD_Y = 0

    PASSWORD = '123'

    TEACHER_PASSWORD_BUTTON = Button(MAIN_WINDOW, text='Войти', command=auth_teacher)
    TEACHER_PASSWORD_BUTTON_X = int(DEFAULT_WIDTH) // 2
    TEACHER_PASSWORD_BUTTON_Y = int(DEFAULT_HEIGHT) // 2

    ########### СОСТОЯНИЕ ДОБАВИТЬ ТЕСТ - ВЕРНУТЬСЯ #####

    RETURN_BUTTON = Button(MAIN_WINDOW, text='Вернуться', command=LAST_STATE)
    RETURN_BUTTON_X = 0
    RETURN_BUTTON_Y = int(DEFAULT_HEIGHT) // 2


    db_users = MongoDriver('app_testing', 'users')






