# Padrão de Projeto Aplicado: Singleton
# Participantes:
# - Singleton: ConfigManager (garante que apenas uma instância de configurações exista globalmente).
# - Client: Os testes no arquivo test_config.py (que instanciam e consomem o gerenciador).

class ConfigManager:
    _instance = None  # Atributo de classe para armazenar a instância única de forma encapsulada

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance.configuracoes = {}
        return cls._instance

    def get_all(self):
        return self.configuracoes

    def set(self, chave, valor):
        self.configuracoes[chave] = valor

    def get(self, chave):
        return self.configuracoes.get(chave)

"""
  AUTOAVALIAÇÃO:
- Tempo gasto: 30 min, onde: 5 min (entendimento do problema e da atividade), 5 min (escrita dos testes), 5 min (entendendo o que a IA propôs),
5 min (resolução dos problemas), 5 min (compreensão do funcionamento do Singleton), 5 min (implementação do Singleton e testes).

- Critérios atingidos: 1, 2, 3, 4 e 5.

- Mudanças na estrutura: Entre a fase verde e a refatorada, o código deixou de depender de uma variável global solta no módulo (`_instancia_unica`) para utilizar um atributo de classe encapsulado (`_instance`).
Isso tornou a classe coesa e aplicou formalmente a estrutura do padrão Singleton.

- Parte mais trabalhosa: Entender e manipular o método mágico `__new__` em Python para interceptar a criação do objeto antes do `__init__`.

- Uso de IA: O assistente ajudou a estruturar os passos do TDD, a escrever os testes assertivos e a formatar os comentários conforme exigido pelas instruções.
Atrapalhou apenas na parte de explicação do uso do pytest, mas não foi necessáriamente um problema com a atividade.

- Saída da execução final dos testes (Critério 5): 

PS C:\Users\lucas\Documents\eng-software\Atividade em Sala - Ciclo Vermelho-Verde-Refatorar> python -m pytest   
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.14.7, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\lucas\Documents\eng-software\Atividade em Sala - Ciclo Vermelho-Verde-Refatorar
collected 3 items                                                                                                                                           

test_config.py ...                                                                                                                                    [100%]

==================================================================== 3 passed in 0.01s =====================================================================
"""