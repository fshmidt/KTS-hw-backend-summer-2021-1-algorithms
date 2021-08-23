from typing import TypeVar

__all__ = (
    'flip_kv_vk',
    'flip_kv_vk_safe',
)


KT = TypeVar('KT')
KV = TypeVar('KV')


def flip_kv_vk(d: dict[KT, KV]) -> dict[KV, KT]:
    new_dict = {v: k for k, v in d.items()}
    return new_dict



def flip_kv_vk_safe(d: dict[KT, KV]) -> dict[KV, list[KT]]:
    new_dict = {}
    for k, v in d.items():
        new_dict.setdefault(v, []).append(k)
    return new_dict
