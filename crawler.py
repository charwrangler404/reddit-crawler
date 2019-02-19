#/usr/local/bin/python3

import praw

def reply(comment):
    ### Place comment reply here
    reply_text = """
"""
    comment.reply(reply_text)

def summon_search(subreddit):
    ### Grab comments as they appear
    for comment in subreddit.stream.comments(skip_existing=True):
        # Check for the bat signal
        if str(comment.body.lower()[0:10]) == '':
            ### Reply to the comment
            reply(comment)
            ### Print comment body to the console - helps track that the scipt
            ### is working
            print(comment.body)

def main():

    ### Access variables defined
    id = ''
    secret = ''
    agent = ''
    name = ''
    pw = ''

    ### Open session
    reddit = praw.Reddit(client_id=id,client_secret=secret,user_agent=agent,username=name,password=pw)

    ### Define subreddit
    subreddit = reddit.subreddit('')

    ### Summon the bot!
    summon_search(subreddit)

if __name__ == '__main__':
    main()
