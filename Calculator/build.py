import os
os.environ["QT_API"] = "pyqt6"
from qtpy import uic

uic.compileUiDir("ui")