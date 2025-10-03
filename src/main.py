from datetime import datetime
import os
import sys
from PyQt6.QtWidgets import QApplication
from components.vRoot import vRoot
import logging

def Main() -> None:    
    app: QApplication = QApplication(sys.argv)
    
    root: vRoot = vRoot()
    root.show()
    
    app.exec()


if __name__ == "__main__":
    Main()