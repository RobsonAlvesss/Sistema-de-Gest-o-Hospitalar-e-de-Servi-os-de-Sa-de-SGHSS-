from datetime import datetime

# Função para agendar uma consulta
def agendar_consulta(paciente: str, consulta: str) -> str:
    """
    Simula o agendamento de uma consulta.

    Parâmetros:
        paciente (str): Nome do paciente.
        consulta (str): Data e hora da consulta no formato 'YYYY-MM-DD HH:MM'.

    Retorna:
        str: Mensagem de confirmação do agendamento.

    Levanta:
        ValueError: Se o formato da data for inválido.
    """
    try:
        datetime.strptime(consulta, "%Y-%m-%d %H:%M")  # Valida o formato da data
    except ValueError:
        raise ValueError("Formato de data inválido. Use 'YYYY-MM-DD HH:MM'.")

    return f"Consulta agendada para {paciente} em {consulta}"


# Classe que implementa os passos do BDD
class BDDSteps:
    def __init__(self):
        """Inicializa o contexto do BDD."""
        self.contexto = {}

    def dado_que_o_paciente_esta_logado(self, paciente: str):
        """Passo 'Dado': Simula que o paciente está logado."""
        self.contexto["paciente"] = paciente

    def quando_ele_agenda_uma_consulta_para(self, consulta: str):
        """Passo 'Quando': Simula o agendamento de uma consulta."""
        try:
            self.contexto["mensagem"] = agendar_consulta(self.contexto["paciente"], consulta)
        except ValueError as e:
            self.contexto["mensagem"] = str(e)

    def entao_a_consulta_deve_aparecer_na_agenda_com_a_mensagem(self, mensagem_esperada: str):
        """Passo 'Então': Verifica se a mensagem de agendamento está correta."""
        mensagem_obtida = self.contexto.get("mensagem", "")
        assert mensagem_obtida == mensagem_esperada, f"Erro: Esperado '{mensagem_esperada}', obtido '{mensagem_obtida}'"


# Função para executar um cenário de teste BDD válido
def executar_cenario_bdd():
    steps = BDDSteps()
    steps.dado_que_o_paciente_esta_logado("Robson Oliveira")
    steps.quando_ele_agenda_uma_consulta_para("2025-03-22 10:00")
    steps.entao_a_consulta_deve_aparecer_na_agenda_com_a_mensagem(
        "Consulta agendada para Robson Oliveira em 2025-03-22 10:00")
    print("✅ Cenário válido executado com sucesso!")


# Função para executar um cenário com data inválida
def executar_cenario_data_invalida():
    steps = BDDSteps()
    steps.dado_que_o_paciente_esta_logado("Maria Oliveira")
    steps.quando_ele_agenda_uma_consulta_para("22/03/2025 10:00")
    steps.entao_a_consulta_deve_aparecer_na_agenda_com_a_mensagem("Formato de data inválido. Use 'YYYY-MM-DD HH:MM'.")
    print("✅ Cenário com data inválida executado com sucesso!")


if __name__ == "__main__":
    executar_cenario_bdd()
    executar_cenario_data_invalida()
