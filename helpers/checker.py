import json

# Período específico; ajuste conforme necessário
period_name = '1º'  # Ou defina como "1º" para o primeiro período por exemplo.

def load_json(file_path):
    """Carrega dados de um arquivo JSON."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def parse_text(text):
    """Extrai disciplinas do texto fornecido."""
    lines = text.strip().split('\n')
    components = set()
    for line in lines:
        if line.strip():
            code = line.split()[0]
            components.add(code.strip())
    return components

def find_missing_components(json_data, period_name, text_components):
    """Encontra componentes no JSON para um período específico ou todos os períodos que não estão no texto."""
    missing_components = []

    for entry in json_data:
        if period_name is None or entry["period"] == period_name:
            for component in entry["components"]:
                code = component["code"]
                if code not in text_components:
                    missing_components.append(component)

    return missing_components

if __name__ == "__main__":
    # Caminho para o arquivo JSON
    json_file_path = 'components.json'

    # Texto de exemplo
    with open('data_to_check.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    # Carregar dados JSON
    json_data = load_json(json_file_path)

    # Extrair componentes do texto
    text_components = parse_text(text)

    # Encontrar componentes ausentes para o período especificado ou todos os períodos
    missing_components = find_missing_components(
        json_data, period_name, text_components)

    if missing_components:
        if period_name is None:
            print("Componentes ausentes no texto para todos os períodos:")
        else:
            print(f"Componentes para o período '{period_name}' encontrados no JSON, mas ausentes no texto:")
        for component in missing_components:
            print(f"Código: {component['code']}, Nome: {component['name']}")
    else:
        if period_name is None:
            print("Todos os componentes em todos os períodos estão presentes no texto.")
        else:
            print(f"Todos os componentes do período '{period_name}' estão presentes no texto.")
