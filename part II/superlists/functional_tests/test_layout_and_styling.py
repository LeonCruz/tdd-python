from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys


class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        # Edith acessa a página inicial
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 786)

        # Ela percebe que a caixa de entrada está elegantemente centralizada
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

        # Ela inicia uma nova lista e vê que a entrada está elegantemente
        # centralizada também
        inputbox.send_keys('testando')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: testando')
        inputbox = self.browser.find_element_by_id('id_new_item')

        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )
