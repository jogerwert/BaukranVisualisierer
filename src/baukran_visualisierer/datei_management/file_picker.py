from tkinter import Tk
from tkinter.filedialog import askopenfilename


def file_picker() -> str:
    """
    Oeffnet einen tkinter Dateiauswahldialog und gibt den Dateinamen zurueck.

    :return: Der Dateiname der ausgewaehlten Datei.
    """
    root = Tk()
    root.title('Baukran Visualisierer')
    root.resizable(False, False)
    root.geometry('300x10')

    filetypes = (
        ('Bauablaufbeschreibungen', '*.bas'),
        ('Alle Dateien', '*.*')
    )
    dateiname = askopenfilename(
        title='Bauablaufbeschreibung auswählen',
        filetypes=filetypes
    )

    root.destroy()

    return dateiname
