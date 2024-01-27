from typing import Literal, Optional

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

    result = requests.post(TRANSLATER_URL + 'translate', json=data,
                           headers=headers)
    return list(map(lambda x: x['text'], result.json()['translations']))


def detect_language(text, language_code_hints=None) -> Optional[str]:
    if language_code_hints is None:
        language_code_hints = ['tt', 'ru']

    data = {
        'text': text,
        'languageCodeHints': language_code_hints
    }

    result = requests.post(TRANSLATER_URL + 'detect', json=data, headers=headers)

    if result:
        return result.json()['languageCode']
    else:
        return None
