## Сбор данных
Парсинг осуществляли перебором значений id по ссылке **habr.com/kek/v2/articles/{id}**, где id - это номер публикации.
[Парсер](new_parser.ipynb) загружен в репозиторий.

## Описание данных

Полученные данные будут загружены на [диск]() в формате .csv. 

Название файла: **habr_{id_start}_{id_end}.csv**, где **id_start** - начальное значение id, **id_end** - конечное значение id.

| Параметр | Описание |
| --- | --- |
| id | id публикации | 
| is_corporative | Корпоративная ли публикация|
| posttype | Тип публикации | 
| title | Заголовок публикации | 
| hubs_pro | Профильные хабы, указанные в публикации (непосредственно связаны с IT). Это список из словарей, в каждом словаре содержатся следующие ключи: 'id' - id хаба, 'alias' - название хаба, 'type' - тип хаба, 'title' и 'titleHtml' - заголовок хаба, 'isProfiled' - профильный ли хаб (True). |
| hubs_nopro | Непрофильные хабы, указанные в публикации. Это список из словарей, в каждом словаре содержатся следующие ключи: 'id' - id хаба, 'alias' - название хаба, 'type' - тип хаба, 'title' и 'titleHtml' - заголовок хаба, 'isProfiled' - профильный ли хаб (False). |
| tags | Теги, указанные в публикации  |
| time_published | Дата и время публикции |
| bookmarks | Количество добавлений в закладки | 
| comments_count | Количество комментариев | 
| views | Количество просмотров публикации |
| votes | Количество голосов за публикацию |
| possitive_votes | Количество положительных голосов за публикацию |
| negative_votes | Количество отрицательных голосов за публикацию |
| reading_time | Время чтения публикации |
| lang | Язык публикации |
| author_username | Ник автора |
| author_id | id автора |
| karma | Карма автора |
| karma_votes | Количество голосов за карму автора |
| rating | Рейтинг автора |
| text | Текст публикации |