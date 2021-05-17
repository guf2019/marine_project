from tkinter import *
# from window_funcs import *

def start_state():
    MAIN_WINDOW_SETTINGS.LABEL_START.place(x=MAIN_WINDOW_SETTINGS.LABEL_START_X, y=MAIN_WINDOW_SETTINGS.LABEL_START_Y)
    MAIN_WINDOW_SETTINGS.BUTTON_START1.place(x=MAIN_WINDOW_SETTINGS.BUTTON_START1_X,
                                             y=MAIN_WINDOW_SETTINGS.BUTTON_START1_Y)
    MAIN_WINDOW_SETTINGS.BUTTON_START2.place(x=MAIN_WINDOW_SETTINGS.BUTTON_START2_X,
                                             y=MAIN_WINDOW_SETTINGS.BUTTON_START2_Y)

def func_student():
    MAIN_WINDOW_SETTINGS.LABEL_START.place_forget()
    MAIN_WINDOW_SETTINGS.BUTTON_START1.place_forget()
    MAIN_WINDOW_SETTINGS.BUTTON_START2.place_forget()

def func_teacher():
    MAIN_WINDOW_SETTINGS.LABEL_START.place_forget()
    MAIN_WINDOW_SETTINGS.BUTTON_START1.place_forget()
    MAIN_WINDOW_SETTINGS.BUTTON_START2.place_forget()
    state_teacher_password()

def state_teacher_password():
    MAIN_WINDOW_SETTINGS.INPUT_TEACHER_PASSWORD.place(x=MAIN_WINDOW_SETTINGS.INPUT_TEACHER_PASSWORD_X, y=MAIN_WINDOW_SETTINGS.INPUT_TEACHER_PASSWORD_Y)
    MAIN_WINDOW_SETTINGS.TEACHER_PASSWORD_BUTTON.place(x=MAIN_WINDOW_SETTINGS.TEACHER_PASSWORD_BUTTON_X, y=MAIN_WINDOW_SETTINGS.TEACHER_PASSWORD_BUTTON_Y)

def auth_teacher():
    if MAIN_WINDOW_SETTINGS.PASSWORD == MAIN_WINDOW_SETTINGS.INPUT_TEACHER_PASSWORD.get():
        MAIN_WINDOW_SETTINGS.INPUT_TEACHER_PASSWORD.place_forget()
        MAIN_WINDOW_SETTINGS.TEACHER_PASSWORD_BUTTON.place_forget()
    else:
        MAIN_WINDOW_SETTINGS.INPUT_TEACHER_PASSWORD.delete(0, END)


class MAIN_WINDOW_SETTINGS:
    MAIN_WINDOW = Tk()
    DEFAULT_HEIGHT = str(MAIN_WINDOW.winfo_screenheight())
    DEFAULT_WIDTH = str(MAIN_WINDOW.winfo_screenwidth())
    HEIGHT = '800'
    WIDTH = '1000'
    TITLE = 'Приложение для проведения тестирования'

    ##### СТАРТОВОЕ СОСТОЯНИЕ ########
    LABEL_START = Label(MAIN_WINDOW, text='Выберите кто вы')
    LABEL_START_X = int(DEFAULT_WIDTH) // 2
    LABEL_START_Y = 0


    BUTTON_START1 = Button(MAIN_WINDOW, text='Ученик', command=func_student)
    BUTTON_START1_X = int(DEFAULT_WIDTH) // 6 * 2
    BUTTON_START1_Y = int(DEFAULT_HEIGHT) // 2


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





