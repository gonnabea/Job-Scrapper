import csv
# CSV == Comma Sperated Value


def save_to_file(jobs, word):
    file = open(f"{word} jobs.csv", mode="w", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
        if job:
            writer.writerow(list(job.values()))
    return
