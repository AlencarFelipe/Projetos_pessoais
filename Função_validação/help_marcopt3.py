# Função para validar jogos no banco de dados
def validar_jogos(numeros):
    # Validação e conversão da entrada
    try:
        numeros = tuple(map(int, numeros.split(',')))
    except ValueError:
        print("Erro: Certifique-se de inserir números separados por vírgula.")
        return False

    # Verifica se a tupla tem exatamente 6 elementos
    if len(numeros) != 6:
        print("Erro: Certifique-se de inserir exatamente 6 números.")
        return False

    # Conectar ao banco de dados
    conexao = sqlite3.connect('jogos.db')
    cursor = conexao.cursor()

    # Consultar o banco de dados para verificar os dados
    cursor.execute('''
        SELECT * FROM jogos 
        WHERE numero1 = ? AND numero2 = ? AND numero3 = ? AND numero4 = ? AND numero5 = ? AND numero6 = ?
    ''', numeros)
    
    resultado = cursor.fetchone()

    # Fechar a conexão com o banco de dados
    conexao.close()

    # Verificar o resultado da consulta
    if resultado:
        return True  # Dados válidos
    else:
        return False  # Dados inválidos

# Exemplo de uso
numeros_a_validar = input("Digite os números do jogo para validar (EX: 01, 02, 03, 04, 05, 06): ")

if validar_jogos(numeros_a_validar):
    print("Os números já existem no banco de dados.")
else:
    print("Os números são válidos e podem ser adicionados.")