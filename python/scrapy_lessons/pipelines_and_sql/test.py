from scrapyd_client import ScrapydClient

client = ScrapydClient()

# for project in client.projects():
#     print(client.jobs(project=project))


def how_many_jobs():
    pending = len(client.jobs("app").get("pending"))
    running = len(client.jobs("app").get("running"))
    finished = len(client.jobs("app").get("finished"))
    print(f"{pending = }")
    print(f"{running = }")
    print(f"{finished = }")


def start_spider():
    how_many_jobs()
    print("starting")
    client.schedule("app", "parsinger")
    print('success')
    how_many_jobs()


how_many_jobs()
# start_spider()
