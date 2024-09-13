from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from locators.ConsultPageLocators import Locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from typing import Dict, Any
from settings import logger


class ConsultPage:
    def __init__(self, driver: WebDriver):
        self.locators = Locators()
        self.driver = driver

    def consult_process(self, number_process: str) -> Dict[str, Any]:
        """
        Consult process number

        Args:
            :param number_process: Number of the process to be consulted

        Returns:
            dict: A dictionary containing the result. The dictionary has the following keys: # noqa E501
                - 'error' (bool): Indicates if an error occurred during the process.
                - 'message' (str): A message associated with the result.
                - 'data' (any): Additional data related to the result.
        """
        try:
            input_process = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.locators.input_process)) # noqa E501
            )

            input_process.send_keys(number_process)
            input_process.send_keys(Keys.ENTER)

            try:
                link_detail_process = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, self.locators.links_process)) # noqa E501
                )
            except TimeoutException:
                logger.error(f'Processo "{number_process}" não encontrado')
                return {
                    'error': True,
                    'message': f'Processo "{number_process}" não encontrado',
                    'data': None,
                }

            link_detail_process = link_detail_process.get_attribute('href')

        except Exception as e:
            logger.error(f'Erro ao pesquisar processo "{number_process}": {e}')
            return {
                'error': True,
                'message': f'Erro ao pesquisar processo "{number_process}"',
                'data': None,
            }

        return {
            'error': False,
            'message': 'Processo pesquisado com sucesso',
            'data': link_detail_process,
        }
