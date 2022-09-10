import os
import sys

# Notwendig, um den tests zu ermoeglichen das src Verzeichnis zu finden
PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH, "src"
)
sys.path.append(SOURCE_PATH)
