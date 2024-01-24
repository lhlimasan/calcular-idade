def obter_ano_de_nascimento():
    while True:
        try:
            ano = int(input("Digite o ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano <= 2021:
                return ano
            else:
                print("Por favor, digite um ano entre 1922 e 2021.")
        except ValueError:
            print("Erro: Por favor, digite um número válido.")

def calcular_idade(ano_nascimento):
    ano_atual = datetime.date.today().year
    idade = ano_atual - ano_nascimento
    return idade

nome_completo = input("Digite seu nome completo: ")
ano_nascimento = obter_ano_de_nascimento()
idade = 2022 - ano_nascimento

print(f"Olá, {nome_completo}! Em 2022, você completou ou completará {idade} anos de idade.")
