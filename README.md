# Análise de Dados — E-commerce Olist

Projeto de análise exploratória de dados desenvolvido em Python a partir do Brazilian E-Commerce Public Dataset by Olist. O objetivo é transformar dados transacionais em insights sobre desempenho comercial, produtos, pagamentos, distribuição geográfica, logística e experiência dos clientes.

## Objetivo

Investigar o desempenho de um e-commerce brasileiro por meio da integração e análise de diferentes bases de dados, apoiando perguntas de negócio relacionadas a vendas, comportamento de compra e qualidade da operação logística.

## Perguntas de negócio

### Desempenho comercial

1. Qual foi o faturamento total da empresa no período analisado?
2. Quantos pedidos foram realizados?
3. Qual foi o ticket médio dos pedidos?
4. Como o faturamento evoluiu ao longo do tempo?

### Produtos e categorias

1. Quais categorias de produtos possuem maior volume de vendas?
2. Quais categorias geram o maior faturamento?
3. As categorias que vendem mais unidades também são as que geram maior faturamento?
4. Quais categorias possuem maior preço médio?
5. Existe concentração significativa do faturamento em poucas categorias ou produtos?

### Distribuição geográfica

1. Quais estados possuem maior quantidade de pedidos?
2. Quais estados geram maior faturamento?
3. O estado que possui mais pedidos é necessariamente o que gera mais receita?
4. Existem estados com participação muito baixa nas vendas que poderiam representar oportunidades de crescimento?

### Logística e experiência do cliente

1. Qual é o tempo médio entre a realização do pedido e a entrega?
2. Qual percentual dos pedidos foi entregue depois da data prevista?
3. Quais regiões apresentam maior ocorrência de atrasos?
4. Existe relação entre atraso na entrega e avaliação do cliente?
5. Clientes que tiveram problemas na entrega tendem a avaliar pior a experiência?

## Dataset

A análise utiliza o conjunto de dados público da Olist, composto por informações relacionadas a pedidos de e-commerce no Brasil. As bases utilizadas incluem dados de:

- Clientes
- Pedidos
- Itens dos pedidos
- Pagamentos
- Categorias de produtos
- Avaliações dos clientes
- Geolocalização

## Tecnologias utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Estrutura do projeto

```text
analise-ecommerce-olist/
│
├── dados/
│   ├── olist_customers_dataset.csv
│   ├── olist_geolocation_dataset.csv
│   ├── olist_order_items_dataset.csv
│   ├── olist_order_payments_dataset.csv
│   ├── olist_order_reviews_dataset.csv
│   ├── olist_orders_dataset.csv
│   ├── olist_products_dataset.csv
│   ├── olist_sellers_dataset.csv
│   └── product_category_name_translation.csv
│
├── analises/
│   ├── coleta.py
│   ├── desempenho_comercial.ipynb
│   ├── produtos_categorias.ipynb
│   ├── distribuicao_geografica.ipynb
│   ├── logistica_experiencia_cliente.ipynb
│   └── pagamentos.ipynb
│
├── requirements.txt
└── README.md
```

## Etapas da análise

### 1. Coleta e preparação dos dados

O script `coleta.py` centraliza o carregamento dos arquivos CSV e realiza etapas iniciais de tratamento, como:

- Leitura das bases com Pandas
- Conversão de colunas de data para o tipo `datetime`
- Remoção de pedidos duplicados
- Organização dos caminhos dos arquivos com `pathlib`

### 2. Desempenho comercial

Análise de indicadores comerciais, incluindo:

- Faturamento total
- Quantidade de pedidos
- Ticket médio
- Evolução do faturamento por ano e por mês

### 3. Produtos e categorias

Análise do comportamento de vendas por categoria de produto:

- Categorias com maior volume de vendas
- Categorias com maior faturamento
- Categorias com maior preço médio
- Concentração do faturamento nas principais categorias

### 4. Distribuição geográfica

Análise da distribuição de pedidos e faturamento entre os estados brasileiros:

- Estados com maior quantidade de pedidos
- Estados com maior faturamento
- Relação entre volume de pedidos e receita
- Estados com menor participação e possível potencial de crescimento

### 5. Logística e experiência do cliente

Avaliação da operação de entrega e de sua associação com a satisfação dos consumidores:

- Tempo médio entre compra e entrega
- Percentual de pedidos entregues após a data estimada
- Estados com maior número de atrasos
- Relação entre atraso e nota de avaliação

### 6. Pagamentos

Análise das formas de pagamento utilizadas pelos consumidores:

- Métodos de pagamento mais frequentes
- Valor médio por método de pagamento
- Participação de cada método no faturamento
- Relação entre número de parcelas e valor pago

## Como executar o projeto

### Pré-requisitos

Antes de começar, é necessário ter instalado:

- Python 3
- Git
- Jupyter Notebook ou Visual Studio Code

### 1. Clone o repositório

Abra o terminal e execute:

```bash
git clone https://github.com/VictorAlbuquerque2003/ProjetoAnaliseDeDadosECommerce.git
cd analise-ecommerce-olist
```

### 2. Crie um ambiente virtual

No diretório raiz do projeto, crie um ambiente virtual:

```bash
python -m venv .venv
```

### 3. Ative o ambiente virtual

No Windows:

```bash
.venv\Scripts\activate
```

No macOS ou Linux:

```bash
source .venv/bin/activate
```

### 4. Instale as dependências

Com o ambiente virtual ativado, instale as bibliotecas necessárias:

```bash
python -m pip install -r requirements.txt
```

### 5. Execute os notebooks

Inicie o Jupyter Notebook com o comando:

```bash
jupyter notebook
```

Em seguida, abra a pasta `analises/` e execute os notebooks na ordem desejada.

> O arquivo `coleta.py` deve permanecer na mesma pasta dos notebooks, pois ele é responsável por carregar as bases de dados utilizadas nas análises.