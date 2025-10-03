from PyQt6.QtWidgets import QMainWindow, QWidget

from components.vFolderControls import vFolderControls #type: ignore


class vRoot(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        folderControls: QWidget = vFolderControls()
        self.setCentralWidget(folderControls)