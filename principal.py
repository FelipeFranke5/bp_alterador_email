import json
import time
from typing import Literal

from selenium.common.exceptions import NoSuchElementException, TimeoutException

from automador import AlteraEmailAPI, AlteraEmailCheckout
from listagem import obter_lista_ecs


def obter_ec_email_solucao(ec: str):
    numero_ec = ec.split()[0]
    if len(numero_ec) != 10:
        raise ValueError('Um dos ECs está sendo enviado fora do padrão.')
    email = ec.split()[1]
    if '@' not in email:
        raise ValueError('O E-mail em uma das linhas do arquivo está mal-formatado.')
    solucao = ec.split()[2]
    if len(solucao) != 1:
        raise ValueError('A solução em uma das linhas do arquivo está mal-formatada.')
    return (numero_ec, email, solucao)


def case_api(
    solucao: Literal['API'],
    numero_ec: str,
    email: str,
    resultado_final: dict[str, dict[str, str]],
):
    automador = AlteraEmailAPI(numero_ec, email)
    automador.fazer_login()
    acesso_ec = automador.acessar_ec()
    match acesso_ec:
        case 'EC localizado!':
            resultado = automador.alterar_email()
            resultado_final[numero_ec] = {}
            resultado_final[numero_ec]['Email'] = email
            resultado_final[numero_ec]['Solucao'] = solucao
            resultado_final[numero_ec]['MensagemRetorno'] = resultado
        case 'EC não localizado!':
            resultado = 'EC nao localizado.'
            resultado_final[numero_ec] = {}
            resultado_final[numero_ec]['Email'] = email
            resultado_final[numero_ec]['Solucao'] = solucao
            resultado_final[numero_ec]['MensagemRetorno'] = resultado
        case 'Mais de 1 EC localizado ou erro inesperado!':
            resultado = 'Mais de 01 EC localizado ou erro inesperado.'
            resultado_final[numero_ec] = {}
            resultado_final[numero_ec]['Email'] = email
            resultado_final[numero_ec]['Solucao'] = solucao
            resultado_final[numero_ec]['MensagemRetorno'] = resultado
    return True


def case_checkout(
    solucao: Literal['Checkout'],
    numero_ec: str,
    email: str,
    resultado_final: dict[str, dict[str, str]],
):
    automador = AlteraEmailCheckout(numero_ec, email)
    automador.fazer_login()
    acesso_ec = automador.acessar_ec()
    match acesso_ec:
        case 'EC localizado!':
            resultado = automador.alterar_email()
            resultado_final[numero_ec] = {}
            resultado_final[numero_ec]['Email'] = email
            resultado_final[numero_ec]['Solucao'] = solucao
            resultado_final[numero_ec]['MensagemRetorno'] = resultado
        case 'EC não localizado!':
            resultado = 'EC nao localizado.'
            resultado_final[numero_ec] = {}
            resultado_final[numero_ec]['Email'] = email
            resultado_final[numero_ec]['Solucao'] = solucao
            resultado_final[numero_ec]['MensagemRetorno'] = resultado
        case 'Mais de 1 EC localizado ou erro inesperado!':
            resultado = 'Mais de 01 EC localizado ou erro inesperado.'
            resultado_final[numero_ec] = {}
            resultado_final[numero_ec]['Email'] = email
            resultado_final[numero_ec]['Solucao'] = solucao
            resultado_final[numero_ec]['MensagemRetorno'] = resultado
    return True


def obter_solucao(solucao_numero: str):
    match solucao_numero:
        case '0':
            solucao = 'API'
        case '1':
            solucao = 'Checkout'
        case _:
            solucao = 'N/A'
    return solucao


def executar_interacao(
    solucao: Literal['API', 'Checkout'],
    numero_ec: str,
    email: str,
    resultado_final: dict[str, dict[str, str]],
    finalizada: bool = False,
):
    erros = 0
    while not finalizada and erros <= 3:
        try:
            match solucao:
                case 'API':
                    finalizada = case_api(solucao, numero_ec, email, resultado_final)
                case 'Checkout':
                    finalizada = case_checkout(solucao, numero_ec, email, resultado_final)
        except (NoSuchElementException, TimeoutException):
            erros += 1
    if erros > 3:
        resultado = 'Timeout ou Erro no Admin.'
        resultado_final[numero_ec] = {}
        resultado_final[numero_ec]['Email'] = email
        resultado_final[numero_ec]['Solucao'] = solucao
        resultado_final[numero_ec]['MensagemRetorno'] = resultado
    return erros


def rodar_automacao(lista_ecs: list[str]):
    resultado_final: dict[str, dict[str, str]] = {}
    lista_deu_erro: list[bool] = []
    for ec in lista_ecs:
        interacao_finalizada = False
        ec_email_solucao = obter_ec_email_solucao(ec)
        numero_ec = ec_email_solucao[0]
        email = ec_email_solucao[1]
        solucao_numero = ec_email_solucao[2]
        solucao = obter_solucao(solucao_numero)
        print('\n- - - - D A D O S  D A  I N T E R A Ç Ã O  - - - -\n')
        print(f'-Número do EC: {numero_ec}')
        print(f'-E-mail: {email}')
        print(f'-Solução: {solucao}\n')
        print('- - - - F I M  D A D O S  D A  I N T E R A Ç Ã O  - - - -\n')
        if solucao == 'N/A':
            resultado = 'Solucao invalida.'
            resultado_final[numero_ec] = {}
            resultado_final[numero_ec]['Email'] = email
            resultado_final[numero_ec]['Solucao'] = solucao
            resultado_final[numero_ec]['MensagemRetorno'] = resultado
            continue
        erros = executar_interacao(solucao, numero_ec, email, resultado_final, interacao_finalizada)
        deu_erro = erros > 0
        lista_deu_erro.append(deu_erro)
    if any(lista_deu_erro):
        print('\n\nATENÇÃO: Uma ou mais falhas ocorreram na execução do script.')
        print('Portanto, será necessário rodar novamente.\n')
    with open('resultado.json', encoding='utf-8', mode='w') as arq:
        arq.write(json.dumps(resultado_final, indent=4))


def main():
    print('- - - - A U T O M A D O R   B R A S P A G   - - - -')
    print('- - - - I N I C I A L I Z A N D O . . .   - - - -')
    time.sleep(5)
    lista_ecs = obter_lista_ecs()
    if not lista_ecs:
        print('\nErro! Um dos dados obrigatórios da automação está faltando..')
        print('Verifique se o arquivo "lista_ec.txt"')
        print('esta presente no diretório e preenchido corretamente.\n')
        return
    for ec in lista_ecs:
        if len(ec.split()) != 3:
            print('\nErro! A lista está mal-formatada..')
            print('Verifique o padrão em uma das linhas do arquivo "lista_ec.txt".')
            print('Padrão correto: EC EMAIL SOLUCAO')
            return
    rodar_automacao(lista_ecs)
    print('\n- - - - T E R M I N A N D O . . .   - - - -')


if __name__ == '__main__':
    main()
