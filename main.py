from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from settings import URL_CONSULT, RESULT_FILE
from utils.extract_data import extract_data
from pages.ConsultPage import ConsultPage
from pages.ProcessPage import ProcessPage
from selenium import webdriver
from settings import logger
import json

process_number = "1027408-36.2018.4.01.3400"

def main() -> None:
    try:

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )

        driver.get(URL_CONSULT)

        consult_page = ConsultPage(driver)
        process_page = ProcessPage(driver)

        consult_process = consult_page.consult_process(process_number)
        if consult_process.get('error'):
            return None

        link_detail_process = consult_process.get('data')
        driver.get(link_detail_process)

        extract_html_process = process_page.extract_html_process()
        if extract_html_process.get('error'):
            return None
    
        html_process = extract_html_process.get("data")
        data_process = extract_data(html_process)

        with open(RESULT_FILE, mode="w", encoding="utf8") as file:
            json.dump(data_process, file, ensure_ascii=False, indent=4)

    except Exception as e:
        logger.error(f"Erro inesperado: {e}")

    finally:
        driver.quit()


if __name__ == '__main__':
    main()
