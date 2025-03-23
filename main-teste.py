# Simulação do Sistema de Gestão Hospitalar e de Serviços de Saúde (SGHSS)

# Dados iniciais
pacientes = []
consultas = []
prontuarios = {}

# Função para cadastrar pacientes
def cadastrar_paciente(nome, cpf, telefone):
    if any(paciente['cpf'] == cpf for paciente in pacientes):
        return "Erro: Paciente já cadastrado."
    paciente = {'nome': nome, 'cpf': cpf, 'telefone': telefone}
    pacientes.append(paciente)
    return "Paciente cadastrado com sucesso."

# Função para agendar consultas
def agendar_consulta(cpf_paciente, data, hora, medico):
    paciente = next((p for p in pacientes if p['cpf'] == cpf_paciente), None)
    if not paciente:
        return "Erro: Paciente não encontrado."
    consulta = {'cpf_paciente': cpf_paciente, 'data': data, 'hora': hora, 'medico': medico}
    consultas.append(consulta)
    return "Consulta agendada com sucesso."


# Função para acessar prontuários
def acessar_prontuario(cpf_paciente):
    if cpf_paciente not in prontuarios:
        return "Erro: Prontuário não encontrado."
    return prontuarios[cpf_paciente]


# Função para adicionar informações ao prontuário
def adicionar_info_prontuario(cpf_paciente, info):
    if cpf_paciente not in prontuarios:
        prontuarios[cpf_paciente] = []
    prontuarios[cpf_paciente].append(info)
    return "Informação adicionada ao prontuário."


# Testes Funcionais

# Teste 1: Cadastro de Paciente
print("Teste 1 - Cadastro de Paciente:")
resultado = cadastrar_paciente("Robson Oiveira", "123.456.789-00", "82982127804")
print(resultado)  # Saída esperada: "Paciente cadastrado com sucesso."

# Teste 2: Tentar cadastrar o mesmo paciente novamente
print("\nTeste 2 - Tentar cadastrar o mesmo paciente:")
resultado = cadastrar_paciente("Robson Oiveira", "123.456.789-00", "82982127804")
print(resultado)  # Saída esperada: "Erro: Paciente já cadastrado."

# Teste 3: Agendar Consulta
print("\nTeste 3 - Agendar Consulta:")
resultado = agendar_consulta("123.456.789-00", "2025-03-21", "14:00", "Dr. Ramildo")
print(resultado)  # Saída esperada: "Consulta agendada com sucesso."

# Teste 4: Tentar agendar consulta para paciente não cadastrado
print("\nTeste 4 - Agendar Consulta para paciente não cadastrado:")
resultado = agendar_consulta("000.000.000-00", "2025-03-21", "14:00", "Dr. Ramildo")
print(resultado)  # Saída esperada: "Erro: Paciente não encontrado."

# Teste 5: Adicionar informação ao prontuário
print("\nTeste 5 - Adicionar informação ao prontuário:")
resultado = adicionar_info_prontuario("123.456.789-00", "Pressão arterial: 12x8")
print(resultado)  # Saída esperada: "Informação adicionada ao prontuário."

# Teste 6: Acessar prontuário
print("\nTeste 6 - Acessar prontuário:")
resultado = acessar_prontuario("123.456.789-00")
print(resultado)  # Saída esperada: ["Pressão arterial: 12x8"]

# Teste 7: Acessar prontuário de paciente não cadastrado
print("\nTeste 7 - Acessar prontuário de paciente não cadastrado:")
resultado = acessar_prontuario("000.000.000-00")
print(resultado)  # Saída esperada: "Erro: Prontuário não encontrado."
