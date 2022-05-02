import json
from exceptions import *


def load_json_data(path):
    """Загрузка JSON-файла"""
    try:
        with open(path, 'r', encoding="UTF-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise DataJsonError


def search_post_by_substring(posts, substring):
    """Поиск поста, среди списка постов"""
    posts_founded = []
    for post in posts:
        if substring.lower() in post["content"].lower():
            posts_founded.append(post)
    return posts_founded
