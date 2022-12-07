from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    expected_keys = {"title", "salary", "type"}

    file = "tests/mocks/brazilians_jobs.csv"
    result = read_brazilian_file(file)

    keys = set()
    for job in result:
        for key in job.keys():
            keys.add(key)

    assert keys == expected_keys
