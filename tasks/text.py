from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:

    optional = text.split()
    min_word = min(optional, default = None, key = len)
    max_word = max(optional, default = None, key = len)

    optional = (min_word, max_word)
    return (optional)
