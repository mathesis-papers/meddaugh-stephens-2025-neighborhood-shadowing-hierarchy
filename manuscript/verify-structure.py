import itertools
import json


def legal_finite(support, size):
    if len(support) < 3:
        return True
    ordered = sorted(support)
    step = 1
    while step <= ordered[-1] - ordered[0]:
        residues = {}
        for position in ordered:
            residues.setdefault(position % step, []).append(position)
        for positions in residues.values():
            for index in range(len(positions) - 2):
                if positions[index + 2] - positions[index] <= (size - 1) * step:
                    return False
        step *= size + 1
    return True


def allowed_words(size):
    result = []
    for length in range(1, 7):
        for bits in itertools.product([0, 1], repeat=length):
            support = {index for index, bit in enumerate(bits) if bit}
            if legal_finite(support, size):
                result.append((length, support))
    return result


def check(size):
    words = allowed_words(size)
    gluing = 0
    for left_length, left_support in words:
        for right_length, right_support in words:
            diameter = max(left_length - 1, right_length - 1)
            for increment in [1, 2, 3]:
                gap = (size - 1) * diameter + increment
                combined = left_support | {
                    left_length + gap + position for position in right_support
                }
                assert legal_finite(combined, size)
                gluing += 1
    periodic = 0
    for length, support in words:
        scale = 1
        exponent = 0
        while scale <= length:
            scale *= size + 1
            exponent += 1
        period = size * scale
        for power in range(exponent + 1):
            step = (size + 1) ** power
            for start in range(period):
                occupied = sum(
                    (start + vertex * step) % period in support
                    for vertex in range(size)
                )
                assert occupied <= 2
                periodic += 1
        assert pow(size + 1, exponent + 1, period) == scale
        assert (scale * (size + 1)) % period == scale
    bridges = 0
    for exponent in [0, 1, 2]:
        step = (size + 1) ** exponent
        left = {0, step}
        right_position = 2 * step
        assert legal_finite(left, size)
        assert legal_finite({step}, size)
        assert not legal_finite(left | {right_position}, size)
        bridges += 1
    return {
        'm': size,
        'allowed_words': len(words),
        'gluing_cases': gluing,
        'periodic_progressions': periodic,
        'bridge_obstructions': bridges,
    }


def main():
    print(json.dumps({
        'status': 'pass',
        'arithmetic': 'exact integer',
        'scope': 'All allowed binary words of lengths 1 through 6 for 3 <= m <= 6; three zero-gap lengths for each ordered pair; every translated progression in each proposed periodic extension at scales 0 through K; bridge obstructions at scales 0, 1, 2. The congruence (m+1)^k = (m+1)^K modulo m(m+1)^K for k >= K and the all-parameter conclusions have written proofs in note.tex.',
        'results': [check(size) for size in range(3, 7)],
    }, indent=2))


if __name__ == '__main__':
    main()
