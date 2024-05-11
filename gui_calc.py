from PyQt5 import QtWidgets, QtGui, QtCore
from logic import calculate_circle_area, calculate_square_area, calculate_rectangle_area, calculate_triangle_area

class MainWindow(QtWidgets.QMainWindow):
    """Main window class for the calculator GUI."""

    def __init__(self, parent=None):
        """Initialize the main window for the calculator GUI."""
        super(MainWindow, self).__init__(parent)
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.mainLayout = QtWidgets.QGridLayout(self.centralwidget)

        self.init_ui()
        self.setWindowTitle("CalculatorProject")

    def init_ui(self):
        """Initialize the entire user interface."""
        self.setup_display()
        self.setup_buttons()
        self.setup_area_calculation_ui()

    def setup_display(self):
        """Set up the display for the calculator."""
        self.display = QtWidgets.QLabel("", self)
        self.display.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.display.setFont(QtGui.QFont("Arial", 24))
        self.display.setFixedHeight(70)
        self.display.setStyleSheet("background-color: #cfc; border: 2px solid #0f9;")
        self.mainLayout.addWidget(self.display, 0, 0, 1, 5)

    def setup_buttons(self):
        """Set up the buttons for the calculator."""
        buttons = {
            'Clear': (1, 0), 'Del': (1, 1), 'Mode': (1, 2), '/': (1, 3),
            '7': (2, 0), '8': (2, 1), '9': (2, 2), '*': (2, 3),
            '4': (3, 0), '5': (3, 1), '6': (3, 2), '-': (3, 3),
            '1': (4, 0), '2': (4, 1), '3': (4, 2), '+': (4, 3),
            '+/-': (5, 0), '0': (5, 1), '.': (5, 2), '=': (5, 3)
        }
        self.buttons = {}
        for btnText, pos in buttons.items():
            button = QtWidgets.QPushButton(btnText, self)
            button.clicked.connect(self.on_button_clicked)
            self.buttons[btnText] = button
            self.mainLayout.addWidget(button, pos[0], pos[1])
        self.buttons['Mode'].clicked.connect(self.toggle_area_mode)

        self.areaFrame = QtWidgets.QFrame(self)
        self.areaLayout = QtWidgets.QGridLayout(self.areaFrame)
        self.mainLayout.addWidget(self.areaFrame, 0, 5, 6, 2)
        self.areaFrame.setVisible(False)

    def setup_area_calculation_ui(self):
        """Set up the UI elements for area calculation."""
        self.radioCircle = QtWidgets.QRadioButton("Circle")
        self.radioSquare = QtWidgets.QRadioButton("Square")
        self.radioRectangle = QtWidgets.QRadioButton("Rectangle")
        self.radioTriangle = QtWidgets.QRadioButton("Triangle")
        self.radioGroup = QtWidgets.QButtonGroup(self)
        self.radioGroup.addButton(self.radioCircle, 1)
        self.radioGroup.addButton(self.radioSquare, 2)
        self.radioGroup.addButton(self.radioRectangle, 3)
        self.radioGroup.addButton(self.radioTriangle, 4)
        self.radioGroup.buttonClicked.connect(self.update_input_fields)

        self.submitButton = QtWidgets.QPushButton("Calculate Area")
        self.submitButton.clicked.connect(self.calculate_area)
        self.areaInput1 = QtWidgets.QLineEdit()
        self.areaInput2 = QtWidgets.QLineEdit()

        self.areaLayout.addWidget(self.radioCircle, 1, 0)
        self.areaLayout.addWidget(self.radioSquare, 1, 1)
        self.areaLayout.addWidget(self.radioRectangle, 2, 0)
        self.areaLayout.addWidget(self.radioTriangle, 2, 1)
        self.areaLayout.addWidget(self.areaInput1, 3, 0, 1, 2)
        self.areaLayout.addWidget(self.areaInput2, 4, 0, 1, 2)
        self.areaLayout.addWidget(self.submitButton, 5, 0, 1, 2)

    def toggle_area_mode(self):
        """Toggle area calculation mode."""
        self.areaFrame.setVisible(not self.areaFrame.isVisible())

    def update_input_fields(self, button):
        """Update input fields based on the selected shape."""
        shape = button.text()
        if shape == "Circle":
            self.areaInput1.setPlaceholderText("Enter radius")
            self.areaInput2.hide()
        elif shape in ["Square", "Rectangle", "Triangle"]:
            self.areaInput1.setPlaceholderText("Enter dimension")
            self.areaInput2.show()
            if shape == "Rectangle":
                self.areaInput2.setPlaceholderText("Enter width")
            elif shape == "Triangle":
                self.areaInput2.setPlaceholderText("Enter base")
            else:
                self.areaInput2.hide()

    def on_button_clicked(self):
        """Handle button clicks."""
        button = self.sender()
        text = button.text()

        if text == "Clear":
            self.display.setText("")
        elif text == "Del":
            current_text = self.display.text()
            self.display.setText(current_text[:-1])
        elif text == "=":
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText("Error")
        elif text == "+/-":
            current_text = self.display.text()
            if current_text.startswith('-'):
                self.display.setText(current_text[1:])
            else:
                self.display.setText('-' + current_text if current_text != "0" else current_text)
        elif text in {'+', '-', '*', '/', '+/-', '.'} or text.isdigit():
            current_text = self.display.text()
            new_text = current_text + text
            self.display.setText(new_text)

    def calculate_area(self):
        """Calculate area based on user input using functions from logic_calc."""
        shape = self.radioGroup.checkedButton().text()
        try:
            if shape == "Circle":
                radius = float(self.areaInput1.text())
                area = calculate_circle_area(radius)
            elif shape == "Square":
                side = float(self.areaInput1.text())
                area = calculate_square_area(side)
            elif shape == "Rectangle":
                length = float(self.areaInput1.text())
                width = float(self.areaInput2.text())
                area = calculate_rectangle_area(length, width)
            elif shape == "Triangle":
                base = float(self.areaInput1.text())
                height = float(self.areaInput2.text())
                area = calculate_triangle_area(base, height)
            self.display.setText(f"Area={area:.2f}")
        except ValueError:
            self.display.setText("Error")


