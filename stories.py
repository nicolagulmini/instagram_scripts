#!pip install instagrapi

''' 
    The usage of this program makes sense only if you have a public profile with public stories available at the moment.
'''

from instagrapi import Client

USERNAME = input('username: ')
PASSWORD = input('password: ')

cl = Client()
print('Try to connect...')
cl.login(USERNAME, PASSWORD)

user_id = cl.user_info(cl.user_id).pk
print('Hi, your user id is:', user_id)

print('Start to count your followers...')
followers = cl.user_followers(cl.user_id)
followers_usernames = []
for el in followers:
    followers_usernames.append(followers[el].username)
print('Done. You have', len(followers_usernames), ' followers right now.')

print('Start to analyze the insta stories:')
stories = cl.user_stories(user_id)
if len(stories) == 0: print('You have no stories.')
i = 1
for story in stories:
    print('Story number', i, ', these are the followers who are spying you:')
    cond = True
    for user in cl.story_viewers(story.pk):
        if user.username not in followers_usernames: 
            print(user.username)
            cond = False
    if cond: 
        print('Nobody is spying you... for now.')
    print()
