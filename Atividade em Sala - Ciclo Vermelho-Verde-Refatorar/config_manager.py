_instancia_unica = None

class ConfigManager:
    def __new__(cls):
        global _instancia_unica
        # Implementação direta para garantir que a mesma instância seja retornada
        if _instancia_unica is None:
            _instancia_unica = super().__new__(cls)
            _instancia_unica.configuracoes = {}
        return _instancia_unica

    def get_all(self):
        return self.configuracoes

    def set(self, chave, valor):
        self.configuracoes[chave] = valor

    def get(self, chave):
        return self.configuracoes.get(chave)