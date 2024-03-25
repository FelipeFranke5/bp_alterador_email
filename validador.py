from dotenv import dotenv_values
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class VariavelAmbiente:
    bp_login: str
    bp_pass: str
    bp_login_pg: str
    bp_home_pg: str
    bp_api30_pg: str
    bp_checkout_pg: str
    bp_login_title: str
    bp_home_title: str

    def __init__(self):
        self.validar_tudo()

    def validar_tudo(self):
        self.validar_bp_login()
        self.validar_bp_pass()
        self.validar_bp_login_pg()
        self.validar_bp_home_pg()
        self.validar_bp_api30_pg()
        self.validar_bp_checkout_pg()
        self.validar_bp_login_title()
        self.validar_bp_home_title()

    def validar_bp_login(self):
        bp_login_var = dotenv_values('.env').get('BP_LOGIN')
        if not bp_login_var:
            raise ValueError('BP_LOGIN é obrigatório.')
        self.bp_login = bp_login_var

    def validar_bp_pass(self):
        bp_pass_var = dotenv_values('.env').get('BP_PASS')
        if not bp_pass_var:
            raise ValueError('BP_PASS é obrigatório.')
        self.bp_pass = bp_pass_var

    def validar_bp_login_pg(self):
        bp_login_page_var = dotenv_values('.env').get('BP_LOGIN_PG')
        if not bp_login_page_var:
            raise ValueError('BP_LOGIN_PG é obrigatório.')
        self.bp_login_pg = bp_login_page_var

    def validar_bp_home_pg(self):
        bp_home_pg_var = dotenv_values('.env').get('BP_HOME_PG')
        if not bp_home_pg_var:
            raise ValueError('BP_HOME_PG é obrigatório.')
        self.bp_home_pg = bp_home_pg_var

    def validar_bp_api30_pg(self):
        bp_api30_pg_var = dotenv_values('.env').get('BP_API30_PG')
        if not bp_api30_pg_var:
            raise ValueError('BP_API30_PG é obrigatório.')
        self.bp_api30_pg = bp_api30_pg_var

    def validar_bp_checkout_pg(self):
        bp_checkout_pg_var = dotenv_values('.env').get('BP_CHECKOUT_PG')
        if not bp_checkout_pg_var:
            raise ValueError('BP_CHECKOUT_PG é obrigatório.')
        self.bp_checkout_pg = bp_checkout_pg_var

    def validar_bp_login_title(self):
        bp_login_title_var = dotenv_values('.env').get('BP_LOGIN_TITLE')
        if not bp_login_title_var:
            raise ValueError('BP_LOGIN_TITLE é obrigatório.')
        self.bp_login_title = bp_login_title_var

    def validar_bp_home_title(self):
        bp_home_title_var = dotenv_values('.env').get('BP_HOME_TITLE')
        if not bp_home_title_var:
            raise ValueError('BP_HOME_TITLE é obrigatorio.')
        self.bp_home_title = bp_home_title_var


class ValidadorAlteraEmailAPI:
    def __init__(self, driver: Edge):
        self.driver = driver

    def encontrar_resultados_busca(self):
        busca = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="adm-title"]'))
        )
        try:
            resultado = int(busca.text.split()[3])
        except ValueError:
            return 0
        else:
            return resultado


class ValidadorAlteraEmailCheckout:
    def __init__(self, driver: Edge):
        self.driver = driver

    def encontrar_resultados_busca(self):
        busca = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, '//th[@class="title"]'))
        )
        try:
            resultado = int(busca.text.split()[3])
        except ValueError:
            return 0
        else:
            return resultado
