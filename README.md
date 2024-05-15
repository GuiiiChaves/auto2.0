# Automação do desafio RPA

Este é um script Python que automatiza o preenchimento de um formulário web no desafio RPA do site [rpachallenge.com](https://www.rpachallenge.com/). Ele realiza as seguintes etapas:

1. Abre o navegador Google Chrome.
2. Navega até a página do desafio RPA.
3. Baixa um arquivo Excel que contém informações de usuários.
4. Preenche um formulário web com essas informações.
5. Submete o formulário preenchido.

## Pré-requisitos

- Python 3.x instalado.
- Bibliotecas Python necessárias instaladas. Você pode instalar as dependências usando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt```


## CONFIGURAÇÃO DO AMBIENTE VIRTUAL:

Para isolar o ambiente e evitar conflitos de dependências, é recomendável criar um ambiente virtual. Você pode fazer isso executando os seguintes comandos:

```bash

python -m venv venv```

Em seguida, ative o ambiente virtual:

No Windows:

```bash

venv\Scripts\activate```


