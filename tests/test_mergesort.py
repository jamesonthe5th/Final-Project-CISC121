from app import mergesort

def test_empty():
    steps = []
    assert mergesort([], steps) == []

def test_single():
    steps = []
    assert mergesort([1], steps) == [1]

def test_sorted():
    steps = []
    assert mergesort([1, 2, 3], steps) == [1, 2, 3]


def test_unsorted():
    steps = []
    assert mergesort([3, 1, 2], steps) == [1, 2, 3]


def test_duplicates():
    steps = []
    assert mergesort([2, 1, 2], steps) == [1, 2, 2]
