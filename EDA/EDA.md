В собранном датафрейме 22 столбца и 170547 строк.



**Столбцы с целочисловым типом данных (int64):**
* **id** - id публикации
* **bookmarks** - количество закладок
* **comments_count** - количество комментариев
* **views**  - количество просмотров
* **votes** - финальный рейтинг публикации
* **possitive_votes**  - количество положительных голосов за публикацию
* **negative_votes**  - количество отрицательных голосов за публикацию
* **reading_time**  - время чтения публикации

**Столбцы с логическим типом данных (bool):**
* **is_corporative** - корпоративный ли пост

**Столбцы со строковым типом данных (object):**
* **posttype** - тип публикации
* **title** - заголовок публикации
* **hubs_pro** - профильные хабы (в строке список из словарей)
* **hubs_nopro** - профильные хабы (в строке список из словарей)
* **tags** - теги (в строке теги через запятую)
* **time_published** - дата и время публикации поста
* **lang** - язык публикации
* **author_name** - никнейм автора
* **text** - текст публикации

**Столбцы с числами с плавающей точкой (float64):**

* **author_id** - айди автора
* **karma** - карма автора
* **karma_votes** - количество голосов за карму
*  **rating** - рейтинг автора

**Пропуски в значениях:**

в столбце **reading_time** (3);
в столбцах **author_id, author_name, karma, karma_votes, rating** (69);
в столбце **title** (1).

Минимальный id публикации 310000, максимальный - 773144.





**После очистки данных от выбросов построили диаграммы корреляции**

*На данной визуализации попарной корреляции можно заметить, что самая большая корреляция между просмотрами и закладками, что может иметь свое обоснование, так как эффект масштаба работает здесь в сторону качества, чем больше людей смотрит - тем больше закладок из них добавляет, однако нельзя делать поспешных выводов, так как данная корреляция лишь демонстрация взаимосвязи, но не причинно-следственной далеко, так как количество закладок и просмотров скорее следствие главной причины, а именно контекста, текста, то есть содержания статьи, либо тем, хабов, по которым они были написаны, то есть главный вывод - это то, что закладки и просмотры являются главным индикатором качества статьи на данный момент.*

*Выше обсуждался самый большой коэффициент корреляции между регрессорами, а сейчас нужно рассмотреть коэффициенты связи между регрессорами и таргетом, что на данный момент очень важно, и для подтверждения нашего убеждения можно заметить, что коэффициенты этих взаимосвязей самые большие после того, что обсудили выше, то есть перейдем к примерам.*

*Количество комментариев и рейтинг статьи имеет прямую связь, причем положительную, что очевидно, что при увеличении комментирования статьи повышается и ее рейтинг, ибо мы понимаем, что комментирование - это привлечение внимания читателя, то есть статья выделилась настолько, что ее захотели обсудить.*

*С закладками аналогичное объяснение. А вот с просмотрами мы видим меньшую взимосвязь, то есть само по себе количество просмотров не является лакмусовой бумажкой, ведь на этот показатель могло повлиять разное отвлекающие и привлекающее из разряда хабов и картинок, а как мы отмечали ранее хабы бывают и непрофильные, так как настраиваются автором*

В собранных данных содержатся статьи на русском (ru) и английском языке (en). Оставили только русскоязычные публикации, а затем удалили столбец "lang", так как в нем во всех строках осталось одно и то же обозначение русского языка (ru).

В заголовке есть одно пропущенное значение. Внимательнее посмотрев на эту публикацию, становится понятно, что эта статья содержит заголовок с текстом "NULL", который был записан как NaN. Заменим этот пропуск обратно на ""NULL"" (в кавычках).

*На данной визуализации попарной корреляции можно заметить, что самая большая корреляция между просмотрами и закладками, что может иметь свое обоснование, так как эффект масштаба работает здесь в сторону качества, чем больше людей смотрит - тем больше закладок из них добавляет, однако нельзя делать поспешных выводов, так как данная корреляция лишь демонстрация взаимосвязи, но не причинно-следственной далеко, так как количество закладок и просмотров скорее следствие главной причины, а именно контекста, текста, то есть содержания статьи, либо тем, хабов, по которым они были написаны, то есть главный вывод - это то, что закладки и просмотры являются главным индикатором качества статьи на данный момент.*

*Выше обсуждался самый большой коэффициент корреляции между регрессорами, а сейчас нужно рассмотреть коэффициенты связи между регрессорами и таргетом, что на данный момент очень важно, и для подтверждения нашего убеждения можно заметить, что коэффициенты этих взаимосвязей самые большие после того, что обсудили выше, то есть перейдем к примерам.*

*Количество комментариев и рейтинг статьи имеет прямую связь, причем положительную, что очевидно, что при увеличении комментирования статьи повышается и ее рейтинг, ибо мы понимаем, что комментирование - это привлечение внимания читателя, то есть статья выделилась настолько, что ее захотели обсудить.*

*С закладками аналогичное объяснение. А вот с просмотрами мы видим меньшую взимосвязь, то есть само по себе количество просмотров не является лакмусовой бумажкой, ведь на этот показатель могло повлиять разное отвлекающие и привлекающее из разряда хабов и картинок, а как мы отмечали ранее хабы бывают и непрофильные, так как настраиваются автором*

*Проведенный анализ на зависимость от времени публикации показал, что в данных присутствует определенная доля сезонности, которую для большей эффективности дальнейшей отработки модели следуюет учесть. Таким образом, мы бы хотели добавить переменные, отвечабщие за дни недели и/или месяцы, которые бы отражали влияние данного фактора на количество просмотров и рейтинг публикации, что в свою очередь бы сгладило и уровняло влияние на таргет, сделаы его более приближенным к правде.*

*Так как главным моментом, который мы в данном случае для себя вынесли, является отсутствие прямой зависимости между просмотрами и таргетом, что наталкивает на мысль на дальнейшем этапе при построении модели посмотреть SHAP values для всех переменных, так как на тот момент будет уже произведена токенизация и лемматизация текстовых данных, поэтому будет возможность вычислить с помощью библиотеки влияние каждой переменной, поэтому на данный момент хотим выдвинуть несколько гипотез: 1. На таргет в большей степени влияют хабы, а точнее профильные хабы; 2. Автор и информация про автора будет иметь значение в случае с корпоративными хабами в большей степени, учитывая создание бренда многих IT-корпорация.*

