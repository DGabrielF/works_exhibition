from tkinter import Tk

from frontConfigs import FrontConfig


class MainWindow:
    root = Tk()
    root.geometry("960x539+10+10")
    root.geometry(str(FrontConfig.window_width)+'x'+str(FrontConfig.window_height))