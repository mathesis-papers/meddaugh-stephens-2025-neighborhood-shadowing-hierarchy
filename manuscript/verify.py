import json
from fractions import Fraction


def masks(size):
    quarter = Fraction(1, 4)
    result = [[(-quarter, 7 * quarter)], [(size - 7 * quarter, size + quarter)]]
    if size >= 4:
        spacing = 1 - Fraction(1, 2 * (size - 3))
        for index in range(2, size - 1):
            center = 7 * quarter + (index - Fraction(3, 2)) * spacing
            result.append([(-quarter, quarter), (center - Fraction(1, 2), center + Fraction(1, 2))])
    return result


def contains(intervals, phase, size):
    return any(left < phase + period * size < right
               for left, right in intervals for period in range(-2, 3))


def arrangement(endpoints, period):
    vertices = sorted({Fraction(0), Fraction(period), *(point % period for point in endpoints)})
    return vertices + [(left + right) / 2 for left, right in zip(vertices, vertices[1:])]


def check(size):
    cover = masks(size)
    polygon_cases = 0
    for intervals in cover:
        assert contains(intervals, Fraction(0), size)
        endpoints = [point - index for interval in intervals for point in interval for index in range(size)]
        for phase in arrangement(endpoints, 1):
            occupied = sum(contains(intervals, phase + index, size) for index in range(size))
            assert occupied <= 2, (size, phase, occupied)
            polygon_cases += 1
    margin = Fraction(1, 16 * size)
    eroded = [[(left + margin, right - margin) for left, right in intervals] for intervals in cover]
    endpoints = [point for intervals in eroded for interval in intervals for point in interval]
    coverage_cases = 0
    for phase in arrangement(endpoints, size):
        assert any(contains(intervals, phase, size) for intervals in eroded), (size, phase)
        coverage_cases += 1
    assert all(any(left <= -Fraction(1, 4) and Fraction(1, 4) <= right
                   for left, right in intervals) or
               any(left <= size - Fraction(1, 4) and size + Fraction(1, 4) <= right
                   for left, right in intervals)
               for intervals in cover)
    return {'m': size, 'polygon_arrangement_cases': polygon_cases,
            'eroded_cover_arrangement_cases': coverage_cases}


def main():
    results = [check(size) for size in range(3, 21)]
    print(json.dumps({'status': 'pass', 'arithmetic': 'exact rational',
        'scope': 'Circle masks, polygon occupancy at all arrangement endpoints and open cells, and circle coverage with margin 1/(16m), for 3 <= m <= 20. The all-integer theorem has a written proof in note.tex.',
        'results': results}, indent=2))


if __name__ == '__main__':
    main()
