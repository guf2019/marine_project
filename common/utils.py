from constants import *



def main_window_first_settings(window):
    # height = str(window.winfo_screenheight())
    # width = str(window.winfo_screenwidth())
    width = MAIN_WINDOW_SETTINGS.DEFAULT_WIDTH
    height = MAIN_WINDOW_SETTINGS.DEFAULT_HEIGHT
    window.geometry(width + 'x' + height)
    window.title(MAIN_WINDOW_SETTINGS.TITLE)
    window.resizable(width=False, height=False)
    start_state()
    return window