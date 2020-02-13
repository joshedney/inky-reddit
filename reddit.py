import praw
import os
from dotenv import load_dotenv


load_dotenv()

# Create the Reddit client
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
)

def hot_posts(subreddit, limit):
    posts = []
    n = 0
    for p in reddit.subreddit(subreddit).hot(limit=limit):
        post = {}
        post['id'] = n
        post['author'] = p.author.name
        post['title'] = p.title
        posts.append(post)
        n += 1

    return posts