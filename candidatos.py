import sys
from PySide6.QtWidgets import (
    QWidget,QVBoxLayout,QHBoxLayout,
    QLineEdit, QComboBox, QPushButton,
    QTableWidgetItem, QHeaderView,QLabel, QTableWidget
)
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Signal



class Candidato:
    def __init__(self, numero: str, nome: str, cargo: str, vice: str = None):
        self.numero = numero
        self.nome = nome
        self.partido = self.partido
        self.cargo = cargo.upper()
        self.vice = vice

candidatos_cadastrados = [
    Candidato("11111", "Gyaradus", "P-POKEMON", "VEREADOR"),
    Candidato("22222", "Naruto", "P-VILA_FOLHA", "VEREADOR"),
    Candidato("11", "Ronaldo", "P-FUTEZIN", "PREFEITO", vice= "Messi"),
    Candidato("22", "Orangotango", "P-AMAZONIA", "PREFEITO", vice= "Gorila tonhão")
]


class TelaCandidatos(QWidget):
    def __init__(self, candidatos_iniciais: list[Candidato] = None):
        super().__init__()
        self.lista_candidatos = candidatos_iniciais if candidatos_iniciais is not None else []
        self.setWindowTitle("Consulta de Candidatos")
        self.setMinimumSize(600, 400)
        self.inicializar_interface()
        self.atualizar_tabela()

    def inicializar_interface(self):
        layout_principal = QVBoxLayout(self)

        layout_filtro = QHBoxLayout()
        label_filtro = QLabel("Filtrar por Cargo:")
        self.combo_filtro = QComboBox()
        self.combo_filtro.addItems(["TODOS", "VEREADOR", "PREFEITO"])
        self.combo_filtro.currentTextChanged.connect(self.filtrar_por_cargo)

        layout_filtro.addWidget(label_filtro)
        layout_filtro.addWidget(self.combo_filtro)

        self.tabela_candidatos = QTableWidget()
        self.tabela_candidatos.setColumnCount(5)
        self.tabela_candidatos.setHorizontalHeaderLabels(["Cargo", "Número", "Nome", "Partido", "Vice"])
        self.tabela_candidatos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        layout_principal.addLayout(layout_filtro)
        layout_principal.addWidget(self.tabela_candidatos)

    def atualizar_tabela(self, candidatos_exibir: list[Candidato] = None):
        if candidatos_exibir is None:
            candidatos_exibir = self.lista_candidatos

        self.tabela_candidatos.setRowCount(0)
        for candidato in candidatos_exibir:
            posicao = self.tabela_candidatos.rowCount()
            self.tabela_candidatos.insertRow(posicao)
            self.tabela_candidatos.setItem(posicao, 0, QTableWidgetItem(candidato.cargo))
            self.tabela_candidatos.setItem(posicao, 1, QTableWidgetItem(candidato.numero))
            self.tabela_candidatos.setItem(posicao, 2, QTableWidgetItem(candidato.nome))
            self.tabela_candidatos.setItem(posicao, 3, QTableWidgetItem(candidato.partido))
            self.tabela_candidatos.setItem(posicao, 4, QTableWidgetItem(candidato.vice if candidato.vice else "-"))

    def filtrar_por_cargo(self, cargo_selecionado: str):
        if cargo_selecionado == "TODOS":
            self.atualizar_tabela(self.lista_candidatos)
        else:
            filtrados = [candidato for candidato in self.lista_candidatos if candidato.cargo == cargo_selecionado]
            self.atualizar_tabela(filtrados)

    def buscar_candidato(self, cargo: str, numero: str) -> Candidato | None:
        cargo_formatado = cargo.upper()
        for candidato in self.lista_candidatos:
            if candidato.cargo == cargo_formatado and candidato.numero == numero:
                return candidato
        return None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = TelaCandidatos(candidatos_cadastrados)
    tela.show()
    sys.exit(app.exec())