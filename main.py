import sys,os

from backend.menu_inicial import MenuUrna

from PySide6.QtWidgets import QApplication

def main():
    
    app = QApplication(sys.argv)
    
   
    janela_principal = MenuUrna()
    
   
    janela_principal.show()
    
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()