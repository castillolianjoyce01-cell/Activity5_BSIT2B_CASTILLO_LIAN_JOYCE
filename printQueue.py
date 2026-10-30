
from collections import deque


def simulate_print_queue():
    jobs = deque()

    jobs.append({"id": "P101", "pages": 5})
    jobs.append({"id": "P102", "pages": 3})
    jobs.append({"id": "P103", "pages": 8})

    print("Print jobs in waiting order:")

    for position, job in enumerate(jobs, start=1):
        print(
            f"Position {position}: "
            f"{job['id']} - {job['pages']} pages"
        )

    print("\nPrinting jobs:")

    while jobs:
        job = jobs.popleft()
        print(
            f"Printing {job['id']} "
            f"({job['pages']} pages)"
        )


if __name__ == "__main__":
    simulate_print_queue()
