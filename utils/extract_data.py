from utils.utils import remove_whitespaces, slugify_text
from bs4 import BeautifulSoup


def extract_data(html: str) -> dict:

    parser = BeautifulSoup(html, "html.parser")
    tab_mov = parser.find("table", {"id": "tab_mov"})
    tab_proc = parser.find("table", {"id": "tab_proc"})

    itens_mov = tab_mov.find_all("tr")
    itens_proc = tab_proc.find_all("tr")

    data_proc = {}
    description = None
    for item in itens_proc:
        tds = item.select('td')

        value = tds[-1].get_text(strip=True)

        if tds[0].get_text(strip=True) != "":
            description = tds[0].get_text(strip=True)
        
        description = slugify_text(description)

        if data_proc.get(description) is None:
            data_proc[description] = []
        
        data_proc[description].append(value)

    for key in data_proc:
        data_proc[key] = ", ".join(data_proc[key])

    movimentations = []
    for item in itens_mov[1:]:
        values = item.select("td", {"class": "detalhamento_label_valor"})
        description = values[0].get_text(strip=True)
        movimentation = values[-1].get_text(strip=True)
        
        movimentations.append({
            "date": remove_whitespaces(description),
            "movimentation": movimentation
        })

    data_proc["movimentations"] = movimentations
    
    return data_proc
