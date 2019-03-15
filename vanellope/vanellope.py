from random import choice


def rotate_blocks(blocks: list, n: int):
    for x in range(n):
        int_a = choice(range(1, len(blocks)))
        int_b = int_a - 1
        blocks[int_a], blocks[int_b] = blocks[int_b], blocks[int_a]

    return blocks


def chunks(data: str, n: int):
    return [data[x: n+x] for x in range(0, len(data), n)]