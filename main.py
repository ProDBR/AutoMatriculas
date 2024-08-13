import json
import time
import pyautogui
import pyperclip

# Configurações
PERIOD_SELECT_COORDS = (1091, 406)
TEXT_FIELD1_COORDS = (221, 406)
TEXT_FIELD2_COORDS = (797, 406)
INSERT_BUTTON_COORDS = (1100, 472)


def load_json(file_path):
    """Carrega dados de um arquivo JSON."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def select_period(period_name):
    """Seleciona um período no menu suspenso com base no nome do período."""
    # Clique no menu suspenso
    pyautogui.click(PERIOD_SELECT_COORDS)
    time.sleep(0.1)  # Aguarde o menu suspenso aparecer

    if period_name == "SEM PERIODIZAÇÃO":
        # Seleciona a opção "SEM PERIODIZAÇÃO"
        pyautogui.press('down')
        time.sleep(0.5)  # Aguarde o menu se ajustar
        pyautogui.press('enter')
    else:
        # Trata períodos numéricos
        period_number = int(period_name.replace('º', '').strip())
        for _ in range(period_number + 1):
            pyautogui.press('down')
            time.sleep(0.1)  # Aguarde o menu se ajustar
        pyautogui.press('enter')

    time.sleep(0.5)  # Aguarde a seleção ser aplicada


def input_data(data):
    """Preenche os campos com os dados fornecidos e insere as informações."""
    for entry in data:
        period = entry["period"]
        components = entry["components"]

        for component in components:
            select_period(period)
            code = component["code"]
            name = component["name"]

            # Preencher os campos de texto usando pyperclip
            pyautogui.click(TEXT_FIELD1_COORDS)
            pyperclip.copy(code)
            pyautogui.hotkey('ctrl', 'v')

            pyautogui.click(TEXT_FIELD2_COORDS)
            pyperclip.copy(name)
            pyautogui.hotkey('ctrl', 'v')

            # Clicar no botão para inserir
            pyautogui.click(INSERT_BUTTON_COORDS)
            time.sleep(1)  # Aguarde o processamento

            # Confirmar a inserção
            pyautogui.press('enter')
            time.sleep(3)  # Aguarde a confirmação e o recarregamento da página


if __name__ == "__main__":
    time.sleep(2)  # Aguardar para garantir que a janela esteja pronta

    # Carregar dados do JSON e iniciar o processo de inserção
    json_data = load_json('components.json')
    input_data(json_data)
