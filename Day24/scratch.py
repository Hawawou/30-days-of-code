import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

todos_by_user = {}

for todo in todos:
    if todo["completed"]:
        try:
            # increment the existing user's count
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            todos_by_user[todo["userId"]] = 1

top_users = sorted(todos_by_user.items(),
                   key=lambda x:x[1], reverse=True)

# Get the maximum number of complete TODOs
max_complete = top_users[0][1]

# List of all users who have completes the max number of todos
users = []

for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = "and ".join(users)

# filter out complete todos
def keep(todo):
    is_complete = todo["complete"]
    has_max_count = str(todo['userId']) in users
    return is_complete and has_max_count

with open("filtered_data.json", "w") as data_file:
    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos, data_file, indent=2)