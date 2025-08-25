## ENTRA DAS NOTAS DO ALUNO
def ALUNO_NOTAS():
    notas = []
    while True:
        try:
            ## AO DIGITA A NOTA, O VALOR ENTRAR NO ARRAY
            nota = float(input("Digite a nota do aluno (ou '-9' para encerrar): ")) ## CONVERSÃO FEITA PARA TIPO FLOAT.
            if nota == -9:
                break
            if 0 <= nota <= 10:
                ## APPEND DAS NOTAS EM UM NOVO ARRAY
                notas.append(nota)
            else:
                print("Nota Invalida, digite algo entre 0 e 1.")
        except ValueError:
            print("Entrada Invalida, digite apenas números.")
    return notas

# CALCULO DA MÉDIA DO ALUNO
def MEDIA(notas):
    ## TAMANHO DO ARRAY
    if len(notas) == 0:
        return 0
        ## SOMA DA MÉDIA // TOMA TODOS OS VALORES DENTRO DO ARRAY DIVIDIDOS PELA QUANTIDADE DE ITENS NO ARRAY.
    return sum(notas) / len(notas)


# SITUACAO DO ALUNO (APROVADO OU REPROVADO)
def SITUACAO(media):
    if media >= 7: ## ACIMA OU IGUAL A 7 (APROVADO)
        return "Aprovado"
    else:
        return "Reprovado"


## PRINT FINAL DE UM RELATÓRIO BREVE
def RELATORIO(notas, media, situacao):
    print("###### MÉDIA FINAL ###")
    print(f"Notas do Aluno: {notas}")
    print(f"Média do Aluno: {media:.2f}")
    print(f"Situação Final: {situacao}")
    print("###### MÉDIA FINAL ###")


## EXECUÇÃO DAS FUNÇÕES 
notas_aluno    = ALUNO_NOTAS()
media_aluno    = MEDIA(notas_aluno)
situacao_aluno = SITUACAO(media_aluno)
RELATORIO(notas_aluno, media_aluno, situacao_aluno)
## EXECUÇÃO DAS FUNÇÕES 
