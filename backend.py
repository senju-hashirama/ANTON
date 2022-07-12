import mysql.connector as msc
con=msc.connect(host='localhost',user='root',passwd='the_guardian_072003',database='project')
cur=con.cursor()

def author_filter():
    cur.execute('select distinct(author) from books_dataset;')
    res=cur.fetchall()
    res.sort()
    temp=[]
    for i in res:
        for j in i:
           temp.extend(j.split(','))
    temp=list(set(temp))
    temp.sort()
    return tuple(temp)

def year_filter():
    cur.execute('select distinct(publication_year) from books_dataset;')
    res=cur.fetchall()
    res.sort()
    temp=[]
    for i in res:
        for j in i:
            if j:
                temp.append(int(j))
    return tuple(temp)

def lang_filter():
    cur.execute('select distinct(language) from books_dataset;')
    res=cur.fetchall()
    res.sort()
    temp=[]
    for i in res:
        for j in i:
            if j:
                temp.append(j)
    return tuple(temp)
    
def avg_rating_filter():
    cur.execute('select distinct(avg_rating) from books_dataset;')
    res=cur.fetchall()
    temp=[]
    for i in res:
        for j in i:
            if j:
                temp.append(float(j))
    temp.sort()
    return tuple(temp)

final_list_authors=('-none-',)+author_filter()
final_list_years=('-none-',)+year_filter()
final_list_lang=('-none-',)+lang_filter()
final_list_ratings=('-none-',)+avg_rating_filter()
