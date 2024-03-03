# Функция для обработки хабов

def extract_text_after_titleHtml(text):
    pattern = r"'titleHtml': '([^']+)'"
    matches = re.findall(pattern, text)
    return matches
result = extract_text_after_titleHtml(big_frame['hubs_pro'][0])
print(result)

# Извлечение текста из HTML текста

def extract_text_before_p(text):
    pattern = r'([^<]+)</p>'
    matches = re.findall(pattern, text)
    return matches
test = big_frame['text'][0]
print(extract_text_before_p(test))

# Убираем тэги из HTML текста, которые остались и которые не были обработаны с помощью регулярных выражений

def remove_html_tags(text):
    clean = re.compile('<[^>]*?>') # re.sub(r'<[^>]*?>', '', value)
    return re.sub(clean, '', text)
test = big_frame['text'][0]
result = extract_text_before_p(test)
print(result)

# Функция для изъятия текста из HTML текста без регулярок и доп обработки с помощью Beautiful Soup 

def text_pars(soup):
    text_full = ''
    text = soup.find_all('p')
    for i in range(len(text)):
        text_full = text_full + text[i].text
    return text_full
text_pars(soup_1)

# Функция для обработки текста для последующей векторизации
noise = stopwords.words("russian") + stopwords.words("english") + list(punctuation) # шум
col  = 'title' # либо 'text'
def text_clean(fr, col: str):
    for i in tqdm(fr.index):
        fr[col][i] = word_tokenize(str(fr[col][i])) # разбиваем на токены
        t = fr[col][i]
        t1 = [x for x in t if x not in noise] # убираем пунктуацию и стоп-слова
        t2 = mystem_analyzer.lemmatize(' '.join(str(j) for j in t1)) # лемматизируем
        t3 = ''.join(str(k) for k in t2)
        fr[col][i] = t3
    return fr

#Соединяем текст и название статьи
col = ['article', 'title', 'text']
def (fr, col):
    fr[col[0]] = '' # создаем столбец с НАЗВАНИЕ СТАТЬИ + ТЕКСТ СТАТЬИ
    for i in tqdm(fr.index):
        fr[col[0]][i] = fr[col[1]][i] + fr[col[2]][i]
        

# Функция для подсчета топов-хабов
def hub_count(fr, hubs:str):
    _count = dict()

    for _list in fr[hubs]:
        for i in _list:
            if i not in _count:
                _count[i] = 1
            else:
                _count[i] += 1

    _count = {k: v for k, v in sorted(_count.items(), key=lambda item: item[1], reverse=True)}
    df = pd.DataFrame.from_dict(_count, orient='index', columns = ['count']).reset_index()
    return df

hub_count(fr, 'hubs_pro')

# Функция для подсчета количества топов-хабов в статье
col_name = 'hubs'
col_name_new = 'top_hub'
def top_count_article_hub(fr, col_name_new, col_name):
    fr[col_name_new] = 0

    for i in tqdm(fr.index):
        for j in tops:
            if j in fr[col_name][i]:
                fr[col_name_new][i] += 1
    return fr

# Функция для отбора одного хаба в статье из топа хабов

col_name = ['hubs', 'top_hub']
col_name_new = 'top_hub_label'
def top_count_article_hub(fr, col_name_new, col_name):

    fr_top[col_name_new] = 0

    for i in tqdm(fr_top.index):
        _list = []
        for j in tops:
            if j in fr_top[col_name[0]][i]:
                fr_top[col_name[1]][i] += 1
                _list.append(j)
        if fr_top[col_name[1]][i] == 0:
            fr_top[col_name_new][i] = ''
        elif fr[col_name[1]][i] > 0:
            fr_top[col_name_new][i] = _list

    return fr_top




