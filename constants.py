from tkinter import *
# from window_funcs import *

def clearFrame():
    for widget in MAIN_WINDOW_SETTINGS.MAIN_WINDOW.winfo_children():
       widget.place_forget()



def start_state():
    for widget in MAIN_WINDOW_SETTINGS.START_STATE:
        widget[0].place(x=widget[1], y=widget[2])


def func_student():
    clearFrame()

def func_teacher():
    clearFrame()
    state_teacher_password()

def state_teacher_password():
    # MAIN_WINDOW_SETTINGS.INPUT_TEACHER_PASSWORD.place(x=MAIN_WINDOW_SETTINGS.INPUT_TEACHER_PASSWORD_X, y=MAIN_WINDOW_SETTINGS.INPUT_TEACHER_PASSWORD_Y)
    # MAIN_WINDOW_SETTINGS.TEACHER_PASSWORD_BUTTON.place(x=MAIN_WINDOW_SETTINGS.TEACHER_PASSWORD_BUTTON_X, y=MAIN_WINDOW_SETTINGS.TEACHER_PASSWORD_BUTTON_Y)
    for widget in MAIN_WINDOW_SETTINGS.TEACHER_PASSWORD_STATE:
        widget[0].place(x=widget[1], y=widget[2])

def auth_teacher():
    if MAIN_WINDOW_SETTINGS.PASSWORD == MAIN_WINDOW_SETTINGS.INPUT_TEACHER_PASSWORD[0].get():
        MAIN_WINDOW_SETTINGS.INPUT_TEACHER_PASSWORD[0].delete(0, END)
        add_test()
    else:
        MAIN_WINDOW_SETTINGS.INPUT_TEACHER_PASSWORD[0].delete(0, END)

def add_test():
    clearFrame()
    for widget in MAIN_WINDOW_SETTINGS.ADD_QUEST0_STATE:
        widget[0].place(x=widget[1], y=widget[2])


def add_quest1():
    clearFrame()
    for widget in MAIN_WINDOW_SETTINGS.ADD_QUEST1_STATE:
        widget[0].place(x=widget[1], y=widget[2])

def add_quest2():
    clearFrame()
    for widget in MAIN_WINDOW_SETTINGS.ADD_QUEST2_STATE:
        widget[0].place(x=widget[1], y=widget[2])


def add_4quest():
    add_test()

def add_textquest():
    add_test()















class MAIN_WINDOW_SETTINGS:
    MAIN_WINDOW = Tk()
    DEFAULT_HEIGHT = str(MAIN_WINDOW.winfo_screenheight())
    DEFAULT_WIDTH = str(MAIN_WINDOW.winfo_screenwidth())
    HEIGHT = '800'
    WIDTH = '1000'
    TITLE = 'Приложение для проведения тестирования'

    ##### СТАРТОВОЕ СОСТОЯНИЕ ########
    LABEL_START = [Label(MAIN_WINDOW, text='Выберите кто вы'), int(DEFAULT_WIDTH) // 2, 0]
    BUTTON_START1 = [Button(MAIN_WINDOW, text='Ученик', command=func_student), int(DEFAULT_WIDTH) // 6 * 2, int(DEFAULT_HEIGHT) // 2]
    BUTTON_START2 = [Button(MAIN_WINDOW, text='Учитель', command=func_teacher), int(DEFAULT_WIDTH) // 6 * 4, int(DEFAULT_HEIGHT) // 2]
    START_STATE = [LABEL_START, BUTTON_START1, BUTTON_START2]

    ##### СОСТОЯНИЕ УЧИТЕЛЯ PASSWORD########
    INPUT_TEACHER_PASSWORD = [Entry(MAIN_WINDOW), int(DEFAULT_WIDTH) // 2, 0]
    PASSWORD = '123'
    TEACHER_PASSWORD_BUTTON = [Button(MAIN_WINDOW, text='Войти', command=auth_teacher), int(DEFAULT_WIDTH) // 2, int(DEFAULT_HEIGHT) // 2]
    TEACHER_PASSWORD_STATE = [INPUT_TEACHER_PASSWORD, TEACHER_PASSWORD_BUTTON]

    ########### СОСТОЯНИЕ ДОБАВИТЬ ТЕСТ - ВЕРНУТЬСЯ #####

    # RETURN_BUTTON = Button(MAIN_WINDOW, text='Вернуться', command=LAST_STATE)
    # RETURN_BUTTON_X = int(DEFAULT_WIDTH) // 10 * 9
    # RETURN_BUTTON_Y = int(DEFAULT_HEIGHT) // 10 * 9

    BUTTON_ADD_QUEST1 = [Button(MAIN_WINDOW, text='Добавить вопрос на 4 варианта ответа', command=add_quest1), int(DEFAULT_WIDTH) // 6 * 2, int(DEFAULT_HEIGHT) // 2]
    BUTTON_ADD_QUEST2 = [Button(MAIN_WINDOW, text='Добавить вопрос на текстовый ответ', command=add_quest2), int(DEFAULT_WIDTH) // 6 * 4, int(DEFAULT_HEIGHT) // 2]
    ADD_QUEST0_STATE = [BUTTON_ADD_QUEST1, BUTTON_ADD_QUEST2]

    ############# ДОБАВЛЕНИЕ ВОПРОСА НА 4 ВАРИАНТА ОТВЕТА ##############
    LABEL_QUEST = [Label(MAIN_WINDOW, text='Введите вопрос и 4 варианта ответа:'), int(DEFAULT_WIDTH) // 2, 0]
    INPUT_QUEST = [Entry(MAIN_WINDOW), int(DEFAULT_WIDTH) // 2, int(DEFAULT_HEIGHT) // 20 * 3]
    INPUT_ANS1 = [Entry(MAIN_WINDOW), int(DEFAULT_WIDTH) // 2, int(DEFAULT_HEIGHT) // 20 * 6]
    INPUT_ANS2 = [Entry(MAIN_WINDOW), int(DEFAULT_WIDTH) // 2, int(DEFAULT_HEIGHT) // 20 * 9]
    INPUT_ANS3 = [Entry(MAIN_WINDOW), int(DEFAULT_WIDTH) // 2, int(DEFAULT_HEIGHT) // 20 * 12]
    INPUT_ANS4 = [Entry(MAIN_WINDOW), int(DEFAULT_WIDTH) // 2, int(DEFAULT_HEIGHT) // 20 * 15]
    BUTTON_ADD_4QUEST = [Button(MAIN_WINDOW, text='Добавить вопрос в базу', command=add_4quest), int(DEFAULT_WIDTH) // 2, int(DEFAULT_HEIGHT) // 20 * 18]
    ADD_QUEST1_STATE = [LABEL_QUEST, INPUT_QUEST, INPUT_ANS1, INPUT_ANS2, INPUT_ANS3, INPUT_ANS4, BUTTON_ADD_4QUEST]


    ############# ДОБАВЛЕНИЕ ВОПРОСА НА ТЕКСТОВЫЙ ОТВЕТ ##############
    LABEL_QUEST0 = [Label(MAIN_WINDOW, text='Введите вопрос и правильный текстовый ответ:'), int(DEFAULT_WIDTH) // 2, 0]
    INPUT_QUEST0 = [Entry(MAIN_WINDOW), int(DEFAULT_WIDTH) // 2, int(DEFAULT_HEIGHT) // 20 * 3]
    INPUT_ANS0 = [Entry(MAIN_WINDOW), int(DEFAULT_WIDTH) // 2, int(DEFAULT_HEIGHT) // 20 * 6]
    BUTTON_ADD_TEXTQUEST = [Button(MAIN_WINDOW, text='Добавить вопрос в базу', command=add_textquest),
                         int(DEFAULT_WIDTH) // 2, int(DEFAULT_HEIGHT) // 20 * 18]
    ADD_QUEST2_STATE = [LABEL_QUEST0, INPUT_QUEST0, INPUT_ANS0, BUTTON_ADD_TEXTQUEST]










