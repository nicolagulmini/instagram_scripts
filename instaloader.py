# Get instance
import instaloader

L = instaloader.Instaloader()

# Login or load session
username = "username"
password = "password"
L.login(username, password)

# Obtain profile metadata
my_profile = instaloader.Profile.from_username(L.context, username)

'''
# Print list of followees
follow_list = []
count = 0
for follower in profile.get_followers():
    print(follower.username)
'''

for story in L.get_stories():
    if story.owner_id == my_profile.userid:
        for item in story.get_items():
            print(item)