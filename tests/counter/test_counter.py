from src.pre_built.counter import count_ocurrences


def test_counter():
    path = "data/jobs.csv"
    word = "FULL-TIME"
    result = count_ocurrences(path, word)
    assert result == 726
