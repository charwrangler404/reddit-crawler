#/usr/local/bin/python3

import praw
import re

### Crisis_Bot ver 0.1
### Author: /u/alkaloid_android


def reply(comment):
    reply_text = """#So you need immediate attention:
- If you feel you are a danger to yourself or others, please call 911 or your local emergency services
- US National Suicide Prevention Hotline: 1-800-273-8255
- Crisis text line: 741-741
- Veterans Crisis Line: 1-800-273-8255, press 1
- [Worldwide Crisis Lines](https://en.m.wikipedia.org/wiki/List_of_suicide_crisis_lines)


#So you're hallucinating
Your hallucinations are in your head, and are not a reflection of reality. Every
person experiences hallucinations differently. They only have the power over you
that you allow them. Hallucinations can be scary, but they cannot hurt you by
themselves. Call your doctor and tell them about your hallucinations. Your doctor
is the best equipped to support *you*, as they have your medical history. If you
are experiencing command hallucinations or your hallucinations are telling you
to kill yourself, it may be time to go to the hospital.


#So you're in crisis:
That's okay. Everyone needs help from time to time. The important thing is to keep
yourself safe. If you are in immediate danger, **call 911 in the US, or your local
emergency services**, and request officers with **Crisis Intervention Training**.
Don't be afraid, they are here to help you.


# So you're going to the hospital:
In a time of crisis, it's important to have people you can depend on to call.
Good friends will help you get yourself to a hospital or some other safe place.
If you have no transportation to the hospital, emergency services will be able
to get you there.

If you end up going to the hospital, you may be staying for a couple days. Pack
comfortable clothes without strings, and a pair of slippers. Sharp objects and
razors are generally not permitted. Another good thing to have with you is a list
of phone numbers for people you want to contact or visit you. You will likely have
access to a phone, but many hospitals will lock up your cell phone. If you have
medications, bring the bottles with you. You may not have access to them, but
it will give the doctors and nurses something to go off of. If you have recently
changed medications, bring both the new and old prescriptions with you. Psychiatric
medications sometimes have the potential side effect of causing suicidal thoughts.


#So your crisis is over:
Those of us who make it through our crisis still need outside support. Often doctors
will recommend an outpatient treatment program. Even if they don't, here are some
resources to help you.

- [National Alliance on Mental Illness](https://www.nami.org) (US)
- [Hearing Voices Network](https://www.hearing-voices.org) (Worldwide)
- [Mental Health Services Near You](https://www.google.com/search?q=mental+health+services+near+me)


*Please submit bug reports at /r/CrisisBot*

*Contact /u/alkaloid_android with major problems*
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
    id = ''
    agent = 'web:com.github.crisis_bot:0.0.1 (by /u/alkaloid_android)'
    name = ''
    pw = ''

    ### Open session
    reddit = praw.Reddit(client_id=id,client_secret=secret,user_agent=agent,username=name,password=pw)

    ### Define subreddit
    subreddit = reddit.subreddit('crisisbot')

    ### Summon the bot!
    summon_search(subreddit)

if __name__ == '__main__':
    main()
