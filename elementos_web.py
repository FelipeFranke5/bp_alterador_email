import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from validador import VariavelAmbiente


class BuscarClicarAlteradoEmailCheckout:
    def __init__(self, driver: Edge):
        self.driver = driver

    def clicar_acessar_ec(self):
        lista_links = WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, 'a'))
        )
        for link in lista_links:
            href = link.get_dom_attribute('href')
            if href:
                if 'MerchantDetails' in href:
                    link.click()
                    break

    def clicar_botao_editar(self):
        botao_editar = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@title="Editar dados cadastrais"]'))
        )
        botao_editar.click()

    def inserir_email1(self, email: str):
        campo_email1 = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.ID, 'Email'))
        )
        campo_email1.clear()
        campo_email1.send_keys(email)

    def inserir_email2(self, email: str):
        campo_email2 = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.ID, 'EmailConfirm'))
        )
        campo_email2.clear()
        campo_email2.send_keys(email)

    def selecionar_origem(self):
        dropdown_origem = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, 'Origin_chzn'))
        )
        dropdown_origem.click()
        email = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, 'Origin_chzn_o_5'))
        )
        email.click()

    def marcar_mesmos_dados_de_cadastro(self):
        checkbox = WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, 'input'))
        )[23]
        checkbox.click()

    def salvar_alteracao(self):
        botao_salvar = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, 'submit'))
        )
        botao_salvar.click()

    def obter_resultado(self):
        try:
            resultado = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, 'statusMessage'))
            )
        except TimeoutException:
            return 'Erro ao salvar.'
        if resultado.get_dom_attribute('class') == 'alert alert-success':
            return 'Sucesso.'
        return 'Erro ao salvar.'

    def enviar_boas_vindas(self):
        email_credenciamento = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, 'EmailCredenciamento'))
        )
        email_credenciamento.click()
        time.sleep(2)


class BuscarClicarNavegadorCheckout:
    def __init__(self, driver: Edge):
        self.driver = driver

    def clicar_botao_cielo(self):
        botao_cielo = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@id="cielo"]'))
        )
        botao_cielo.click()

    def clicar_botao_pesquisar_estabelecimentos(self):
        botao_pesquisar_estabelecimentos = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/CheckoutCielo/ListEstablishments"]'))
        )
        botao_pesquisar_estabelecimentos.click()

    def inserir_ec(self, ec: str):
        campo_ec = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.ID, 'AffiliationCode'))
        )
        campo_ec.clear()
        campo_ec.send_keys(ec)

    def limpar_data_inicial(self):
        data_inicial = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.ID, 'StartCreatedDate'))
        )
        data_inicial.clear()

    def clicar_botao_buscar(self):
        botao_buscar = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, 'buttonSearch'))
        )
        botao_buscar.click()


class BuscarClicarAutenticador:
    def __init__(self, driver: Edge):
        self.driver = driver

    def inserir_usuario(self, usuario: str):
        campo_usuario = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, 'param1'))
        )
        campo_usuario.clear()
        campo_usuario.send_keys(usuario)

    def inserir_senha(self, senha: str):
        campo_senha = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, 'param2'))
        )
        campo_senha.clear()
        campo_senha.send_keys(senha)

    def clicar_entrar(self):
        botao_entrar = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, 'enter'))
        )
        botao_entrar.click()


class BuscarClicarNavegadorEC:
    def __init__(self, driver: Edge):
        self.driver = driver

    def clicar_botao_cielo(self):
        botao_cielo = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@id="cielo"]'))
        )
        botao_cielo.click()

    def clicar_botao_pesquisar_estabelecimentos(self):
        botao_pesquisar_estabelecimentos = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/EcommerceCielo/List"]'))
        )
        botao_pesquisar_estabelecimentos.click()

    def inserir_ec(self, ec: str):
        campo_ec = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, 'EcNumber'))
        )
        campo_ec.clear()
        campo_ec.send_keys(ec)

    def limpar_data_inicio(self):
        dt_inicio = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, 'StartDate'))
        )
        dt_inicio.clear()

    def clicar_botao_buscar(self):
        botao_buscar = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, 'buttonSearch'))
        )
        botao_buscar.click()


class BuscarClicarAlteradorEmail:
    def __init__(self, driver: Edge):
        self.driver = driver

    def clicar_acessar_ec(self):
        detalhe_ec = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@title="Ver Detalhes"]'))
        )
        detalhe_ec.click()

    def clicar_botao_editar(self):
        lista_elementos_p = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_all_elements_located((By.TAG_NAME, 'p'))
        )
        merchant_id = lista_elementos_p[1].text.lower()
        editar = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, f'//a[@href="/EcommerceCielo/Edit/{merchant_id}"]'))
        )
        editar.click()

    def inserir_email(self, email: str):
        campo_email = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.ID, 'ContactEmail'))
        )
        campo_email.clear()
        campo_email.send_keys(email)

    def clicar_origem(self):
        menu = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, 'selectize-input'))
        )
        menu[0].click()
        origem_email = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@data-value="E-mail"]'))
        )
        origem_email.click()

    def marcar_mesmos_dados_de_cadastro(self):
        checkbox = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, 'UseRegisterDataForTechnicalContact'))
        )
        checkbox.click()

    def inserir_senha(self, var_ambiente: VariavelAmbiente):
        senha = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.ID, 'Password'))
        )
        senha.clear()
        senha.send_keys(var_ambiente.bp_pass)

    def clicar_botao_salvar(self):
        botao_salvar = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, 'buttonEdit'))
        )
        botao_salvar.click()

    def obter_resultado(self):
        resultado = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_all_elements_located((By.TAG_NAME, 'h3'))
        )
        return resultado[0].text

    def voltar_tela_cadastro(self):
        botao_x = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//a[@href="#"][@class="close"][@data-dismiss="modal"]')
            )
        )
        botao_x.click()
        time.sleep(2)

    def enviar_boas_vindas(self, senha: str):
        botao_tipo_notificacao = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, 'emailNotification-selectized'))
        )
        botao_tipo_notificacao.click()
        credenciamento_boas_vindas = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@data-value="13"]'))
        )
        credenciamento_boas_vindas.click()
        botao_enviar = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, 'buttonSendNotification'))
        )
        botao_enviar.click()
        campo_senha = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, 'Password'))
        )
        campo_senha.clear()
        campo_senha.send_keys(senha)
        botao_confirmar = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, 'btnConfirm'))
        )
        botao_confirmar.click()
        try:
            botao_x = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//a[@href="#"][@class="close"][@data-dismiss="modal"]')
                )
            )
        except TimeoutException:
            return
        botao_x.click()
        time.sleep(2)
