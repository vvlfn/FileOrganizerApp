from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QFileDialog

class vFolderDialog(QWidget):
    def __init__(self, acceptAction) -> None:
        super().__init__()
        
        self.fileDialog: QFileDialog = QFileDialog(self)
        self.fileDialog.setFileMode(QFileDialog.FileMode.Directory)
        self.fileDialog.setOption(QFileDialog.Option.ShowDirsOnly, True)
        
        if self.fileDialog.exec():
            selected_folder = self.fileDialog.selectedFiles()[0]
            acceptAction(selected_folder)