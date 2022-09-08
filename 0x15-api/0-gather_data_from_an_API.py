#!/usr/bin/python3
from urllib import request
import json
from sys import argv

if __name__ == "__main__":
    todos = "https://jsonplaceholder.typicode.com/todos"
    user = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    with request.urlopen(todos) as response:
        with request.urlopen(user) as User:
            content_user = User.read()
            content_user = content_user.decode('utf8').replace("'", '"')
            data_user = json.loads(content_user)
        task_completed = []
        total_task = 0
        content = response.read()
        content = content.decode('utf8').replace("'", '"')
        data = json.loads(content)
        for task in data:
            if task.get('userId') == int(argv[1]):
                total_task += 1
                if task.get('completed') is True:
                    task_completed.append(task)
        print("Employee {} is done with tasks({}/{}):"
              .format(data_user['name'], len(task_completed), total_task))
        for instance in task_completed:
            print("\t {}".format(instance.get('title')))
