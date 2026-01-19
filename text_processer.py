import re
import unicodedata

def clean_text(text):
    if not isinstance(text, str):
        return ""

    text = unicodedata.normalize("NFC", text)
    text = re.sub(r'[\n\r\t]', ' ', text)

    text = re.sub(
        "[" 
        "\U0001F600-\U0001F64F"
        "\U0001F300-\U0001F5FF"
        "\U0001F680-\U0001F6FF"
        "\U0001F700-\U0001F77F"
        "\U0001F780-\U0001F7FF"
        "\U0001F800-\U0001F8FF"
        "\U0001F900-\U0001F9FF"
        "\U0001FA00-\U0001FAFF"
        "\U00002700-\U000027BF"
        "]+",
        "",
        text
    )

    text = re.sub(r'[^0-9a-zA-ZÀ-ỹ\s]', ' ', text)
    text = text.lower()
    text = re.sub(r'\s+', ' ', text).strip()

    return text
