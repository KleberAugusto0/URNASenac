import os
import sys
from pathlib import Path
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QMessageBox, QWidget)
from backend.urna import Urna
from backend.pop_up_aviso_da_zeressima import TelaAvisoZeresima
from backend.pop_up_voto_nulo import TelaVotoNulo
from backend.pop_up_confirmar_candidato import TelaConfirmacaoVoto
from backend.tela_confirmacao_voto import TelaConfirmacaoVoto as TelaVotoRegistrado
from backend.tela_titulo_eleitor import TelaTituloEleitor
from backend.tela_votacao import TelaDeVotacao
from backend.tela_zeresima import TelaZerezima

BASE_DIR = Path(__file__).resolve().parent


class TelaRelatorioFinal(TelaZerezima):
    def __init__(self, urna, parent=None):
        super().__init__(urna=urna, titulo="RELATÓRIO FINAL", subtitulo="Resultado da Votação", parent=parent)


class MenuUrna(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu")
        self.urna = Urna()
        self.janela_aberta = None
        self.montar_interface()
        self.carregar_estilo()

    def montar_interface(self):
        layout = QVBoxLayout(self)
        layout.addStretch(1)

        txt_urna = QLabel("Urna Eletrônica")
        txt_urna.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(txt_urna)

        self.botao_zerezima = QPushButton("Relatório inicial (Zerésima)")
        self.botao_zerezima.setFixedSize(250, 50)
        self.botao_zerezima.clicked.connect(self.emitir_zeresima)
        layout.addWidget(self.botao_zerezima, alignment=Qt.AlignmentFlag.AlignCenter)

        self.botao_votar = QPushButton("Votar")
        self.botao_votar.setFixedSize(250, 50)
        self.botao_votar.clicked.connect(self.votar)
        layout.addWidget(self.botao_votar, alignment=Qt.AlignmentFlag.AlignCenter)

        self.botao_relatorio = QPushButton("Relatório Final")
        self.botao_relatorio.setFixedSize(250, 50)
        self.botao_relatorio.clicked.connect(self.relatorio)
        layout.addWidget(self.botao_relatorio, alignment=Qt.AlignmentFlag.AlignCenter)

        self.botao_sair = QPushButton("Sair")
        self.botao_sair.setObjectName("botao_sair")
        self.botao_sair.setFixedSize(250, 50)
        self.botao_sair.clicked.connect(self.sair_do_sistema)
        layout.addWidget(self.botao_sair, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addStretch(1)
        self.setFixedSize(500, 500)

    def carregar_estilo(self):
        caminho = BASE_DIR / "estilo" / "estilo_menu.qss"
        if caminho.exists():
            with open(caminho, "r", encoding="utf-8") as arquivo:
                self.setStyleSheet(arquivo.read())

    def emitir_zeresima(self):
        self.urna.emitir_zeresima()
        tela = TelaZerezima(self.urna, parent=self)
        self.janela_aberta = tela
        tela.exec()

    def verificar_zeresima(self, acao):
        if not self.urna.zeresima_emitida:
            TelaAvisoZeresima(acao=acao, parent=self).exec()
            return False
        return True

    def votar(self):
        if not self.verificar_zeresima("votar"):
            return

        tela_titulo = TelaTituloEleitor(self)
        self.janela_aberta = tela_titulo
        tela_titulo.titulo_confirmado.connect(lambda titulo: self.validar_titulo(tela_titulo, titulo))
        tela_titulo.exec()

    def validar_titulo(self, tela_titulo, titulo):
        valido, mensagem = self.urna.validar_eleitor(titulo)
        if not valido:
            QMessageBox.warning(tela_titulo, "Votação", mensagem)
            return

        tela_titulo.accept()
        self.abrir_tela_votacao(titulo)

    def abrir_tela_votacao(self, titulo):
        tela_votacao = TelaDeVotacao(self)
        self.janela_aberta = tela_votacao
        tela_votacao.voto_confirmado.connect(lambda numero: self.processar_voto(titulo, numero, tela_votacao))
        tela_votacao.show()

    def processar_voto(self, titulo, numero, tela_votacao):
        if numero == "BRANCO":
            tela_votacao.close()
            self.urna.registrar_voto_branco(titulo)
            TelaVotoRegistrado(self).exec()
            return

        candidato = self.urna.buscar_candidato(numero)
        if candidato is None:
            dialogo_nulo = TelaVotoNulo(self)
            if dialogo_nulo.exec() == QDialog.DialogCode.Accepted:
                tela_votacao.close()
                self.urna.registrar_voto_nulo(titulo)
                TelaVotoRegistrado(self).exec()
            return

        confirmacao = TelaConfirmacaoVoto(candidato, self)
        if confirmacao.exec() == QDialog.DialogCode.Accepted:
            tela_votacao.close()
            self.urna.registrar_voto_candidato(titulo, candidato)
            TelaVotoRegistrado(self).exec()
            self.janela_aberta = None

    def relatorio(self):
        if not self.verificar_zeresima("relatório final"):
            return
        tela = TelaRelatorioFinal(self.urna, parent=self)
        self.janela_aberta = tela
        tela.exec()

    def sair_do_sistema(self):
        tela_sair = QDialog(self)
        tela_sair.setFixedSize(450, 280)
        tela_sair.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)

        tela_alinhamento = QVBoxLayout(tela_sair)
        layout_botoes = QHBoxLayout()

        botao_fechar = QPushButton("×")
        botao_fechar.setObjectName("botao_fechar_x")
        botao_fechar.clicked.connect(tela_sair.reject)
        tela_alinhamento.addWidget(botao_fechar, alignment=Qt.AlignmentFlag.AlignRight)

        icone = QLabel()
        icone.setObjectName("quadrado_icone")
        caminho_imagem = BASE_DIR / "imagens" / "exit.png"
        if caminho_imagem.exists():
            icone.setPixmap(QPixmap(str(caminho_imagem)).scaled(78, 78, Qt.AspectRatioMode.KeepAspectRatio))
        tela_alinhamento.addWidget(icone, alignment=Qt.AlignmentFlag.AlignCenter)

        titulo = QLabel("Sair do sistema")
        titulo.setObjectName("titulo_popup")
        subtitulo = QLabel("Tem certeza que deseja sair?")
        subtitulo.setObjectName("subtitulo_popup")
        tela_alinhamento.addWidget(titulo, alignment=Qt.AlignmentFlag.AlignCenter)
        tela_alinhamento.addWidget(subtitulo, alignment=Qt.AlignmentFlag.AlignCenter)

        botao_cancelar = QPushButton("Cancelar")
        botao_cancelar.setObjectName("botao_cancelar_dialog")
        botao_cancelar.clicked.connect(tela_sair.reject)

        botao_confirmar = QPushButton("Confirmar")
        botao_confirmar.setObjectName("botao_confirmar_dialog")
        botao_confirmar.clicked.connect(tela_sair.accept)

        layout_botoes.addWidget(botao_cancelar)
        layout_botoes.addWidget(botao_confirmar)
        tela_alinhamento.addLayout(layout_botoes)

        caminho_estilo = BASE_DIR / "estilo" / "estilo_sair.qss"
        if caminho_estilo.exists():
            with open(caminho_estilo, "r", encoding="utf-8") as arquivo:
                tela_sair.setStyleSheet(arquivo.read())

        if tela_sair.exec() == QDialog.DialogCode.Accepted:
            QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    caminho_estilo = BASE_DIR / "estilo" / "estilo_menu.qss"
    if caminho_estilo.exists():
        with open(caminho_estilo, "r", encoding="utf-8") as arquivo:
            app.setStyleSheet(arquivo.read())
    janela = MenuUrna()
    janela.show()
    sys.exit(app.exec())