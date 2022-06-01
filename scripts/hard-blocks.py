from __future__ import annotations
from typing import TypeVar
from dataclasses import dataclass
from itertools import product

@dataclass(frozen=True)
class Size:
    w: int
    h: int

    def reverse(self) -> Size:
        return Size(self.h, self.w)

    def v_combine(self, rhs: Size) -> Size:
        return Size(self.w + rhs.w, max(self.h, rhs.h))

    def h_combine(self, rhs: Size) -> Size:
        return Size(max(self.w, rhs.w), self.h + rhs.h)

    def __lt__(self, rhs: Size) -> bool:
        return (
            self.w < rhs.w and self.h <= rhs.h
        ) or (
            self.w <= rhs.w and self.h < rhs.h
        )


T = TypeVar('T')
def dedup(li: list[T]) -> list[T]:
    return list(set(li))


class Node:
    def sizes(self) -> list[Size]:
        raise NotImplementedError('Node must implement sizes')


class TerminalNode(Node):
    def __init__(self, w: int, h: int) -> None:
        self.w = w
        self.h = h

    def sizes(self) -> list[Size]:
        return dedup([Size(self.w, self.h), Size(self.h, self.w)])


class VSplitNode(Node):
    def __init__(self, name: str, left: Node, right: Node) -> None:
        self.name = name
        self.left = left
        self.right = right

    def sizes(self) -> list[Size]:
        lsizes = self.left.sizes()
        rsizes = self.right.sizes()
        candidates = []
        for lsize, rsize in product(lsizes, rsizes):
            combined = lsize.v_combine(rsize)
            candidates.append(combined)
        ans = dedup([s for s in candidates if not any(z < s for z in candidates)])

        print(self.name, candidates)
        print(self.name, ans)

        return ans


class HSplitNode(Node):
    def __init__(self, name: str, left: Node, right: Node) -> None:
        self.name = name
        self.left = left
        self.right = right

    def sizes(self) -> list[Size]:
        lsizes = self.left.sizes()
        rsizes = self.right.sizes()
        candidates = []
        for lsize, rsize in product(lsizes, rsizes):
            combined = lsize.h_combine(rsize)
            candidates.append(combined)
        ans = dedup([s for s in candidates if not any(z < s for z in candidates)])

        print(self.name, candidates)
        print(self.name, ans)

        return ans


def main():
    H = HSplitNode
    V = VSplitNode
    T = TerminalNode

    tree = H('H1',
        H('H2',
            V('V1',
                T(3, 1),
                T(3, 2)),
            V('V2',
                T(4, 1),
                T(2, 2))),
        V('V3',
            T(3, 4),
            T(1, 2)))
    print(tree.sizes())


if __name__ == '__main__':
    main()
