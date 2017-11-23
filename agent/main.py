import requests # permite hacer consultas a una endpoint
import pymongo # libreria de conexion a una base de datos en mongo

API_URL = 'https://api.coinmarketcap.com/v1/ticker/'

def get_db_connection(uri):
    client = pymongo.MongoClient(uri);
    return client.cryptongo

def get_crytocurrencies_from_api():
    r = requests.get(API_URL)
    if r.status_code == 200:
        result = r.json() # diccionario de python para llevarlo a Mongo
        return result
    raise Exception('API Error')

def get_hash(value):
    # usabilidad de la funcion de cifrado sha512
    from hashlib import sha512
    return sha512(value.encode('utf-8')).hexdigest();

def first_element(elements):
    # tupla -> key / value (inmutable)
    return elements[0]
    pass

def get_ticker_hash(ticker_data):
    # tomar todos los valores y colocarlos en un string largo
    from collections import OrderedDict     # py3.5 -> generar un diccionario ordenado (key, value)
    ticker_data = OrderedDict(
        sorted(
            ticker_data.items(),
            key=first_element
        )
    )
        # sorted() ordenar estructura de dato de acuerdo a un valor

    ticker_value = ''
    for _, value in ticker_data.items():
        ticker_value += str(value)

    return get_hash(ticker_value)


def check_if_exists(db_connection,ticker_data):

    ticker_hash = get_ticker_hash(ticker_data)
    # verificamos si la data es unica
    if db_connection.tickers.find_one({'ticker_hash': ticker_hash}): # mongo find by Object
        return True
    else:
        return False

def save_ticker(db_connection, ticker_data = None):
    if not ticker_data:
        return False
    if check_if_exists(db_connection,ticker_data):
        return False

    ticker_hash = get_ticker_hash(ticker_data)
    ticker_data['ticker_hash'] = ticker_hash
    ticker_data['rank'] = int(ticker_data['rank']) # casteo del V-diccionario a un Int
    ticker_data['last_updated'] = int(ticker_data['last_updated']) # casteo del V-diccionario a un Int

    # mongo syntax -> conexion, collection, metodo de insersion
    db_connection.tickers.insert_one(ticker_data)

# punto de entrada desde el archivo
if __name__ == "__main__":
    connection = get_db_connection('mongodb://localhost:27017')
    tickers = get_crytocurrencies_from_api();
    for ticker in tickers:
        save_ticker(connection,ticker)

    print('Tickers Saved')
