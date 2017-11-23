# davidCoin

DavidCoin es una API creada con Python3, bajo el microframework Flask y MongoDB para la construccion de una
experiencia con datos reales de criptomonedas (coinmarketcap)

## Dependencias

  Pymongo -> manejo de mongoDB con Python (operaciones en la BD)
  Flask -> microframework para crear un Servidor Web
  Jsonify -> enviar JSON al clientes (usando diccionarios de Python)
  Request -> capturar informacion del cliente a traves del QueryString

## API Run
  - Asumiendo mongoDB instalado

  ```
    python3 agent/main.py
  ```

  - python3 api/main.py

## URLs

  - GET ('/', '/top-20','/tickers')
  - DELETE ('/tickers?name="COIN_NAME"')

## Créditos
  - [David Lares](https://twitter.com/davidlares3)

## Licencia

  [MIT](https://opensource.org/licenses/MIT)
