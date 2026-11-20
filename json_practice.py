import json

def analyze_jobs(jobs, min_salary, remote_only):
    if not isinstance(jobs, list) or not all(isinstance(job, dict) for job in jobs):   
        raise ValueError("Jobs must be a list of dictionaries")

    if not all("title" in job and "salary" in job and "remote" in job for job in jobs):
        raise ValueError("Each job must have 'title', 'salary', and 'remote' keys")

    if not all(isinstance(job["title"], str) for job in jobs):
        raise ValueError("Job title must be a string")

    if not all(isinstance(job["salary"], (int, float)) for job in jobs) and not all(isinstance(job["salary"], bool) for job in jobs):
        raise ValueError("Salary must be a number")

    if not all(isinstance(job["remote"], bool) for job in jobs):
        raise ValueError("Remote must be a boolean")

    if not isinstance(min_salary, (int, float)) or isinstance(min_salary, bool):
        raise ValueError("Minimum salary must be a number")

    if not isinstance(remote_only, bool):
        raise ValueError("Remote only must be a boolean")

    filtered_jobs = []
    count = 0
    total_salary = 0
    average_salary = 0

    if remote_only:
        for job in jobs:
            if job["remote"] and job["salary"] >= min_salary:
                filtered_jobs.append(job)
                count += 1
                total_salary += job["salary"]

    else:
        for job in jobs:
            if job["salary"] >= min_salary:
                filtered_jobs.append(job)
                count += 1
                total_salary += job["salary"]

    if count > 0:
        average_salary = total_salary / count       

    return {
        "count": count,
        "average_salary": average_salary,
        "filtered_jobs": filtered_jobs
    }

jobs_json = '''
[
    {
        "title": "QA Automation Engineer",
        "salary": 65000,
        "remote": true
    },
    {
        "title": "Manual QA",
        "salary": 45000,
        "remote": false
    },
    {
        "title": "SDET",
        "salary": 80000,
        "remote": true
    }
]
'''

job_data = json.loads(jobs_json)

result = analyze_jobs(job_data, min_salary=50000, remote_only=True)
print(json.dumps(result, indent=4))