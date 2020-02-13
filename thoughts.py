import os
import random
from reddit import hot_posts


quantity = 50

result = hot_posts('showerthoughts', quantity)
uid = random.randint(0, quantity - 1)

for r in result:
    if r['id'] == uid:
        print(r['title'])
        print(r['author'])
