# AtividadeFinalPDS

    - INTEGRANTES - 
* Júlia Medeiros do Nascimento - 20201214010028
* Maria Clara Araújo dos Santos - 20201214010035
* Raquel Gabrielly do Nascimento - 20201214010024
* Tainá Brito de Medeiros - 20201214010015
  
# TB Makes - Controle de Maquiagens

A TB Makes é um projeto de software que está sendo implementado por estudantes que cursam o ensino médio técnico integrado em Informática no Instituto Federal de Educação, Ciências, Tecnologias, Pesquisa e Extensões do Rio Grande do Norte (IFRN) - Campus Avançado Parelhas. O objetivo desse projeto é ajudar na dinâmica de funcionamento da loja física de maquiagem TB Makes, como também no gerenciamento de estoque de produtos de maquiagem. A aplicação do desenvolvimento do software está sendo desenvolvida em: 

Linguagem de back-end e front-end: Python;
Banco de dados: PostgreSQL 15.1;
Arquitetura: MVC (Model, View, Controller);
Ambiente de desenvolvimento: VSCode.

# Necessidade do Cliente

A loja TB Makes é um espaço dedicado à venda e teste de produtos de maquiagem, com o objetivo de proporcionar uma experiência segura e confortável às clientes, reforçando a autoestima delas e criando um atendimento individualizado para as necessidades de cada cliente.

Como uma classificação de loja de cosméticos específica, existem necessidades a serem supridas para que seu funcionamento seja eficiente. 

Durante uma visita ao local, identificou-se questões e situações de carência quanto ao sistema de vendas, cada passo à passo. Logo, ficou claro que melhorar o controle de vendas e o cadastro de produtos era importante. Portanto, o projeto tem como finalidade automatizar a gestão de maquiagens, armazenando os dados em um banco de dados para facilitar o trabalho dos funcionários, permitindo consultas e a manipulação de informações. Funcionalidades e requesitos serão implementados para a criação do sistema. 

Esse sistema de controle de maquiagens proporcionará aos funcionários um conhecimento abrangente das operações que eles poderão exercer na TB Makes, mesmo quando não estiverem fisicamente no ambiente, o que irá facilitar o aumento das vendas, a eficência e proporcionar melhores manuseios para os pedidos e compras já realizadas. Isso possibilitará o acompanhamento do estoque de maquiagens disponíveis para venda (por meio de IDs), a categorização dos tipos de maquiagem (por meio dos nomes) e o controle da quantidade de maquiagens em estoque (por meio do estado). Além disso, o sistema ajudará a prever a necessidade de novas compras, tornando possível o acompanhamento externo da loja. Sendo assim, frisando acima de tudo o controle das informações de cada venda. 

Existindo uma visualização simples e objetiva para facilitar o uso, o usuário deverá selecionar a aba correspondente ao que deseja acessar. Para realizar as operações de adição, atualização e remoção de maquiagens, o usuário deverá fornecer o código, nome, quantidade de produtos e data da ação, e confirmar a operação por meio de um botão na parte inferior. Na aba de visualização, uma tabela exibirá todos os produtos de maquiagem cadastrados, facilitando a organização do sistema e gerando praticidade aos usuários.

# Requisitos

## Requisitos Funcionais

* [RF001] Cadastrar Produto

    Descrição: O sistema deve conceder aos funcionários a capacidade de cadastrar novas maquiagens.

    Prioridade: Essencial

* [RF002] Visualização de Produtos

    Descrição: O sistema deve permitir a visualização de produtos existentes.

    Prioridade: Essencial

* [RF003] Atualização de Produtos

    Descrição: O sistema deve conceder aos funcionários a capacidade de atualizar os dados dos produtos.

    Prioridade: Essencial

* [RF004] Deletamento de Produtos

    Descrição: O sistema deve conceder aos funcionários a capacidade de excluir produtos

    Prioridade: Essencial

* [RF005] Monitoramento da disponibilidade de produtos para venda

    Descrição: O sistema deve conceder aos funcionários a capacidade de verificar se o produto está disponível para venda pela quantidade.

    Prioridade: Essencial

* [RF006] Controle de Entrada e Saída de produtos
    
    Descrição: O sistema deve permitir aos funcionários a capacidade de visualizara a data de cadastramento do produto (Chegada) e a data de venda do produto (Saída).

    Prioridade: Essencial

## Requisitos Não Funcionais

* [NF001] Necessidade de compra de novos produtos

    Descrição: O sistema deve permitir aos funcionários a capacidade de acompanhar a quantidade de produtos disponíveis para poder fazer a compra de produtos novos.

    Prioridade: Desejável


# Análise dos Requisitos e do Projeto

## Diagramação  
* Casos de uso

Os requisitos que serão implementados consistem no cadastro, visualização, atualização e deleção de produtos. Por meio do diagrama de Caso de Uso, é possível analisar a conexão entre o administrador e as funções de cadastrar, atualizar e deletar produtos.

![image](https://github.com/TainaBrito/AtividadeFinal4Ano/assets/108409645/89373697-47b8-48e4-ae0d-72b3f4144328)

* Banco de Dados
  
  Conforme os requisitos implementados, fez-se necessário o uso auxiliar de um Banco de Dados para o armazenamento das informações coletadas.


  ![image](https://github.com/TainaBrito/AtividadeFinal4Ano/assets/108409645/cfd33d75-94ae-489e-87db-46f648451a4f)
