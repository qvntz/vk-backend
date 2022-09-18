import json
from typing import Callable, List, Union


def some_callback(key):
    print(key)


def parse_json(
        json_str: json,
        keyword_callback: Callable,
        required_fields: List[Union[str]] = None,
        keywords: list[str] = None
) -> None:
    json_dict = json.loads(json_str)
    keywords = keywords
    for i in required_fields:
        if (k := json_dict.get(i, None)) and (keys := [x for x in k.split() if x in keywords]):
            try:
                for key in keys:
                    keyword_callback(key)
            except Exception:
                pass
