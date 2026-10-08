"""
Plano de Execução:
- Problema escolhido: Um Gerenciador de Configurações (ConfigManager) de uma aplicação.
- Padrão escolhido: Singleton.
- Por que: Em uma aplicação, faz sentido ter apenas um ponto global de acesso às configurações, garantindo que qualquer parte do sistema acesse ou modifique o mesmo estado.
- Casos a testar (3 variações de comportamento):
  1. O gerenciador deve inicializar com configurações padrão vazias.
  2. O gerenciador deve permitir adicionar e recuperar uma configuração específica.
  3. O gerenciador deve garantir que múltiplas chamadas de instanciação retornem a mesma instância na memória (comportamento chave do Singleton).
- Tempo alocado: 10 min (Plano), 15 min (Red), 10 min (Green), 75 min (Refactor), 10 min (Autoavaliação).
- Uso de IA: Assistente Gemini utilizado para estruturar a estratégia de testes, definir o problema aderente ao Singleton e formatar os comentários exigidos.
"""

import pytest
from config_manager import ConfigManager

def test_initial_config_is_empty():
    """variação 1: Inicialização padrão"""
    config = ConfigManager()
    assert config.get_all() == {}

def test_set_and_get_config():
    """variação 2: Modificação de estado"""
    config = ConfigManager()
    config.set("theme", "dark")
    assert config.get("theme") == "dark"

def test_multiple_instances_share_state():
    """variação 3: Comportamento de estado compartilhado/instância única"""
    config1 = ConfigManager()
    config1.set("language", "pt-br")

    config2 = ConfigManager()
    # no ciclo green isso vai falhar se instanciarmos objetos diferentes
    assert config2.get("language") == "pt-br" 
    assert config1 is config2