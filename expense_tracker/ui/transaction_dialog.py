from PySide6.QtWidgets import(QDialog,QVBoxLayout,QLabel,QLineEdit,QPushButton,QHBoxLayout, QMessageBox)

from PySide6.QtGui import QDoubleValidator

class TransactionDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nueva Transaccion")
        self.resize(400,300)

        layout=QVBoxLayout()
        self.setLayout(layout)

        #campos
        self.amount_input=QLineEdit()
        self.amount_input.setValidator(QDoubleValidator(0,9999999,2))

        self.category_input = QLineEdit()
        self.category_input.setPlaceholderText("Categoria")

        layout.addWidget(QLabel("Monto"))
        layout.addWidget(self.amount_input)

        layout.addWidget(QLabel("Categoría"))
        layout.addWidget(self.category_input)

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
            "amount":self.amount_input.text(),
            "category": self.category_input.text()
        }
    
    #valida y acepta
    def validate_and_accept(self):
        if not self.amount_input.text()or not self.category_input.text():
            QMessageBox.warning(self,"Error","Todos los campos son obligatorios")
            return 
        self.accept