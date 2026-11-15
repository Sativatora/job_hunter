from job_filter import get_jobs_by_salary
import pytest


# Positive tests

@pytest.mark.parametrize(
    "salary, min_salary, expected",
    [
        (65000, 50000, True),
        (50000, 50000, True),
        (45000, 50000, False),
        (100000, 50000, True),
        (0, 50000, False),
        (49999, 50000, False),
        (50001, 50000, True),
    ]
)
def test_salary_filter(salary, min_salary, expected):
    jobs = [{"title": "SDET", "salary": salary}]
    result = get_jobs_by_salary(jobs, min_salary)
    assert bool(result) == expected


def test_empty_jobs_list():
    assert get_jobs_by_salary([], 50000) == []


# Negative tests

def test_negative_min_salary():
    with pytest.raises(ValueError, match="Minimum salary must be a non-negative number"):
        get_jobs_by_salary([], -1000)


def test_jobs_none():
    with pytest.raises(ValueError, match="Jobs must be a list"):
        get_jobs_by_salary(None, 50000)


def test_min_salary_string():
    with pytest.raises(ValueError, match="Minimum salary must be a number"):
        get_jobs_by_salary([], "50000")


def test_negative_job_salary():
    with pytest.raises(ValueError, match="Job salary must be a non-negative number"):
        get_jobs_by_salary([{"title": "SDET", "salary": -50000}], 50000)