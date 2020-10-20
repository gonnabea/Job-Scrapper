from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs
from save import save_to_file


def get_jobs(word):
    print(f"{word}: 스크래핑 시작")
    indeed_jobs = get_indeed_jobs(word)
    so_jobs = get_so_jobs(word)
    # 검색결과가 나오지 않았을 경우 체크
    jobs = None
    if so_jobs and indeed_jobs:
        jobs = so_jobs + indeed_jobs
    elif indeed_jobs and so_jobs == []:
        jobs = indeed_jobs
    else:
        jobs = so_jobs
    save_to_file(jobs)  # 스크래핑 실행
    return jobs
