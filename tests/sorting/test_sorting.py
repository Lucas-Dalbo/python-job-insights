import pytest
from src.pre_built.sorting import sort_by

@pytest.fixture()
def jobs_list():
    return [
        {"min_salary": 100, "max_salary": 500, "date_posted": "2020-06-10"},
        {"min_salary": 1000, "max_salary": 1200, "date_posted": "2020-04-03"},
        {"min_salary": 2000, "max_salary": 3000, "date_posted": "2020-10-15"},
    ]

def test_sort_by_criteria(jobs_list):
    # min_salary
    sorted_by_min = [
        {"min_salary": 100, "max_salary": 500, "date_posted": "2020-06-10"},
        {"min_salary": 1000, "max_salary": 1200, "date_posted": "2020-04-03"},
        {"min_salary": 2000, "max_salary": 3000, "date_posted": "2020-10-15"},
    ]

    sort_by(jobs_list, "min_salary")
    assert jobs_list == sorted_by_min
    
    # max_salary
    sorted_by_max = [
        {"min_salary": 2000, "max_salary": 3000, "date_posted": "2020-10-15"},
        {"min_salary": 1000, "max_salary": 1200, "date_posted": "2020-04-03"},
        {"min_salary": 100, "max_salary": 500, "date_posted": "2020-06-10"},
    ]

    sort_by(jobs_list, "max_salary")
    assert jobs_list == sorted_by_max

    # date_posted
    sorted_by_date = [
        {"min_salary": 2000, "max_salary": 3000, "date_posted": "2020-10-15"},
        {"min_salary": 100, "max_salary": 500, "date_posted": "2020-06-10"},
        {"min_salary": 1000, "max_salary": 1200, "date_posted": "2020-04-03"},
    ]

    sort_by(jobs_list, "date_posted")
    assert jobs_list == sorted_by_date
