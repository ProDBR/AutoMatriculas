import re

regex = r'([A-Z0-9]+)-\s([A-ZÀ-Ú0-9\s\n-:]+)\s*(OBRIG|OPT|ELETIVO)\s*(\d+)\s*(\d+)\s*(\d+)\s*([\d.]+)\s*'


def text_parser_ufpe(text):
    """
    Parses a text containing information about academic courses and returns a list of dictionaries, where each dictionary represents a period and its associated course components.

    The function expects the text to be formatted in a specific way, with sections separated by "PERÍODO:" or "SEM PERIODIZAÇÃO" headers, and each course component formatted as:
    [CODE] - [NAME] [TYPE] [CH TEÓRICA] [CH PRÁTICA] [CH TOTAL] [CRÉDITOS]

    The function returns a list of dictionaries, where each dictionary has two keys:
    - "period": the name of the period, either a number followed by "º" or "SEM PERIODIZAÇÃO"
    - "components": a list of dictionaries, where each dictionary has two keys:
        - "code": the code of the course component
        - "name": the name of the course component

    The function uses regular expressions to parse the text and extract the relevant information.
    """

    data = {}

    # Dividindo o texto em seções por "PERÍODO:" ou "SEM PERIODIZAÇÃO"
    periods = re.split(r'\n(?=PERÍODO:|\bSEM PERIODIZAÇÃO\b)', text.strip())

    for period in periods:
        # Verifica se é um período específico ou "SEM PERIODIZAÇÃO"
        period_match = re.search(r'PERÍODO:\s*(\d+º)|SEM PERIODIZAÇÃO', period)

        if period_match:
            # Define o nome do período
            period_name = period_match.group(
                1) if period_match.group(1) else "SEM PERIODIZAÇÃO"

            # Inicializa a lista de componentes para o período, se necessário
            if period_name not in data:
                data[period_name] = []

            # Regex para capturar o formato desejado e extrair apenas ID e Nome
            component_pattern = re.compile(regex)

            # Percorre todas as correspondências e extrai código e nome
            for match in component_pattern.finditer(period):
                code = match.group(1).strip()
                name = match.group(2).strip()

                component = {
                    "code": code,
                    "name": name
                }
                data[period_name].append(component)

    # Convertendo o dicionário para a lista de dicionários desejada
    result = [{"period": period, "components": components}
              for period, components in data.items()]

    return result
