# AutoMatriculas

O AutoMatriculas é uma ferramenta desenvolvida para facilitar a inserção de disciplinas no Portal do Bolsista (PE no Campus). Este projeto automatiza o processo de adição de disciplinas ao portal, simplificando o processo e economizando tempo.

## Requisitos

Python

## Instalação

Clone o repositório:
```sh
git clone https://github.com/SrDouglax/AutoMatriculas.git
```

Instale as dependências:
```sh
pip install -r requirements.txt
```

## Execução

### Preparar Dados:

Copie os dados do PDF com as disciplinas da sua faculdade para o arquivo `dados.txt`. O texto copiado deve estar em um formato compatível com um dos parsers disponíveis.
[Default data copied](https://3e6095a2-8551-4827-8588-755f3377dd2f.filesusr.com/ugd/01d816_69be6ef675ac47abbf2445f893d06bb9.pdf)

### Converter Texto para JSON:

Em helpers, execute o script `text_to_json.py` para converter o texto em um arquivo JSON. Altere o parser se necessário. [Result](https://github.com/SrDouglax/AutoMatriculas/blob/main/components.json)
```sh
python helpers/text_to_json.py
```

### Adicionar Disciplinas ao Portal:

Execute o script `main.py` para adicionar as disciplinas no portal do bolista. Após iniciar o script, vá para a página e aguarde a conclusão do processo. Ajuste a posição dos botões no início do código. Para obter as coordenadas, utilize o script `get_cord.py` na pasta helpers.
```sh
python main.py
```

### Excluir Disciplinas:

Para uma forma rápida de deletar as disciplinas, execute o script `delete.py`.
```sh
python delete.py
```

### Testar o Parser:

Vá para o parser em uso, copie o regex e verifique se está funcionando corretamente com seus dados. Teste usando a ferramenta [regex101](https://regex101.com).

### Modificar Dados:

Para excluir algum período ou disciplina, basta removê-los do arquivo `components.json`.

### Checar dados:

Após a execução do arquivo `main.py`, você pode verificar a aplicação dos componentes. Para isso, copie e cole uma lista com os IDs das disciplinas no arquivo `data_to_check.txt`, colocando cada ID em uma linha separada. Se algum ID do `components.json` não estiver presente nesta lista, ele será exibido no console ao executar o arquivo `checker.py` da pasta helpers. 

## Notas Adicionais

Certifique-se de que todas as coordenadas dos botões estejam corretas. Use o script `get_cord.py` para determinar as coordenadas exatas na sua tela.
