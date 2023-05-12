import requests
import json


class ConvertionException(Exception):
    pass

class CryptoConvertor:
    @staticmethod
    def convert(base: str, quote: str, amount: str):
        if base == quote:
            raise ConvertionException(
                f'Друг, ты конвертируешь одинаковые валюты {quote}. Надо вот так (Пример): доллар рубль 1')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество валюты {amount}.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        total_quote = json.loads(r.content)[keys[quote]]

        return total_quote