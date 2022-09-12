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


### Bauen des Programms mit pyInstaller bzw. auto-py-to-exe
Es gibt Kompatibilitätsprobleme zwischen pyInstaller und vpython.
Diese führen dazu, dass pyInstaller die von vpython benötigten Dateien nicht mit in die .exe Datei packt.
Dadurch ist es unmöglich Programme mit vpython als einzelne .exe Datei bereitzustellen.

Es ist möglich, den Fehler manuell zu beheben, indem der vpython Ordner zum output von pyInstaller hinzugefügt wird und bestimmte Ordner und Dateien kopiert und umbenannt werden.
Diese Lösung führt jedoch zu enormen Performance-Problemen und kann nicht realistisch in Betracht gezogen werden.

Weiter Informationen zu der Problematik können unter folgenden Links gefunden werden:

* https://groups.google.com/g/vpython-users/c/4EFCROxsHE0/m/bgAPn8PbAQAJ
* https://groups.google.com/g/vpython-users/c/Unz6Lx7Xk34/m/rOxQZFQ7BAAJ
