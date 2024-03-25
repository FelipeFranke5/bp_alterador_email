from selenium import webdriver

from elementos_web import (BuscarClicarAlteradoEmailCheckout,
                           BuscarClicarAlteradorEmail,
                           BuscarClicarAutenticador,
                           BuscarClicarNavegadorCheckout,
                           BuscarClicarNavegadorEC)
from validador import (ValidadorAlteraEmailAPI, ValidadorAlteraEmailCheckout,
                       VariavelAmbiente)


class AlteraEmailCheckout:
    def __init__(self, ec: str, email: str):
        self.var_ambiente = VariavelAmbiente()
        self.ec = ec
        self.email = email
        self.options = webdriver.EdgeOptions()
        self.options.add_argument('--start-maximized')
        self.driver = webdriver.Edge(options=self.options)

    def fazer_login(self):
        self.driver.get(self.var_ambiente.bp_login_pg)
        autenticador = BuscarClicarAutenticador(self.driver)
        autenticador.inserir_usuario(self.var_ambiente.bp_login)
        autenticador.inserir_senha(self.var_ambiente.bp_pass)
        autenticador.clicar_entrar()

    def acessar_ec(self):
        navegador = BuscarClicarNavegadorCheckout(self.driver)
        validador = ValidadorAlteraEmailCheckout(self.driver)
        navegador.clicar_botao_cielo()
        navegador.clicar_botao_pesquisar_estabelecimentos()
        self.driver.switch_to.window(self.driver.window_handles[1])
        navegador.inserir_ec(self.ec)
        navegador.limpar_data_inicial()
        navegador.clicar_botao_buscar()
        resultado = validador.encontrar_resultados_busca()
        match resultado:
            case 0:
                resultado_acesso = 'EC não localizado!'
                return resultado_acesso
            case 1:
                resultado_acesso = 'EC localizado!'
                return resultado_acesso
            case _:
                resultado_acesso = 'Mais de 1 EC localizado ou erro inesperado!'
                return resultado_acesso

    def alterar_email(self):
        automador = BuscarClicarAlteradoEmailCheckout(self.driver)
        automador.clicar_acessar_ec()
        automador.clicar_botao_editar()
        automador.inserir_email1(self.email)
        automador.inserir_email2(self.email)
        automador.selecionar_origem()
        automador.marcar_mesmos_dados_de_cadastro()
        automador.salvar_alteracao()
        resultado_alteracao = automador.obter_resultado()
        if resultado_alteracao == 'Sucesso.':
            automador.enviar_boas_vindas()
        return resultado_alteracao


class AlteraEmailAPI:
    def __init__(self, ec: str, email: str):
        self.var_ambiente = VariavelAmbiente()
        self.ec = ec
        self.email = email
        self.options = webdriver.EdgeOptions()
        self.options.add_argument('--start-maximized')
        self.driver = webdriver.Edge(options=self.options)

    def fazer_login(self):
        self.driver.get(self.var_ambiente.bp_login_pg)
        autenticador = BuscarClicarAutenticador(self.driver)
        autenticador.inserir_usuario(self.var_ambiente.bp_login)
        autenticador.inserir_senha(self.var_ambiente.bp_pass)
        autenticador.clicar_entrar()

    def acessar_ec(self):
        navegador = BuscarClicarNavegadorEC(self.driver)
        validador = ValidadorAlteraEmailAPI(self.driver)
        resultado_acesso = ''
        navegador.clicar_botao_cielo()
        navegador.clicar_botao_pesquisar_estabelecimentos()
        navegador.inserir_ec(self.ec)
        navegador.limpar_data_inicio()
        navegador.clicar_botao_buscar()
        resultado = validador.encontrar_resultados_busca()
        match resultado:
            case 0:
                resultado_acesso = 'EC não localizado!'
                return resultado_acesso
            case 1:
                resultado_acesso = 'EC localizado!'
                return resultado_acesso
            case _:
                resultado_acesso = 'Mais de 1 EC localizado ou erro inesperado!'
                return resultado_acesso

    def alterar_email(self):
        automador = BuscarClicarAlteradorEmail(self.driver)
        automador.clicar_acessar_ec()
        automador.clicar_botao_editar()
        automador.inserir_email(self.email)
        automador.clicar_origem()
        automador.marcar_mesmos_dados_de_cadastro()
        automador.inserir_senha(self.var_ambiente)
        automador.clicar_botao_salvar()
        resultado_alteracao = automador.obter_resultado()
        if 'sucesso' in resultado_alteracao:
            automador.voltar_tela_cadastro()
            automador.enviar_boas_vindas(self.var_ambiente.bp_pass)
        return resultado_alteracao
