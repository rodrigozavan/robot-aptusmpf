import slugify
import string
import re

whitespace = '\t\n\r\v\f'

def remove_whitespaces(text: str) -> str:
    text = text.replace("\xa0", " ")
    text = re.sub(r"\s{2,}", " ", text)
    return text.translate(str.maketrans('', '', whitespace))

def remove_punctuation(text: str) -> str:
    return text.translate(str.maketrans('', '', string.punctuation))

def slugify_text(text: str) -> str:
    return slugify.slugify(remove_punctuation(text)).lower()