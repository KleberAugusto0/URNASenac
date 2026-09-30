class CandidatoBackEnd:
    def __init__(self):
        self.candidatos = [
            {"numero": 11, "nome": "Gyaradus", "partido": "P-POKEMON", "votos": 0},
            {"numero": 22, "nome": "Naruto", "partido": "P-VILLA_FOLHA", "votos": 0},
            {"numero": 33, "nome": "Orangotango", "partido": "AMAZONIA", "votos": 0},
        ]
        
        self.votos_brancos = 0
        self.votos_nulos = 0

    def buscar_candidato(self, entrada: str) -> dict | None:

        entrada_limpa = entrada.strip()
        
        if not entrada_limpa.isdigit():
            return None

        numero_digitado = int(entrada_limpa)
        return next((c for c in self.candidatos if c["numero"] == numero_digitado), None)

    def registrar_voto(self, tipo_voto: str, candidato_numero: int | None = None) -> bool:
    
            if tipo_voto == "VALIDO" and candidato_numero is not None:
                candidato = next((c for c in self.candidatos if c["numero"] == candidato_numero), None)
                if candidato:
                    candidato["votos"] += 1
                    return True
                return False
    
            elif tipo_voto == "BRANCO":
                self.votos_brancos += 1
                return True
    
            elif tipo_voto == "NULO":
                self.votos_nulos += 1
                return True
    
            return False