class ErroArquivoAutomacao:
    pass


def obter_lista_ecs():
    try:
        with open('lista_ec.txt', encoding='utf-8') as arq:
            lista_ecs = arq.read().splitlines()
    except FileNotFoundError:
        return ['']
    return lista_ecs
