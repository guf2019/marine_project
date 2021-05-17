from tkinter import *
from tkinter.ttk import Combobox
# from window_funcs import *
from database.Mongodriver import MongoDriver


def _expand_(data):
    for widget in data:
        widget[0].place(x=widget[1], y=widget[2])


def clearFrame():
    for widget in MAIN_WINDOW_SETTINGS.MAIN_WINDOW.winfo_children():
       widget.place_forget()


def start_state():
    clearFrame()
    _expand_(MAIN_WINDOW_SETTINGS.START_STATE)

def state_rating():
    clearFrame()

def func_student():
    clearFrame()
    state_input_student_name()


def state_input_student_name():
    _expand_(MAIN_WINDOW_SETTINGS.INPUT_STATE)


def state_random_test():
    clearFrame()
    _expand_(MAIN_WINDOW_SETTINGS.TEST_STATE)


def send_message():
    text = MAIN_WINDOW_SETTINGS.INPUT_NAME[0].get()
    _id = get_id()
    MAIN_WINDOW_SETTINGS.db_users.push({'id': _id, 'name': text, 'score': 0})
    state_random_test()


def get_id():
    try:
        id = MAIN_WINDOW_SETTINGS.db_users.get_last_item()['id'] + 1
        return id
    except Exception as e:
        return 0

def get_id_question():
    try:
        return MAIN_WINDOW_SETTINGS.db_questions.get_last_item() + 1
    except:
        return 0




def state_teacher_password():
    clearFrame()
    _expand_(MAIN_WINDOW_SETTINGS.TEACHER_PASSWORD_STATE)


def auth_teacher():
    if MAIN_WINDOW_SETTINGS.PASSWORD == MAIN_WINDOW_SETTINGS.INPUT_TEACHER_PASSWORD[0].get():
        MAIN_WINDOW_SETTINGS.INPUT_TEACHER_PASSWORD[0].delete(0, END)
        add_test()
    else:
        MAIN_WINDOW_SETTINGS.INPUT_TEACHER_PASSWORD[0].delete(0, END)


def add_test():
    clearFrame()
    _expand_(MAIN_WINDOW_SETTINGS.ADD_QUEST0_STATE)


def add_quest1():
    clearFrame()
    _expand_(MAIN_WINDOW_SETTINGS.ADD_QUEST1_STATE)

def add_quest2():
    clearFrame()
    _expand_(MAIN_WINDOW_SETTINGS.ADD_QUEST2_STATE)


def add_4quest():
    if (MAIN_WINDOW_SETTINGS.INPUT_QUEST[0].get() == '' or MAIN_WINDOW_SETTINGS.INPUT_ANS1[0].get() == '' or MAIN_WINDOW_SETTINGS.INPUT_ANS2[0].get() == ''
        or MAIN_WINDOW_SETTINGS.INPUT_ANS3[0].get() == '' or MAIN_WINDOW_SETTINGS.INPUT_ANS4[0].get() == ''):
        MAIN_WINDOW_SETTINGS.INPUT_QUEST[0].delete(0, END)
        MAIN_WINDOW_SETTINGS.INPUT_ANS1[0].delete(0, END)
        MAIN_WINDOW_SETTINGS.INPUT_ANS2[0].delete(0, END)
        MAIN_WINDOW_SETTINGS.INPUT_ANS3[0].delete(0, END)
        MAIN_WINDOW_SETTINGS.INPUT_ANS4[0].delete(0, END)
    else:
        quest = {}
        quest['id'] = get_id_question()
        quest['level'] = 1
        quest['question'] = MAIN_WINDOW_SETTINGS.INPUT_QUEST[0].get()
        quest['answer'] = [MAIN_WINDOW_SETTINGS.INPUT_ANS1[0].get(), MAIN_WINDOW_SETTINGS.INPUT_ANS2[0].get(),
                           MAIN_WINDOW_SETTINGS.INPUT_ANS3[0].get(), MAIN_WINDOW_SETTINGS.INPUT_ANS4[0].get()]
        quest['correct'] = MAIN_WINDOW_SETTINGS.INPUT_CUR_ANS1[0].get()
        MAIN_WINDOW_SETTINGS.db_questions.push(quest)
        MAIN_WINDOW_SETTINGS.INPUT_QUEST[0].delete(0, END)
        MAIN_WINDOW_SETTINGS.INPUT_ANS1[0].delete(0, END)
        MAIN_WINDOW_SETTINGS.INPUT_ANS2[0].delete(0, END)
        MAIN_WINDOW_SETTINGS.INPUT_ANS3[0].delete(0, END)
        MAIN_WINDOW_SETTINGS.INPUT_ANS4[0].delete(0, END)
        add_test()








def add_textquest():
    if (MAIN_WINDOW_SETTINGS.INPUT_QUEST0[0].get() == '' or MAIN_WINDOW_SETTINGS.INPUT_CUR_ANS2[0].get() == ''):
        MAIN_WINDOW_SETTINGS.INPUT_QUEST0[0].delete(0, END)
        MAIN_WINDOW_SETTINGS.INPUT_CUR_ANS2[0].delete(0, END)
    else:
        quest = {}
        quest['id'] = get_id_question()
        quest['level'] = 2
        quest['question'] = MAIN_WINDOW_SETTINGS.INPUT_QUEST0[0].get()
        quest['correct'] = MAIN_WINDOW_SETTINGS.INPUT_CUR_ANS2[0].get()
        MAIN_WINDOW_SETTINGS.db_questions.push(quest)
        MAIN_WINDOW_SETTINGS.INPUT_QUEST0[0].delete(0, END)
        MAIN_WINDOW_SETTINGS.INPUT_CUR_ANS2[0].delete(0, END)
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
    BUTTON_START2 = [Button(MAIN_WINDOW, text='Учитель', command=state_teacher_password), int(DEFAULT_WIDTH) // 6 * 4, int(DEFAULT_HEIGHT) // 2]
    BUTTON_RATING = [Button(MAIN_WINDOW, text='Рейтинг', command=state_rating), int(DEFAULT_WIDTH) // 2,
                     int(DEFAULT_HEIGHT) // 3 * 2]
    START_STATE = [LABEL_START, BUTTON_START1, BUTTON_START2, BUTTON_RATING]

    ##### СОСТОЯНИЕ ВВОДА ИМЕНИ #####
    LABEL_INPUT_NAME = [Label(MAIN_WINDOW, text='Введите имя и фамилию через запятую:'), 0, 0]
    INPUT_NAME = [Entry(MAIN_WINDOW), 0, +30]
    BUTTON_INPUT_NAME = [Button(MAIN_WINDOW, text='Oтправить', command=send_message), 0, +70]
    INPUT_STATE = [LABEL_INPUT_NAME, INPUT_NAME, BUTTON_INPUT_NAME]

    #### СОСТОЯНИЕ СЛУЧАЙНОГО ТЕСТА #####
    LABEL_RANDOM_TEST = [Label(MAIN_WINDOW, text='Выберите 1 ответ на вопрос:'), 0, 0]
    BUTTON_INPUT_TEST_1 = [Button(MAIN_WINDOW, text='1', command=send_message), 70, +70]
    BUTTON_INPUT_TEST_2 = [Button(MAIN_WINDOW, text='2', command=send_message), 0, +140]
    BUTTON_INPUT_TEST_3 = [Button(MAIN_WINDOW, text='3', command=send_message), 0, +70]
    BUTTON_INPUT_TEST_4 = [Button(MAIN_WINDOW, text='4', command=send_message), +70, +140]
    TEST_STATE = [LABEL_RANDOM_TEST, BUTTON_INPUT_TEST_1, BUTTON_INPUT_TEST_2, BUTTON_INPUT_TEST_3, BUTTON_INPUT_TEST_4]
    ##### СОСТОЯНИЕ УЧИТЕЛЯ PASSWORD########
    INPUT_TEACHER_PASSWORD = [Entry(MAIN_WINDOW), int(DEFAULT_WIDTH) // 2, 0]
    PASSWORD = '123'
    TEACHER_PASSWORD_BUTTON = [Button(MAIN_WINDOW, text='Войти', command=auth_teacher), int(DEFAULT_WIDTH) // 2, int(DEFAULT_HEIGHT) // 2]
    RETURN_TEACHER = [Button(MAIN_WINDOW, text='Вернуться', command=start_state),
                     int(DEFAULT_WIDTH) // 10 * 9, int(DEFAULT_HEIGHT) // 10 * 9]
    TEACHER_PASSWORD_STATE = [INPUT_TEACHER_PASSWORD, TEACHER_PASSWORD_BUTTON, RETURN_TEACHER]

    ########### СОСТОЯНИЕ ДОБАВИТЬ ТЕСТ - ВЕРНУТЬСЯ #####

    # RETURN_BUTTON = Button(MAIN_WINDOW, text='Вернуться', command=LAST_STATE)
    # RETURN_BUTTON_X = int(DEFAULT_WIDTH) // 10 * 9
    # RETURN_BUTTON_Y = int(DEFAULT_HEIGHT) // 10 * 9

    BUTTON_ADD_QUEST1 = [Button(MAIN_WINDOW, text='Добавить вопрос на 4 варианта ответа', command=add_quest1), int(DEFAULT_WIDTH) // 6 * 2, int(DEFAULT_HEIGHT) // 2]
    BUTTON_ADD_QUEST2 = [Button(MAIN_WINDOW, text='Добавить вопрос на текстовый ответ', command=add_quest2), int(DEFAULT_WIDTH) // 6 * 4, int(DEFAULT_HEIGHT) // 2]
    RETURN_QUEST0 = [Button(MAIN_WINDOW, text='Вернуться', command=state_teacher_password),
                     int(DEFAULT_WIDTH) // 10 * 9, int(DEFAULT_HEIGHT) // 10 * 9]
    ADD_QUEST0_STATE = [BUTTON_ADD_QUEST1, BUTTON_ADD_QUEST2, RETURN_QUEST0]

    ############# ДОБАВЛЕНИЕ ВОПРОСА НА 4 ВАРИАНТА ОТВЕТА ##############
    LABEL_QUEST = [Label(MAIN_WINDOW, text='Введите вопрос и 4 варианта ответа:'), int(DEFAULT_WIDTH) // 2, 0]
    INPUT_QUEST = [Entry(MAIN_WINDOW), int(DEFAULT_WIDTH) // 2, int(DEFAULT_HEIGHT) // 20 * 2]
    INPUT_ANS1 = [Entry(MAIN_WINDOW), int(DEFAULT_WIDTH) // 2, int(DEFAULT_HEIGHT) // 20 * 4]
    INPUT_ANS2 = [Entry(MAIN_WINDOW), int(DEFAULT_WIDTH) // 2, int(DEFAULT_HEIGHT) // 20 * 6]
    INPUT_ANS3 = [Entry(MAIN_WINDOW), int(DEFAULT_WIDTH) // 2, int(DEFAULT_HEIGHT) // 20 * 8]
    INPUT_ANS4 = [Entry(MAIN_WINDOW), int(DEFAULT_WIDTH) // 2, int(DEFAULT_HEIGHT) // 20 * 10]
    INPUT_CUR_ANS1 = [Combobox(MAIN_WINDOW) , int(DEFAULT_WIDTH) // 2, int(DEFAULT_HEIGHT) // 20 * 12]
    INPUT_CUR_ANS1[0]['values'] = (1, 2, 3, 4)
    INPUT_CUR_ANS1[0].current(0)
    BUTTON_ADD_4QUEST = [Button(MAIN_WINDOW, text='Добавить вопрос в базу', command=add_4quest), int(DEFAULT_WIDTH) // 2, int(DEFAULT_HEIGHT) // 20 * 14]
    RETURN_QUEST1 = [Button(MAIN_WINDOW, text='Вернуться', command=add_test),
                     int(DEFAULT_WIDTH) // 10 * 9, int(DEFAULT_HEIGHT) // 10 * 9]
    ADD_QUEST1_STATE = [LABEL_QUEST, INPUT_QUEST, INPUT_ANS1, INPUT_ANS2, INPUT_ANS3, INPUT_ANS4, INPUT_CUR_ANS1, BUTTON_ADD_4QUEST, RETURN_QUEST1]


    ############# ДОБАВЛЕНИЕ ВОПРОСА НА ТЕКСТОВЫЙ ОТВЕТ ##############
    LABEL_QUEST0 = [Label(MAIN_WINDOW, text='Введите вопрос и правильный текстовый ответ:'), int(DEFAULT_WIDTH) // 2, 0]
    INPUT_QUEST0 = [Entry(MAIN_WINDOW), int(DEFAULT_WIDTH) // 2, int(DEFAULT_HEIGHT) // 20 * 2]
    INPUT_CUR_ANS2 = [Entry(MAIN_WINDOW), int(DEFAULT_WIDTH) // 2, int(DEFAULT_HEIGHT) // 20 * 6]
    BUTTON_ADD_TEXTQUEST = [Button(MAIN_WINDOW, text='Добавить вопрос в базу', command=add_textquest),
                         int(DEFAULT_WIDTH) // 2, int(DEFAULT_HEIGHT) // 20 * 8]
    RETURN_QUEST2 = [Button(MAIN_WINDOW, text='Вернуться', command=add_test),
                         int(DEFAULT_WIDTH) // 10 * 9, int(DEFAULT_HEIGHT) // 10 * 9]
    ADD_QUEST2_STATE = [LABEL_QUEST0, INPUT_QUEST0, INPUT_CUR_ANS2, BUTTON_ADD_TEXTQUEST, RETURN_QUEST2]



    db_users = MongoDriver('app_testing', 'users')
    db_questions = MongoDriver('app_testing', 'questions')






