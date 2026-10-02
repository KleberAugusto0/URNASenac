import os
import sys
from pathlib import Path
from PySide6.QtCore import Qt, QSize as Tamanho, QEvent, QObject
from PySide6.QtGui import QPixmap,QIcon
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QToolButton, QComboBox, QCheckBox, QRadioButton)
from backend.urna import Urna
from backend.pop_up_aviso_da_zeressima import TelaAvisoZeresima
from backend.pop_up_voto_nulo import TelaVotoNulo
from backend.pop_up_confirmar_candidato import TelaConfirmacaoVoto
from backend.tela_confirmacao_voto import TelaConfirmacaoVoto as TelaVotoRegistrado
from backend.tela_titulo_eleitor import TelaTituloEleitor
from backend.tela_votacao import TelaDeVotacao
from backend.tela_zeresima import TelaZerezima

BASE_DIR = Path(__file__).resolve().parent


class CursorBotoes(QObject):

    def eventFilter(self, objeto, evento):
        if evento.type() == QEvent.Type.Enter and isinstance(
            objeto, (QPushButton, QToolButton, QComboBox, QCheckBox, QRadioButton)
        ):
            objeto.setCursor(Qt.CursorShape.PointingHandCursor)
        return super().eventFilter(objeto, evento)


def ativar_cursor_botoes(aplicacao):
    filtro_cursor = CursorBotoes(aplicacao)
    aplicacao.installEventFilter(filtro_cursor)
    aplicacao._filtro_cursor_botoes = filtro_cursor


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
        self.botao_zerezima.setEnabled(not self.urna.zeresima_emitida)

    def montar_interface(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 16, 30, 12)
        layout.setSpacing(8)

        layout_cabecalho = QHBoxLayout()
        layout_cabecalho.setContentsMargins(0, 0, 0, 0)
        layout_cabecalho.setSpacing(10)

        icone_urna = QLabel()
        icone_urna.setObjectName("icone_urna_menu")
        icone_urna.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icone_urna.setFixedSize(50, 50)
        caminho_icone_urna = BASE_DIR / "imagens" / "voting-box.png"
        if caminho_icone_urna.exists():
            icone_urna.setPixmap(
                QPixmap(str(caminho_icone_urna)).scaled(
                    50, 50,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
        layout_cabecalho.addWidget(icone_urna)

        layout_textos = QVBoxLayout()
        layout_textos.setContentsMargins(0, 0, 0, 0)
        layout_textos.setSpacing(2)

        txt_urna = QLabel("URNA ELETRÔNICA")
        txt_urna.setObjectName("titulo_urna_menu")
        layout_textos.addWidget(txt_urna)

        subtitulo_urna = QLabel("Sistema de Votação")
        subtitulo_urna.setObjectName("subtitulo_urna_menu")
        layout_textos.addWidget(subtitulo_urna)

        layout_cabecalho.addLayout(layout_textos)
        layout_cabecalho.addStretch()
        layout.addLayout(layout_cabecalho)

        layout.addSpacing(9)

        self.botao_zerezima = QPushButton("ZERÉSIMA")
        self.botao_zerezima.setObjectName("botao_menu")
        self.botao_zerezima.setFixedSize(260, 43)
        self.botao_zerezima.clicked.connect(self.emitir_zeresima)
        self.botao_zerezima.setIcon(QIcon(str(BASE_DIR / "imagens" / "icone_documento.png")))
        self.botao_zerezima.setIconSize(Tamanho(25, 25))
        layout.addWidget(self.botao_zerezima, alignment=Qt.AlignmentFlag.AlignCenter)

        self.botao_votar = QPushButton("VOTAR")
        self.botao_votar.setObjectName("botao_menu")
        self.botao_votar.setFixedSize(260, 43)
        self.botao_votar.clicked.connect(self.votar)
        self.botao_votar.setIcon(QIcon(str(BASE_DIR / "imagens" / "voting-box.png")))
        self.botao_votar.setIconSize(Tamanho(25, 25))
        layout.addWidget(self.botao_votar, alignment=Qt.AlignmentFlag.AlignCenter)

        self.botao_relatorio = QPushButton("RELATÓRIO FINAL")
        self.botao_relatorio.setObjectName("botao_menu")
        self.botao_relatorio.setFixedSize(260, 43)
        self.botao_relatorio.clicked.connect(self.relatorio)
        self.botao_relatorio.setIcon(QIcon(str(BASE_DIR / "imagens" / "icone_grafico.png")))
        self.botao_relatorio.setIconSize(Tamanho(25, 25))
        layout.addWidget(self.botao_relatorio, alignment=Qt.AlignmentFlag.AlignCenter)

        self.botao_sair = QPushButton("SAIR")
        self.botao_sair.setObjectName("botao_sair")
        self.botao_sair.setFixedSize(260, 43)
        self.botao_sair.clicked.connect(self.sair_do_sistema)
        self.botao_sair.setIcon(QIcon(str(BASE_DIR / "imagens" / "sair.png")))
        self.botao_sair.setIconSize(Tamanho(25, 25))
        layout.addWidget(self.botao_sair, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addStretch(1)

        self.setFixedSize(354, 306)

    def carregar_estilo(self):
        caminho = BASE_DIR / "estilo" / "estilo_menu.qss"
        if caminho.exists():
            with open(caminho, "r", encoding="utf-8") as arquivo:
                self.setStyleSheet(arquivo.read())

    def emitir_zeresima(self):
        if self.urna.zeresima_emitida:
            TelaAvisoZeresima(
                parent=self,
                titulo="Zerésima já emitida",
                mensagem="A Zerésima já foi emitida e não pode\nser emitida novamente.").exec()
            return

        if self.urna.urna_encerrada:
            TelaAvisoZeresima(
                parent=self,
                titulo="Zerésima",
                mensagem="Não é possível emitir a Zerésima porque\no Relatório Final já foi emitido.").exec()
            return

        if not self.urna.emitir_zeresima():
            return

        self.botao_zerezima.setEnabled(False)
        tela = TelaZerezima(self.urna, parent=self)
        self.janela_aberta = tela
        tela.exec()

    def verificar_zeresima(self, acao):
        if not self.urna.zeresima_emitida:
            TelaAvisoZeresima(acao=acao, parent=self).exec()
            return False
        return True

    def votar(self):
        if self.urna.urna_encerrada:
            TelaAvisoZeresima(
                parent=self,
                titulo="Votação",
                mensagem="Não é possível votar porque o Relatório Final\njá foi emitido e a urna está encerrada.").exec()
            return

        if not self.verificar_zeresima("votar"):
            return

        tela_titulo = TelaTituloEleitor(self)
        self.janela_aberta = tela_titulo
        tela_titulo.titulo_confirmado.connect(lambda titulo: self.validar_titulo(tela_titulo, titulo))
        tela_titulo.exec()

    def validar_titulo(self, tela_titulo, titulo):
        valido, mensagem = self.urna.validar_eleitor(titulo)
        if not valido:
            TelaAvisoZeresima(
                parent=tela_titulo,
                titulo="Votação",
                mensagem=mensagem).exec()
            return

        tela_titulo.accept()
        self.abrir_tela_votacao(titulo)

    def abrir_tela_votacao(self, titulo):
        tela_votacao = TelaDeVotacao(self)
        self.janela_aberta = tela_votacao
        tela_votacao.voto_confirmado.connect(lambda numero: self.processar_voto(titulo, numero, tela_votacao))
        tela_votacao.show()

    def processar_voto(self, titulo, numero, tela_votacao):
        if self.urna.urna_encerrada:
            tela_votacao.close()
            TelaAvisoZeresima(
                parent=self,
                titulo="Votação",
                mensagem="Não é possível registrar o voto porque o Relatório Final\njá foi emitido e a urna está encerrada.").exec()
            return

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

        self.urna.encerrar_urna()
        tela = TelaRelatorioFinal(self.urna, parent=self)
        self.janela_aberta = tela
        tela.exec()

    def sair_do_sistema(self):
        tela_sair = QDialog(self)
        tela_sair.setObjectName("tela_sair")
        tela_sair.setFixedSize(460, 400)
        tela_sair.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)

        layout_raiz = QVBoxLayout(tela_sair)
        layout_raiz.setContentsMargins(24, 16, 24, 24)
        layout_raiz.setSpacing(0)

        botao_fechar = QPushButton("×")
        botao_fechar.setObjectName("botao_fechar_x")
        botao_fechar.setCursor(Qt.PointingHandCursor)
        botao_fechar.setFixedSize(28, 28)
        botao_fechar.clicked.connect(tela_sair.reject)

        layout_topo = QHBoxLayout()
        layout_topo.addStretch()
        layout_topo.addWidget(botao_fechar)
        layout_raiz.addLayout(layout_topo)

        icone = QLabel()
        icone.setObjectName("quadrado_icone")
        icone.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icone.setFixedSize(84, 84)
        caminho_imagem = BASE_DIR / "imagens" / "sair.png"
        if caminho_imagem.exists():
            icone.setPixmap(
                QPixmap(str(caminho_imagem)).scaled(
                    84, 84, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation
                )
            )
        layout_raiz.addWidget(icone, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_raiz.addSpacing(16)

        titulo = QLabel("Saindo do sistema")
        titulo.setObjectName("titulo_popup")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_raiz.addWidget(titulo)
        layout_raiz.addSpacing(12)

        subtitulo = QLabel("Tem certeza que deseja sair?")
        subtitulo.setObjectName("subtitulo_popup")
        subtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_raiz.addWidget(subtitulo)

        layout_raiz.addSpacing(24)

        layout_botoes = QHBoxLayout()
        layout_botoes.setSpacing(12)

        botao_cancelar = QPushButton("Cancelar")
        botao_cancelar.setObjectName("botao_cancelar_dialog")
        botao_cancelar.setCursor(Qt.PointingHandCursor)
        botao_cancelar.setFixedHeight(48)
        botao_cancelar.clicked.connect(tela_sair.reject)

        botao_confirmar = QPushButton("Confirmar")
        botao_confirmar.setObjectName("botao_confirmar_dialog")
        botao_confirmar.setCursor(Qt.PointingHandCursor)
        botao_confirmar.setFixedHeight(48)
        botao_confirmar.clicked.connect(tela_sair.accept)
        

        layout_botoes.addWidget(botao_cancelar)
        layout_botoes.addWidget(botao_confirmar)
        layout_raiz.addLayout(layout_botoes)

        caminho_estilo = BASE_DIR / "estilo" / "estilo_sair.qss"
        if caminho_estilo.exists():
            with open(caminho_estilo, "r", encoding="utf-8") as arquivo:
                tela_sair.setStyleSheet(arquivo.read())

        geometria_pai = self.frameGeometry()
        centro_pai = geometria_pai.center()
        geometria_dialogo = tela_sair.frameGeometry()
        geometria_dialogo.moveCenter(centro_pai)
        tela_sair.move(geometria_dialogo.topLeft())

        if tela_sair.exec() == QDialog.DialogCode.Accepted:
            QApplication.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ativar_cursor_botoes(app)
    caminho_estilo = BASE_DIR / "estilo" / "estilo_menu.qss"
    if caminho_estilo.exists():
        with open(caminho_estilo, "r", encoding="utf-8") as arquivo:
            app.setStyleSheet(arquivo.read())
    janela = MenuUrna()
    janela.show()
    sys.exit(app.exec())