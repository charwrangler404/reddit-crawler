#/usr/local/bin/python3

import praw

def reply(comment):
    reply_text = """
- If you feel you are a danger to yourself or others, please call 911 or your local emergency number
- US National Suicide Prevention Hotline: 1-800-273-8255
- Crisis text line: 741-741
- Veterans Crisis Line: 1-800-273-8255, press 1

*Fully automated*

*Please submit bug reports at /r/CrisisBot*

*Contact /u/alkaloid_android with major problems*
"""
    comment.reply(reply_text)

def summon_search(subreddit):
    ### Grab comments as they appear
    for comment in subreddit.stream.comments(skip_existing=True):
        # Check for the bat signal
        if str(comment.body.lower()[0:10]) == '!crisisbot':
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
    subreddit = reddit.subreddit('SchizoaffectiveBot')

    ### Summon the bot!
    summon_search(subreddit)

if __name__ == '__main__':
    main()
