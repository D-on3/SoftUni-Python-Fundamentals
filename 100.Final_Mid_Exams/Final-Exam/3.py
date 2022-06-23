def new_follower(followers_dict, name):
    if name not in followers_dict:
        followers_dict[name] = {'likes': 0, 'comments': 0}
    return followers_dict


def like(followers_dict, name, number):
    if name not in followers_dict:
        followers_dict[name] = {'likes': number, 'comments': 0}
    else:
        followers_dict[name]['likes'] += number
    return followers_dict


def comment(followers_dict, name):
    if name not in followers_dict:
        followers_dict[name] = {'likes': 0, 'comments': 1}
    else:
        followers_dict[name]['comments'] += 1
    return followers_dict


def blocked(followers_dict, name):
    if name not in followers_dict:
        print(f"{name} doesn't exist.")
    else:
        del followers_dict[name]
    return followers_dict


followers = {}

command_data = input()

while not command_data == "Log out":
    data = command_data.split(": ")
    command = data[0]
    username = data[1]

    if command == "New follower":
        followers = new_follower(followers, username)
    elif command == "Like":
        count = int(data[2])
        followers = like(followers, username, count)
    elif command == "Comment":
        followers = comment(followers, username)
    elif command == "Blocked":
        followers = blocked(followers, username)

    command_data = input()

for username, follower_data in followers.items():
    followers[username]['likes_comments'] = followers[username]['likes'] + followers[username]['comments']

sorted_followers = sorted(followers.items(), key=lambda x: (-x[1]['likes_comments'], x[0]))

print(f"{len(followers)} followers")
for username, value in sorted_followers:
    print(f"{username}: {value['likes_comments']}")


