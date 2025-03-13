# Análise de vendas de café (WIP)

Criei um dashboard em Power BI sobre um dataset do Kaggle de vendas de uma máquina de venda automática de café, onde fiz a extração dos dados através do Python e o armazenei dentro de um banco de dados SQLite. 
Juntando com dados externos relevantes, fiz a análise com sugestões além de previsão do faturamento.

Dataset: https://www.kaggle.com/datasets/ihelon/coffee-sales

![image](https://github.com/user-attachments/assets/69356479-3016-4595-9125-527a9640fa31)

## Sobre o dataset

O dataset é referente à venda de uma máquina de venda automática de café na Ucrânia, que inclui a data, hora, tipo de pagamento, valor e o tipo de café vendido. 
Como os dados são atualizados com frequência, faço a atualização dos dados através de um script de Python, onde armazeno em um banco de dados SQLite.

Valores convertidos em BRL obter valores mais próximos à realidade brasileira através de um simples cálculo de conversão, mas idealmente seria feito relacionando com um histórico de conversão de UAH/BRL.

Dados de feriados da Ucrânia inseridos manualmente provisioriamente para permitir analisar a performance entre dia útil e feriado.

## Análises
