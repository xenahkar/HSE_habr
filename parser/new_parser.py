#!/usr/bin/env python
# coding: utf-8

# # **Парсер для Хабра**

# In[1]:


import json
import requests
from tqdm import tqdm
import pandas as pd


def parser(i):
    url = f'https://habr.com/kek/v2/articles/{i}'
    r = requests.get(url)
    if r.status_code == 200:

        article = json.loads(r.text)
        # id публикации
        id = article['id']
        # корпоративный пост
        is_corporative = article['isCorporative']
        # тип публикации
        posttype = article['postType']
        # заголовок
        title = article['titleHtml']
        # профильные хабы
        hubs_pro = []
        for hub in article['hubs']:
          if hub['isProfiled']==True:
            hubs_pro.append(hub)
        # непрофильные хабы
        hubs_nopro = []
        for hub in article['hubs']:
          if hub['isProfiled']==False:
            hubs_nopro.append(hub)
        # теги
        tags = article['tags']
        # время публикации
        time_published = article['timePublished']
        # количество закладок
        bookmarks = article['statistics']['favoritesCount']
        # количество комментариев
        comments_count = article['statistics']['commentsCount']
        # количество просмотров
        views = article['statistics']['readingCount']
        # количество голосов за рейтинг публикации
        votes = article['statistics']['score']
        # положительные голоса за рейтинг публикации
        possitive_votes = article['statistics']['votesCountPlus']
        # отрицательные голоса за рейтинг публикации
        negative_votes = article['statistics']['votesCountMinus']
        # время чтения
        reading_time = article['readingTime']
        # язык публикации
        lang = article['lang']
        # теги
        tags = ','.join(tuple(tag['titleHtml'] for tag in article['tags']))
        # информация об авторе (ник, айди автора, карма, голоса за карму, рейтинг автора)
        author_name = article['author']['alias']
        author_id = article['author']['id']
        karma = article['author']['scoreStats']['score']
        karma_votes  =article['author']['scoreStats']['votesCount']
        rating = article['author']['rating']
        # текст публикации
        text = article['textHtml']
        data = {'id': id,
                'is_corporative': is_corporative,
                'posttype': posttype,
                'title': title,
                'hubs_pro': hubs_pro,
                'hubs_nopro': hubs_nopro,
                'tags': tags,
                'time_published': time_published,
                'bookmarks': bookmarks,
                'comments_count': comments_count,
                'views': views,
                'votes': votes,
                'possitive_votes': possitive_votes,
                'negative_votes': negative_votes,
                'reading_time': reading_time,
                'lang': lang,
                'tags': tags,
                'author_name': author_name,
                'author_id': author_id,
                'karma': karma,
                'karma_votes': karma_votes,
                'rating': rating,
                'text': text}
        return data
    else:
        None


# In[2]:


def get_parseHabr_list(id_start, id_end):
    parseHabr_list = list()
    for i in tqdm(range(id_start, id_end)):
        p = parser(i)
        if p is not None:
            parseHabr_list.append(p)
    return  parseHabr_list


def save_csv(id_start, id_end):
    result = get_parseHabr_list(id_start, id_end)
    parseHabr_df = pd.DataFrame(result)
    parseHabr_df.to_csv(f'habr_{id_start}_{id_end}.csv', index=False)
    return parseHabr_df

