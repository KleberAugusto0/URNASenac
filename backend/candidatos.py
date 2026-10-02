import sys
<<<<<<< HEAD
from PySide6.QtWidgets import (
    QWidget,QVBoxLayout,QHBoxLayout,
    QLineEdit, QComboBox, QPushButton,
    QTableWidgetItem, QHeaderView,QLabel, QTableWidget
)
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Signal



class Candidato:
    def __init__(self, numero: str, nome: str,partido: str, cargo: str, vice: str = None):
        self.numero = numero
        self.nome = nome
        self.partido = partido
        self.cargo = cargo.upper()
        self.vice = vice

candidatos_cadastrados = [
    Candidato("001" , "Dollynho", "Presidente"),
    Candidato("002" , "Eren", "Presidente"),
    Candidato("003" , "Naruto" , "Presidente"),
    Candidato("004" , "Gyro" , "Presidente")
]


class TelaCandidatos(QWidget):
    def __init__(self, candidatos_iniciais: list[Candidato] = None):
=======
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
>>>>>>> 04ac49f0616f7c423d0141229bf8e0e6ea10d209
        super().__init__()
        self.lista_candidatos = candidatos_iniciais if candidatos_iniciais is not None else []
        self.setWindowTitle("Consulta de Candidatos")
        self.setMinimumSize(600, 400)
        self.inicializar_interface()
        self.atualizar_tabela()

    def inicializar_interface(self):
        layout_principal = QVBoxLayout(self)
<<<<<<< HEAD

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
=======
        self.tabela_candidatos = QTableWidget()
        self.tabela_candidatos.setColumnCount(3)
        self.tabela_candidatos.setHorizontalHeaderLabels(["Cargo", "Número", "Nome"])
        self.tabela_candidatos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout_principal.addWidget(self.tabela_candidatos)

    def atualizar_tabela(self):
        self.tabela_candidatos.setRowCount(0)
        for candidato in self.lista_candidatos:
>>>>>>> 04ac49f0616f7c423d0141229bf8e0e6ea10d209
            posicao = self.tabela_candidatos.rowCount()
            self.tabela_candidatos.insertRow(posicao)
            self.tabela_candidatos.setItem(posicao, 0, QTableWidgetItem(candidato.cargo))
            self.tabela_candidatos.setItem(posicao, 1, QTableWidgetItem(candidato.numero))
            self.tabela_candidatos.setItem(posicao, 2, QTableWidgetItem(candidato.nome))
<<<<<<< HEAD
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
=======
>>>>>>> 04ac49f0616f7c423d0141229bf8e0e6ea10d209


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = TelaCandidatos(candidatos_cadastrados)
    tela.show()
    sys.exit(app.exec())