from typing import Literal

import requests

from config import TRANSLATER_API_KEY, TRANSLATER_URL

headers = {'Content-Type': 'application/json',
           'Authorization': f'Api-Key {TRANSLATER_API_KEY}'}


def get_translation(texts: list, source_lang: Literal['tt', 'ru'], target_lang: Literal['ru', 'tt']) -> list[str]:
    data = {
        "sourceLanguageCode": source_lang,
        "targetLanguageCode": target_lang,
        "format": "PLAIN_TEXT",
        "texts": texts
    }

    result = requests.post(TRANSLATER_URL, json=data,
                           headers=headers)
    print(result.json())
    return list(map(lambda x: x['text'], result.json()['translations']))
