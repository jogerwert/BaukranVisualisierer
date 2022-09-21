# Baukran Visualisierer

## Bauen und Starten der Anwendung

### Anforderungen:
* Python 3.10 oder höher

### Starten der Anwendung aus dem Source Code:

#### Einmalige Vorbereitung:

*Durchführung im Verzeichnis **BaukranVisualisierer***
```commandline
python -m venv venv
.\venv\Scripts\pip install -r .\requirements.txt
```

#### Main ausführen:

*Durchführung im Verzeichnis **src***
```commandline
..\venv\Scripts\python.exe -m baukran_visualisierer.main
```

#### Tests ausführen:

*Durchführung im Verzeichnis **tests***
```commandline
..\venv\Scripts\pytest.exe
```

### Bearbeiten des Source Code mit PyCharm:
Das Verzeichnis **src** muss als **Sources Root** markiert werden.

Das Verzeichnis **tests** muss als **Test Sources Root** markiert werden.


### Bauen des Programms 
#### pynsist 
Link: https://pypi.org/project/pynsist/

Ausführung der Commandline-Befehle vom Verzeichnis **src** aus gesehen

* Installieren von **NSIS**: https://nsis.sourceforge.io/Download
* Installieren von **pynsist** mit 
    ```commandline
    ..\venv\Scripts\pip.exe install pynsist
    ```
* Ausführen von **pyinsist** mit
    ```commandline
    ..\venv\Scripts\pynsist.exe installer.cfg
    ```
  
Behebung von wahrscheinlich auftretenden Fehlern:

* Falls den Projekt weitere Python-Packages hinzugefügt werden, müssen diese mit allen eigenen Abhängigkeiten zu den pypi-wheels in installer.cfg hinzugefügt werden


* Falls wheels für benötigte packages nicht gefunden werden, können diese mit 
    ```commandline
    ..\venv\Scripts\pip.exe wheel <package-name>
    ```
    gebaut werden. Aktuell ist von der install.cfg Datei vorgesehen, dass nach diesen nachträglich gebauten wheels in einem Ordner namens "wheels" im Ordner "BaukranVisualisierer" gesucht wird. Siehe https://pynsist.readthedocs.io/en/latest/faq.html#faq-no-wheels


* Falls tkinter nicht gefunden wird, müssen mehrere Dateien in den Projektordner gelegt werden:
  * Der Ordner "tcl" aus einer Windows-Python-Installation mit der gewünschten Versionsnummer muss in den Order "src" gelegt werden und zu "lib" umbenannt werden.
  * Die Dateien _tkinter.pyd, tcl86t.dll und tk86t.dll aus dem Ordner "DLLs" einer Windows-Python-Installation mit der gewünschten Versionsnummer muss in einen neuen Ordner "pynsist_pkgs" in "src" gelegt werden.
  * Die Datei _tkinter.lib aus dem Ordner "libs" einer Windows-Python-Installation mit der gewünschten Versionsnummer muss in den Ordner "pynsist_pkgs", der im vorigen Schritt erstellt wurde, gelegt werden.
  
  Siehe https://pynsist.readthedocs.io/en/latest/faq.html#packaging-with-tkinter

#### pyInstaller und auto-py-to-exe
Es gibt Kompatibilitätsprobleme zwischen pyInstaller und vpython.
Diese führen dazu, dass pyInstaller die von vpython benötigten Dateien nicht mit in die .exe Datei packt.
Dadurch ist es unmöglich Programme mit vpython als einzelne .exe Datei bereitzustellen.

Es ist möglich, den Fehler manuell zu beheben, indem der vpython Ordner zum output von pyInstaller hinzugefügt wird und bestimmte Ordner und Dateien kopiert und umbenannt werden.
Diese Lösung führt jedoch zu enormen Performance-Problemen und kann nicht realistisch in Betracht gezogen werden.

Weiter Informationen zu der Problematik können unter folgenden Links gefunden werden:

* https://groups.google.com/g/vpython-users/c/4EFCROxsHE0/m/bgAPn8PbAQAJ
* https://groups.google.com/g/vpython-users/c/Unz6Lx7Xk34/m/rOxQZFQ7BAAJ
