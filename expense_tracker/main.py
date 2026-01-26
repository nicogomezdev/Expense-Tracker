import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,QVBoxLayout,QPushButton, QTableWidget,QTableWidgetItem)
from ui.transaction_dialog import TransactionDialog
from database.database import init_db, save_expense

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
        self.table= QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Tipo","monto","Categoría","Fecha", "Descripción"])
        layout.addWidget(self.table)

    #añadir transacción
    def open_add_transaction(self):
        dialog=TransactionDialog()
        if dialog.exec():
            data= dialog.get_data()
            expense_id =save_expense(data)
            self.add_expense_to_table(data)

    #metodo para agregar una fila (UI)
    def add_expense_to_table(self, data: dict):
        row= self.table.rowCount()
        self.table.insertRow(row)

        self.table.setItem(row, 0, QTableWidgetItem(data["type"]))
        self.table.setItem(row, 1, QTableWidgetItem(str(data["amount"])))
        self.table.setItem(row, 2, QTableWidgetItem(data["category"]))
        self.table.setItem(row, 3, QTableWidgetItem(data["date"]))
        self.table.setItem(row, 4, QTableWidgetItem(data["description"]))
        

if __name__=="__main__":
    init_db()
    app=QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())    

