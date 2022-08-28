from tkinter import Tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo


def file_picker():
    root = Tk()
    root.title('Baukran Visualisierer')
    root.resizable(False, False)
    root.geometry('300x150')

    filetypes = (
        ('Bauablaufbeschreibungen', '*.bas'),
        ('Alle Dateien', '*.*')
    )
    dateiname = askopenfilename(
        title='Bauablaufbeschreibung auswählen',
        filetypes=filetypes
    )
    return dateiname
