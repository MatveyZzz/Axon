import json


def load_json(path: str) -> list[dict[str, any]]:
    """Читает JSON файл и возвращает список записей.
       Возвращает пустой список, если файл пустой или не существует."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            raise ValueError("Ожидался список в корне JSON.")
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Ошибка чтения JSON: {e}") from e


read = load_json('data/data.json')


def topic_2_message(message, file=None):
    if file is None:
        file = read

    message_lower = message.lower()
    for item in file:
        # Проверяем все теги
        for tag in item.get("tags", []):
            if tag.lower() in message_lower:
                return item

    # Если ничего не нашли
    return None


def answer(message):
    result = topic_2_message(message, read)
    if result:
        return (
            f"🔬 {result['title']}\n\n"
            f"💡 {result['summary']}\n\n"
            f"🚀 Применение: {result['application']}\n\n"
            f"Источник: {result['source']}"
        )
    else:
        return "🤔 К сожалению, я не нашёл исследований по этой теме. Попробуй задать запрос иначе."
