import json
from _env import *
from text_parsers import ufpe


def parse_data(text):
    parser = 'ufpe'

    if parser == 'ufpe':
        return ufpe.text_parser_ufpe(text)
    else:
        return None


# Lendo os dados do arquivo de texto
with open('dados.txt', 'r', encoding='utf-8') as file:
    text_data = file.read()

# Convertendo os dados para JSON
json_data = parse_data(text_data)

# Salvando o JSON em um arquivo
with open('components.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)


# Imprimindo a quantidade de disciplinas por período
total = 0
for entry in json_data:
    period = entry["period"]
    num_components = len(entry["components"])
    total = total + num_components
    print(f"{period}: {num_components} disciplinas")

print("JSON criado com sucesso!", f'Total: {total}')
