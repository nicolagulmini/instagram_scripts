#!pip install instagrapi

from instagrapi import Client

USERNAME = None
PASSWORD = None

cl = Client()
cl.login(USERNAME, PASSWORD)

user_id = cl.user_info(cl.user_id).pk

followers = cl.user_followers(cl.user_id)
followers_usernames = []
for el in followers:
    followers_usernames.append(followers[el].username)

stories = cl.user_stories(user_id)
i = 1
for story in stories:
    print('Story number', i, ':')
    for user in cl.story_viewers(story.pk):
        if user.username not in followers_usernames: print(user.username)
    print()
