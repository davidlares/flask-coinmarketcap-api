## CoinMarketCap API with Flask

This is an API built with Python 3, using the Flask and MongoDB microframeworks, for building an experience with real cryptocurrency data (coinmarketcap).

## Dependencies

Pymongo -> Managing MongoDB with Python (database operations)
Flask -> Microframework for creating a Web Server
Jsonify -> Sending JSON to the client (using Python dictionaries)
Request -> Capturing client information via QueryString

## API Run
- Assuming MongoDB is installed

```
python3 agent/main.py
```

- python3 api/main.py

## URLs

- GET ('/', '/top-20','/tickers')
- DELETE ('/tickers?name="COIN_NAME"')

## Credits
[David Lares S](https://davidlares.com)

## License
[MIT](https://opensource.org/licenses/MIT)
