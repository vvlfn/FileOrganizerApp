from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, QMainWindow

from components.vFolderDialog import vFolderDialog #type: ignore

class vFolderControls(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.url = ""
        
        layout: QHBoxLayout = QHBoxLayout()
        
        self.selectFileButton: QPushButton = self._createPushButton()
        layout.addWidget(self.selectFileButton)
        
        self.selectedPath: QLabel = self._createLabel()
        layout.addWidget(self.selectedPath)
        
        self.setLayout(layout)
        self.show()
    
    
    def _createPushButton(self) -> QPushButton:
        button: QPushButton = QPushButton()
        button.setText("Select a folder")
        button.clicked.connect(self._openFolderDialog)
        return button
    
    def _createLabel(self) -> QLabel:
        label: QLabel = QLabel()
        label.setText("No folder selected" if self.url == "" else self.url)
        return label

    def _updateUrl(self) -> None:
        self.selectedPath.setText("No folder selected" if self.url == "" else self.url)
    
    def _openFolderDialog(self) -> None:
        folderDialog: QWidget = vFolderDialog(self._fileDialogAccept)
        folderDialog.show()
        
    def _fileDialogAccept(self, url) -> None:
        self.url = url
        self._updateUrl()