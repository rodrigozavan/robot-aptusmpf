from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from locators.ProcessPageLocators import Locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from typing import Dict, Any
from settings import logger


class ProcessPage:
    def __init__(self, driver: WebDriver):
        self.locators = Locators()
        self.driver = driver

    def extract_html_process(self) -> Dict[str, Any]:
        """
        Extract the html from the page
        
        Args:
            :param

        Returns:
            dict: A dictionary containing the result. The dictionary has the following keys: # noqa E501
                - 'error' (bool): Indicates if an error occurred during the process.
                - 'message' (str): A message associated with the result.
                - 'data' (any): Additional data related to the result.
        """
        try:

            try:
                html_process = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, self.locators.html_process)) # noqa E501
                )
            except TimeoutException:
                return {
                    'error': True,
                    'message': f'Dados do processo não encontrados',
                    'data': None,
                }
        
            html_process = html_process.get_attribute('innerHTML')

        except Exception as e:
            logger.error(f'Erro ao extrair html: {e}')
            return {
                'error': True,
                'message': f'Erro ao extrair html',
                'data': None,
            }

        return {
            'error': False,
            'message': 'HTML extraido com sucesso',
            'data': html_process,
        }
