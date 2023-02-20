# Game Finance API

É um jogo que tem como objetivo obter a maior rentabilidade numa carteira virtual, com dados reais da bolsa de valores de São Paulo, a B3. Para Jogar é necessário efetuar o cadastro escolher no máximo cinco papéis listados na bolsa, ganha quem conseguir a maior rentabilidade dentro do período estipulado na rodada.

Os dados dos papéis são reais, e são consumidos a partir do pacote [yfinance](https://github.com/ranaroussi/yfinance) que utiliza a API pública do [Yahoo Finance](https://finance.yahoo.com/).

O objetivo do projeto é aprimorar minhas habilidades no Django Rest Framework, especificamente no tratamento de dados de requisições, autorizalções e permissões de usuários.

## Building

Esse projeto foi desenvolvido utilizando a versão 3.2.6 do interpretador Python. Todas as dependências
estão listadas no arquivo *requiments.txt*

### Como rodar ?

* realize o clone do repositório - `git clone https://github.com/MaercioMamedes/GameFinanceAPI.git`
* [crie um ambiente virtual dentro do diretório do projeto e instale todas as dependências](https://www.alura.com.br/artigos/ambientes-virtuais-em-python)
* rode o comando `python manage.py runserver`


## Etapas do projeto

:heavy_check_mark: Definir modelos e relacionamentos

:heavy_check_mark: Implementar lib de acesso aos Dados da bolsa de Valores B3

:heavy_check_mark: implementar autenticação de usuários

:x: implementar permissões de usuários

:heavy_check_mark: Definir view e rota para criar papel

:x: Definir view e rota para editar papel

:heavy_check_mark: Definir view e rota para adicionar papel à carteira

:x: Definir view e rota para editar carteira

:x: Definir view e rota configurar rodada

:heavy_check_mark: Definir view e rota resultado

:heavy_check_mark: Definir view e rota para simular rodada

:x: implementar ordenação de jogadores de acordo com a rentabilidade da carteira

:x: validação de entrada de dados


### End points

|          URI          |    MÉTODO    |                         RECURSO                         |
|:---------------------:|:------------:|:-------------------------------------------------------:|
|       /usuarios       |     GET      |                  lista todos usuários                   |
|       /usuarios       |     POST     |                    Cria novo usuário                    |
| /usuarios/{ user_id } |     GET      |                     retorna usuário                     |
| /usuarios/{ user_id } | PUT ou PATCH |                    atualiza usuário                     |
|        /papel         |     GET      |            lista todos os papéis cadastrados            |
|        /papel         |     POST     |                   cria um novo papel                    |
|       /carteira       |     GET      |      lista papéis na carteira do usuário da sessão      |
|       /carteira       |     POST     |     adiciona papel na carteira do usuário da sessão     |
|       /posicao        |     GET      |   retorna a lista dos jogadares e suas rentabilidades   |
|      /calculator      |     POST     | atualiza papéis adicionados nas carteiras dos jogadores |
|        /logout        |     POST     |                encerra sessão do usuário                |


### atributos dos modelos

#### User 
`{
    "username": input_username,
    "first_name": input_first_name,
    "last_name": input_last_name,
    "email": input_email,
    "password": input_password
}`

#### Paper
`{
    "b3_code": input_código_papel,
    "company_name": "input_nome_da_empresa"
}`

#### Wallet

`{
    "paper": id_papel
}`

### Calculando rentabilidade de período passado

`{
    "period": "3mo"
}`


## Disposições finais

Você pode navegar por essa aplicação, utilizando o próprio browser, inclusive pode acessar django-admin,
como super usuário e acessar a base de dados do projeto.
Para criar um super usuário execute os seguintes passos, no terminal:
* execute `python manage.py createsuperuser`
* digite um username válido
* digite uma senha válida
* confirme a senha digitada

Pronto, após a criação da conta de superusuário, rode a aplicação e acesse a uri `/admin`, na tela de 
login você digita o username e as senhas criados para seu superusuário.