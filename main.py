from PyQt5 import QtWidgets
from gui_calc import MainWindow
import sys

def main():
    """Main function to start the application."""
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
