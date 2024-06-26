# Simulação de Abertura de Conta Bancária

Este projeto é uma aplicação web interativa desenvolvida em Python usando Streamlit para simular o processo de abertura de uma conta bancária. O objetivo é fornecer uma interface amigável onde os usuários podem inserir suas informações pessoais e, com base nesses dados, determinar se a conta pode ser aprovada.

## Funcionalidades

- Entrada de dados do usuário:
  - Idade
  - Tempo de emprego (em meses)
  - Quantidade de pessoas na residência

- Classificação de crédito:
  - Predição se o usuário receberá crédito baseado em um modelo preditivo treinado.
  - Exibição do resultado da predição na interface.

## Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [scikit-learn](https://scikit-learn.org/stable/)
- [pandas](https://pandas.pydata.org/)
- [imbalanced-learn (SMOTE)](https://imbalanced-learn.org/stable/)

## Como Executar o Projeto

### Pré-requisitos

- Python 3.7 ou superior
- Pip (gerenciador de pacotes do Python)

### Instalação

1. Clone o repositório para sua máquina local:

```sh
git clone https://github.com/shadyrajab/abertura-conta-bancaria.git
cd abertura-conta-bancaria
```

2. Crie um ambiente virtual:
```sh
python -m venv venv
```
3. Instale as dependências:
```sh
pip install -r requirements.txt
```

# Executando a Aplicação
```sh
streamlit run Abertura.py
```

# Construção do Modelo Preditivo

O modelo preditivo utilizado na aplicação foi construído no notebook Criando o Modelo.ipynb. Fique a vontade para ler o notebook e entender todo o processo!

Para testar a funcionalidade de predição dos dados, um arquivo de teste model_scoring.ftr foi disponibilizado na pasta test/. Esse arquivo pode ser utilizado para verificar a precisão da predição do modelo antes de aplicá-lo a novos dados.


Você também pode acessar o projeto e fazer um teste através deste link: https://abertura-conta-bancaria.streamlit.app/

[streamlit-Abertura-2024-06-05-17-06-00.webm](https://github.com/shadyrajab/projeto-final-ebac/assets/65933264/887cb654-dc6a-47b4-97f7-be2a7650e9e7)
