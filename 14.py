def add_job(queue, job):
    queue.append(job)
    print("Job added:", job)


def delete_job(queue):
    if len(queue) == 0:
        print("No jobs to delete.")
    else:
        job = queue.pop(0)
        print("Job deleted:", job)


def display_jobs(queue):
    print("Jobs in queue:")
    for job in queue:
        print(job)



queue = []

while True:
    print("""
Menu:
1) Add Job
2) Delete Job
3) Display Jobs
4) Exit
""")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        job = input("Enter job name: ")
        add_job(queue, job)
    elif ch == 2:
        delete_job(queue)
    elif ch == 3:
        display_jobs(queue)
    elif ch == 4:
        break
    else:
        print("Invalid choice!")
