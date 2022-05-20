import re
from typing import List


def solution(s: str, query: List[str]) -> List[str]:
    pattern = re.compile(s)
    res = []
    for q in query:
        r = re.match(pattern, q)
        if r:
            res.append(r.string)
    return res