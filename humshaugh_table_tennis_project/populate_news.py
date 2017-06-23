import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humshaugh_table_tennis_project.settings')

import django
django.setup()
from humshaugh_table_tennis.models import News


def populate():

    news = [
        {'title': '2015 SEASON',
         'content': 'iueu weu ef i w weifhu we we hf w iw ef whe',
        },
        {'title': '2016 Season',
         'content': 'efjb wef jwe f webbwe f efb h',
        },
    ]

    for i in range(56):
        for post in news:
            add_post(i, post['content'])


def add_post(title, content):
    p = News.objects.get_or_create(title=title, content=content)[0]
    p.save()
    return p


if __name__ == '__main__':
    print("Starting news population . . .")
    populate()
    for p in News.objects.all():
        print("{0} - {1}".format(p.title, p.content))
