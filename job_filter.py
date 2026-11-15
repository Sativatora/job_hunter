# Job filtering utilities

def get_jobs_by_salary(jobs, min_salary):
    if not isinstance(jobs, list):
        raise ValueError("Jobs must be a list")
    if not isinstance(min_salary, (int, float)):
        raise ValueError("Minimum salary must be a number")
    if min_salary < 0:
        raise ValueError("Minimum salary must be a non-negative number")
    if len(jobs) == 0:
        return []

    filtered_jobs = []
    for job in jobs:
        if not isinstance(job, dict) or "title" not in job or "salary" not in job:
            raise ValueError("Each job must be a dictionary with 'title' and 'salary' keys")
        if not isinstance(job["salary"], (int, float)) or job["salary"] < 0:
            raise ValueError("Job salary must be a non-negative number")
        if job["salary"] >= min_salary:
            filtered_jobs.append(job)

    return filtered_jobs