import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,QVBoxLayout,QPushButton, QTableWidget,QTableWidgetItem)
from ui.transaction_dialog import TransactionDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Expense Tracker")
        self.resize(900, 600)
        
        
        #central widget
        central_widget= QWidget()
        self.setCentralWidget(central_widget)

        #layout principal
        layout=QVBoxLayout()
        central_widget.setLayout(layout)

        #botón
        self.add_button=QPushButton("Agregar Transacción")
        layout.addWidget(self.add_button)
        #agregar botón
        self.add_button.clicked.connect(self.open_add_transaction)

        #tabla
        table= QTableWidget()
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(["Tipo","monto","Categoría","Fecha", "Descripción"])
        layout.addWidget(table)

    #añadir transacción
    def open_add_transaction(self):
        dialog=TransactionDialog()
        if dialog.exec():
            data= dialog.get_data()
            print(data)
        

if __name__=="__main__":
    app=QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())    
