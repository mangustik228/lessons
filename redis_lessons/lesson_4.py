from redis import Redis


client = Redis("localhost", 6379, 0)


def do_something(task):
    print(task)


while True:
    task = client.brpop("task")
    do_something(task)
