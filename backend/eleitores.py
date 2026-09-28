class TituloEleitorBackEnd:
    def __init__(self):
        self.zeresima_emitida = True
        self.urna_encerrada = False

        self.eleitores = [
            {"titulo": "000001", "nome": "Luiz Carlos", "voto_computado": False},
            {"titulo": "000002", "nome": "Ryan Vidal", "voto_computado": False},
            {"titulo": "000003", "nome": "Lucas Sol", "voto_computado": False},
            {"titulo": "000004", "nome": "Arthur Domingues", "voto_computado": False},
            {"titulo": "000005", "nome": "Carla Lacerda", "voto_computado": False},
        ]

    def validar_eleitor(self, titulo: str) -> tuple[bool, str]:

        if not self.zeresima_emitida:
            return False, "A votação ainda não foi liberada! É necessário emitir a Zerésima."
        
        if self.urna_encerrada:
            return False, "A urna eletrônica já está encerrada para votação."

        titulo_limpo = titulo.strip()
        if not titulo_limpo:
            return False, "Por favor, digite o número do título de eleitor."

        eleitor = next((e for e in self.eleitores if e["titulo"] == titulo_limpo), None)

        if not eleitor:
            return False, "Título de eleitor não encontrado na base de dados."

        if eleitor["voto_computado"]:
            return False, f"O eleitor(a) {eleitor['nome']} já realizou a votação!"

        return True, eleitor["nome"]