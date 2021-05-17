from tkinter import *
# from window_funcs import *
from database.Mongodriver import MongoDriver


def clearFrame():
    for widget in MAIN_WINDOW_SETTINGS.MAIN_WINDOW.winfo_children():
       widget.place_forget()



def start_state():
    for widget in MAIN_WINDOW_SETTINGS.START_STATE:
        widget[0].place(x=widget[1], y=widget[2])



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
    clearFrame()
    state_teacher_password()


def state_teacher_password():
    MAIN_WINDOW_SETTINGS.INPUT_TEACHER_PASSWORD.place(x=MAIN_WINDOW_SETTINGS.INPUT_TEACHER_PASSWORD_X, y=MAIN_WINDOW_SETTINGS.INPUT_TEACHER_PASSWORD_Y)
    MAIN_WINDOW_SETTINGS.TEACHER_PASSWORD_BUTTON.place(x=MAIN_WINDOW_SETTINGS.TEACHER_PASSWORD_BUTTON_X, y=MAIN_WINDOW_SETTINGS.TEACHER_PASSWORD_BUTTON_Y)


def auth_teacher():
    if MAIN_WINDOW_SETTINGS.PASSWORD == MAIN_WINDOW_SETTINGS.INPUT_TEACHER_PASSWORD.get():
        clearFrame()
        MAIN_WINDOW_SETTINGS.INPUT_TEACHER_PASSWORD.delete(0, END)
        add_test()
    else:
        MAIN_WINDOW_SETTINGS.INPUT_TEACHER_PASSWORD.delete(0, END)


def add_test():
    MAIN_WINDOW_SETTINGS.BUTTON_ADD_QUEST1.place(x=MAIN_WINDOW_SETTINGS.BUTTON_ADD_QUEST1_X, y=MAIN_WINDOW_SETTINGS.BUTTON_ADD_QUEST1_Y)
    MAIN_WINDOW_SETTINGS.BUTTON_ADD_QUEST2.place(x=MAIN_WINDOW_SETTINGS.BUTTON_ADD_QUEST2_X,
                                                 y=MAIN_WINDOW_SETTINGS.BUTTON_ADD_QUEST2_Y)


def add_quest1():
    clearFrame()
    MAIN_WINDOW_SETTINGS.LABEL_QUEST.place(x=MAIN_WINDOW_SETTINGS.LABEL_QUEST_X, y=MAIN_WINDOW_SETTINGS.LABEL_QUEST_Y)
    MAIN_WINDOW_SETTINGS.INPUT_QUEST.place(x=MAIN_WINDOW_SETTINGS.INPUT_QUEST_X, y=MAIN_WINDOW_SETTINGS.INPUT_QUEST_Y)

    MAIN_WINDOW_SETTINGS.INPUT_ANS1.place(x=MAIN_WINDOW_SETTINGS.INPUT_ANS1_X, y=MAIN_WINDOW_SETTINGS.INPUT_ANS1_Y)
    MAIN_WINDOW_SETTINGS.INPUT_ANS2.place(x=MAIN_WINDOW_SETTINGS.INPUT_ANS2_X, y=MAIN_WINDOW_SETTINGS.INPUT_ANS2_Y)
    MAIN_WINDOW_SETTINGS.INPUT_ANS3.place(x=MAIN_WINDOW_SETTINGS.INPUT_ANS3_X, y=MAIN_WINDOW_SETTINGS.INPUT_ANS3_Y)
    MAIN_WINDOW_SETTINGS.INPUT_ANS4.place(x=MAIN_WINDOW_SETTINGS.INPUT_ANS4_X, y=MAIN_WINDOW_SETTINGS.INPUT_ANS4_Y)

    MAIN_WINDOW_SETTINGS.BUTTON_ADD_4QUEST.place(x=MAIN_WINDOW_SETTINGS.BUTTON_ADD_4QUEST_X, y=MAIN_WINDOW_SETTINGS.BUTTON_ADD_4QUEST_Y)

def add_quest2():
    clearFrame()


def add_4quest():
    pass

















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


    LABEL_INPUT_NAME = Label(MAIN_WINDOW, text='Введите имя и фамилию через запятую:')
    INPUT_NAME = Entry(MAIN_WINDOW)
    BUTTON_INPUT_NAME = Button(MAIN_WINDOW, text='Oтправить', command=send_message)
    BUTTON_INPUT_NAME_X = int(DEFAULT_WIDTH) // 6 * 2
    BUTTON_INPUT_NAME_Y = int(DEFAULT_HEIGHT) // 2
    LABEL_INPUT_NAME_X = int(DEFAULT_WIDTH) // 2
    LABEL_INPUT_NAME_Y = 0

    ##### СОСТОЯНИЕ УЧИТЕЛЯ PASSWORD########
    INPUT_TEACHER_PASSWORD = Entry(MAIN_WINDOW)
    INPUT_TEACHER_PASSWORD_X = int(DEFAULT_WIDTH) // 2
    INPUT_TEACHER_PASSWORD_Y = 0

    PASSWORD = '123'

    TEACHER_PASSWORD_BUTTON = Button(MAIN_WINDOW, text='Войти', command=auth_teacher)
    TEACHER_PASSWORD_BUTTON_X = int(DEFAULT_WIDTH) // 2
    TEACHER_PASSWORD_BUTTON_Y = int(DEFAULT_HEIGHT) // 2

    ########### СОСТОЯНИЕ ДОБАВИТЬ ТЕСТ - ВЕРНУТЬСЯ #####

    # RETURN_BUTTON = Button(MAIN_WINDOW, text='Вернуться', command=LAST_STATE)
    # RETURN_BUTTON_X = int(DEFAULT_WIDTH) // 10 * 9
    # RETURN_BUTTON_Y = int(DEFAULT_HEIGHT) // 10 * 9

    BUTTON_ADD_QUEST1 = Button(MAIN_WINDOW, text='Добавить вопрос на 4 варианта ответа', command=add_quest1)
    BUTTON_ADD_QUEST1_X = int(DEFAULT_WIDTH) // 6 * 2
    BUTTON_ADD_QUEST1_Y = int(DEFAULT_HEIGHT) // 2

    BUTTON_ADD_QUEST2 = Button(MAIN_WINDOW, text='Добавить вопрос на текстовый ответ', command=add_quest2)
    BUTTON_ADD_QUEST2_X = int(DEFAULT_WIDTH) // 6 * 4
    BUTTON_ADD_QUEST2_Y = int(DEFAULT_HEIGHT) // 2

    ############# ДОБАВЛЕНИЕ ВОПРОСА НА 4 ВАРИАНТА ОТВЕТА ##############
    LABEL_QUEST = Label(MAIN_WINDOW, text='Введите вопрос и 4 варианта ответа:')
    LABEL_QUEST_X = int(DEFAULT_WIDTH) // 2
    LABEL_QUEST_Y = 0

    INPUT_QUEST = Entry(MAIN_WINDOW)
    INPUT_QUEST_X = int(DEFAULT_WIDTH) // 2
    INPUT_QUEST_Y = int(DEFAULT_HEIGHT) // 20 * 3

    INPUT_ANS1 = Entry(MAIN_WINDOW)
    INPUT_ANS1_X = int(DEFAULT_WIDTH) // 2
    INPUT_ANS1_Y = int(DEFAULT_HEIGHT) // 20 * 6

    INPUT_ANS2 = Entry(MAIN_WINDOW)
    INPUT_ANS2_X = int(DEFAULT_WIDTH) // 2
    INPUT_ANS2_Y = int(DEFAULT_HEIGHT) // 20 * 9

    INPUT_ANS3 = Entry(MAIN_WINDOW)
    INPUT_ANS3_X = int(DEFAULT_WIDTH) // 2
    INPUT_ANS3_Y = int(DEFAULT_HEIGHT) // 20 * 12

    INPUT_ANS4 = Entry(MAIN_WINDOW)
    INPUT_ANS4_X = int(DEFAULT_WIDTH) // 2
    INPUT_ANS4_Y = int(DEFAULT_HEIGHT) // 20 * 15

    BUTTON_ADD_4QUEST = Button(MAIN_WINDOW, text='Добавить вопрос в базу', command=add_4quest)
    BUTTON_ADD_4QUEST_X = int(DEFAULT_WIDTH) // 2
    BUTTON_ADD_4QUEST_Y = int(DEFAULT_HEIGHT) // 20 * 18



    ############# ДОБАВЛЕНИЕ ВОПРОСА НА ТЕКСТОВЫЙ ОТВЕТ ##############






    db_users = MongoDriver('app_testing', 'users')






