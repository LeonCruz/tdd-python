from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from unittest import skip


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith acessa a página inicial e acidentalmente tenta submeter
        # um item vazio na lista. Ela tecla enter na caixa de entrada vazia

        # A página inicial é atualizada e há uma mensagem de erro informando
        # que itens na lista não podem estar em branco

        # Ela tenta novamente com umtexto para o item, e isso agora funciona

        # De forma perversa, ela agora decide submeter um segundo item em
        # branco na lista

        # Ela recebe um avio semelhante na página da lista

        # E la pode corrigir isso preenchendo o item com um texto
        self.fail('write me!')
