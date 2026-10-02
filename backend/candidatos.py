import sys
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QTableWidgetItem, QHeaderView, QTableWidget, QApplication)


class Candidato:
    def __init__(self, numero: str, nome: str, cargo: str, foto: str = ""):
        self.numero = numero
        self.nome = nome
        self.cargo = cargo.upper()
        self.foto = foto
        self.votos = 0


candidatos_cadastrados = [
    Candidato("001", "Dollynho", "Presidente", "imagens/candidato_dollynho.webp"),
    Candidato("002", "Barriguinha mole", "Presidente", "imagens/candidato_barriguinha_mole.webp"),
    Candidato("003", "Naruto", "Presidente", "imagens/candidato_naruto.webp"),
]


def buscar_candidato(candidatos: list[Candidato], cargo: str, numero: str) -> Candidato | None:
    cargo_formatado = cargo.upper()
    for candidato in candidatos:
        if candidato.cargo == cargo_formatado and candidato.numero == numero:
            return candidato
    return None


class TelaCandidatos(QWidget):
    def __init__(self, candidatos_iniciais: list[Candidato] | None = None):
        super().__init__()
        self.lista_candidatos = candidatos_iniciais if candidatos_iniciais is not None else []
        self.setWindowTitle("Consulta de Candidatos")
        self.setMinimumSize(600, 400)
        self.inicializar_interface()
        self.atualizar_tabela()

    def inicializar_interface(self):
        layout_principal = QVBoxLayout(self)
        self.tabela_candidatos = QTableWidget()
        self.tabela_candidatos.setColumnCount(3)
        self.tabela_candidatos.setHorizontalHeaderLabels(["Cargo", "Número", "Nome"])
        self.tabela_candidatos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout_principal.addWidget(self.tabela_candidatos)

    def atualizar_tabela(self):
        self.tabela_candidatos.setRowCount(0)
        for candidato in self.lista_candidatos:
            posicao = self.tabela_candidatos.rowCount()
            self.tabela_candidatos.insertRow(posicao)
            self.tabela_candidatos.setItem(posicao, 0, QTableWidgetItem(candidato.cargo))
            self.tabela_candidatos.setItem(posicao, 1, QTableWidgetItem(candidato.numero))
            self.tabela_candidatos.setItem(posicao, 2, QTableWidgetItem(candidato.nome))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = TelaCandidatos(candidatos_cadastrados)
    tela.show()
    sys.exit(app.exec())