# Dashboard Titanic 🚢
# Este projeto utiliza dados reais do Titanic para explorar informações e criar visualizações detalhadas com o Power BI

# Dicionário de Variáveis 
    • PassengerID: Número de identificação do passageiro.
    •Survived: Informa se o passageiro sobreviveu ao naufrágio (0 = não e 1 = sim).
    •Pclass: Classe do bilhete (1 = 1ª classe; 2 = 2ª classe; 3 = 3ª classe).
    •Name: Nome do passageiro.
    •Sex: Sexo do passageiro.
    •Age: Idade do passageiro.
    •SibSp: Quantidade de cônjuges e/ou irmãos a bordo.
    •Parch: Quantidade de pais e filhos a bordo.
    •Ticket: Número da passagem.
    •Fare: Preço da passagem.
    •Cabin: Número da cabine do passageiro.
    •Embarked: Porto de embarque (C = Cherbourg; Q = Queenstown; S = Southampton).

# Estrutura do Projeto 

 ## 1. Datawarehouse

    •Um Datawarehouse foi criado para consolidar os dados.
    •As tabelas foram modeladas em um banco de dados SQL, separadas em tabelas de dimensões e fatos.
    •Após o processamento, os dados foram exportados para arquivos CSV para integração no Power BI.

 ## 2. Visualização no Power BI

    •Dados estruturados foram carregados no Power BI para a construção de relatórios e dashboards interativos.
    •Gráficos, tabelas dinâmicas e métricas foram configurados para explorar os dados de forma intuitiva.

# Tecnologias Utilizadas 
    •SQL: Para criação e manipulação do Datawarehouse.
    •Power BI: Para visualização e exploração dos dados.
    •CSV: Para armazenamento e integração dos dados.

# Link Dashboard
https://app.powerbi.com/view?r=eyJrIjoiZGQ0ZDBmMjItNzk1ZC00MjNmLThlYzUtNmQzNzEzMTBiZDU0IiwidCI6ImQ5NzZkNWZjLTk2NWItNDkyZi1hOTkxLWIwZGRkOTQ5ZmI2YyJ9