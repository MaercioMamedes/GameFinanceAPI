# Game Finance API

É um jogo que tem como objetivo obter a maior rentabilidade numa carteira virtual, com dados reais da bolsa de valores de São Paulo, a B3. Para Jogar é necessário efetuar o cadastro escolher no máximo cinco papéis listados na bolsa, ganha quem conseguir a maior rentabilidade dentro do período estipulado na rodada.

Os dados dos papéis são reais, e são consumidos a partir do pacote [yfinance](https://github.com/ranaroussi/yfinance) que utiliza a API pública do [Yahoo Finance](https://finance.yahoo.com/).

O objetivo do projeto é aprimorar minhas habilidades no Django Rest Framework, especificamente no tratamento de dados de requisições, autorizalções e permissões de usuários.

## Building

Esse projeto foi desenvolvido utilizando a versão 3.2.6 do interpretador Python. Todas as dependências
estão listadas no arquivo *requiments.txt*


## Etapas do projeto

:heavy_check_mark: Definir modelos e relacionamentos

:heavy_check_mark: Implementar lib de acesso aos Dados da bolsa de Valores B3

:heavy_check_mark: implementar autenticação de usuários

:x: implementar permissões de usuários

:x: Definir view e rota para adicionar papel à carteira

:x: Definir view e rota para editar carteira

:x: Definir view e rota configurar rodada

:x: Definir view e rota resultado

:x: Definir view e rota para simular rodada