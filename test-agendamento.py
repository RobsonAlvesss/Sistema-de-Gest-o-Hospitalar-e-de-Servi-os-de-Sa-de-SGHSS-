import unittest
from datetime import datetime


# Implementação do método agendarConsulta
def agendarConsulta(paciente, consulta):
    # Valida o formato da data
    try:
        datetime.strptime(consulta, "%Y-%m-%d %H:%M")
    except ValueError:
        raise ValueError("Formato de data inválido. Use 'YYYY-MM-DD HH:MM'.")

    # Retorna a mensagem de confirmação
    return f"Consulta agendada para {paciente} em {consulta}"


# Classe de teste para o método agendarConsulta
class TestAgendamento(unittest.TestCase):
    def test_agendarConsulta(self):
        # Teste com dados válidos
        paciente = "Robson Oliveira"
        consulta = "2025-03-22 10:00"
        resultado = agendarConsulta(paciente, consulta)
        self.assertEqual(resultado, "Consulta agendada para Robson Oliveira em 2025-03-22 10:00")

    def test_agendarConsulta_data_invalida(self):
        # Teste com data inválida
        paciente = "Robson Oliveira"
        consulta = "22/03/2025 10:00"  # Formato inválido
        with self.assertRaises(ValueError):
            agendarConsulta(paciente, consulta)


# Executa os testes
if __name__ == "__main__":
    unittest.main()
