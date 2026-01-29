from PySide6.QtWidgets import(QDialog,QVBoxLayout,QLabel,QLineEdit,QPushButton,QHBoxLayout, QMessageBox)
from datetime import date
from PySide6.QtWidgets import QComboBox
from PySide6.QtWidgets import QDateEdit
from PySide6.QtCore import QDate
from PySide6.QtGui import QDoubleValidator

class TransactionDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nueva Transaccion")
        self.resize(400,300)

        layout=QVBoxLayout()
        self.setLayout(layout)

        #campos
        self.type_input= QComboBox()
        self.type_input.addItems(["Ingreso","Gasto"])

        self.amount_input=QLineEdit()
        self.amount_input.setValidator(QDoubleValidator(0,9999999,2))

        self.category_input = QLineEdit()
        self.category_input.setPlaceholderText("Categoria")

        self.description_input= QLineEdit()
        self.description_input.setPlaceholderText("Descripcion")

        self.date_input = QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QDate.currentDate())
        self.date_input.setDisplayFormat("yyyy-MM-dd")

        #Layout Addwidget Campos
        layout.addWidget(QLabel("Tipo"))
        layout.addWidget(self.type_input)

        layout.addWidget(QLabel("Monto"))
        layout.addWidget(self.amount_input)

        layout.addWidget(QLabel("Categoría"))
        layout.addWidget(self.category_input)

        layout.addWidget(QLabel("Descripción"))
        layout.addWidget(self.description_input)

        layout.addWidget(QLabel("Fecha"))
        layout.addWidget(self.date_input)

        #botones
        buttons_layout=QHBoxLayout()

        self.save_button=QPushButton("Guardar")
        self.cancel_button=QPushButton("Cancelar")

        buttons_layout.addWidget(self.save_button)
        buttons_layout.addWidget(self.cancel_button)

        layout.addLayout(buttons_layout)
        
        self.cancel_button.clicked.connect(self.reject)
        self.save_button.clicked.connect(self.validate_and_accept)
    
    #crea diccionario con los datos ingresados
    def get_data(self):
        return{
            "type":self.type_input.currentText(),
            "amount":self.amount_input.text(),
            "category": self.category_input.text(),
            "date": self.date_input.date().toString("yyyy-MM-dd"),
            "description":self.description_input.text(),
        }
    
    #valida y acepta
    def validate_and_accept(self):
        if not self.type_input.currentText() or not self.amount_input.text()or not self.category_input.text() or not self.description_input.text():
            QMessageBox.warning(self,"Error","Todos los campos son obligatorios")
            return 
        self.accept()