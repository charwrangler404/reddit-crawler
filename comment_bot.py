#/usr/local/bin/python3

import praw
import re

### Crisis_Bot ver 0.1
### Author: /u/alkaloid_android


def reply(comment):
    reply_text = """
    
    Reply text here
    
"""
    comment.reply(reply_text)

def summon_search(subreddit):
    pattern = re.compile('!crisisbot')
    ### Grab comments as they appear
    for comment in subreddit.stream.comments(skip_existing=True):
        # Check for the bat signal
        if pattern.search(str(comment.body.lower())) != None:
            ### Reply to the comment
            reply(comment)
            ### Print comment body to the console - helps track that the scipt
            ### is working
            print(comment.body)

def main():

    ### Access variables defined
    agent = 'web:com.github.crisis_bot:0.1 (by /u/alkaloid_android)'

    ### Open session
    reddit = praw.Reddit(Crisis_Bot, user_agent=agent)

    ### Define subreddit
    subreddit = reddit.subreddit('crisisbot')

    ### Summon the bot!
    summon_search(subreddit)

if __name__ == '__main__':
    main()
