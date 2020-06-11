from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith acessa a página inicial e acidentalmente tenta submeter
        # um item vazio na lista. Ela tecla enter na caixa de entrada vazia
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        # A página inicial é atualizada e há uma mensagem de erro informando
        # que itens na lista não podem estar em branco
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            'Você não pode ter um item vazio em uma lista'
        ))

        # Ela tenta novamente com umtexto para o item, e isso agora funciona
        self.browser.find_element_by_id('id_new_item').send_keys('Comprar leite')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Comprar leite')

        # De forma perversa, ela agora decide submeter um segundo item em
        # branco na lista
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        # Ela recebe um avio semelhante na página da lista
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            'Você não pode ter um item vazio em uma lista'
        ))

        # E la pode corrigir isso preenchendo o item com um texto
        self.browser.find_element_by_id('id_new_item').send_keys('Fazer chá')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Comprar leite')
        self.wait_for_row_in_list_table('2: Fazer chá')
