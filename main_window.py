import csv
import os
import sys

from iterator import SimpleIterator
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QFileDialog, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        """
        Creates a window for displaying images, next image button and a button for selecting an annotation file
        """
        super().__init__()
        self.setWindowTitle("Image Dataset Viewer")
        self.setGeometry(100, 100, 800, 600)
        self.layout = QVBoxLayout()
        self.label = QLabel("Choose annotation file")
        self.label.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.layout.addWidget(self.label)
        self.image_label = QLabel()
        self.image_label.setFixedSize(800, 600)
        self.layout.addWidget(self.image_label)
        self.next_button = QPushButton("Next image")
        self.next_button.clicked.connect(self.show_next_image)
        self.layout.addWidget(self.next_button)
        self.select_button = QPushButton("Choose annotation file")
        self.select_button.clicked.connect(self.select_annotation)
        self.layout.addWidget(self.select_button)
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
        self.iterator = None

    def select_annotation(self):
        """
        Opens a dialog box to open the annotation file
        """
        annotation_file = QFileDialog.getOpenFileName(self, "Choose annotation file")[0]
        if annotation_file:
            self.iterator = SimpleIterator(annotation_file)
            self.label.setText(f"Annotation file: {annotation_file}")
            self.show_next_image()

    def show_next_image(self):
        """
        Shows next image in annotation file
        """
        if self.iterator:
            try:
                image_path = next(self.iterator)
                self.display_image(image_path)
            except StopIteration:
                self.label.setText("No more images.")

    def display_image(self, image_path):
        """
        Displays current image in annotatin file
        """
        if os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            scaled_pixmap = pixmap.scaled(self.image_label.size(), aspectRatioMode=1)
            self.image_label.setPixmap(scaled_pixmap)
            self.image_label.setScaledContents(True)
        else:
            self.label.setText("Image is not found.")


def main():
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
