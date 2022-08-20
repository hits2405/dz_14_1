from load_db import connection_date_base


def get_title_db(title):
    sql = f'''select title, country, release_year, listed_in as genre, description
            from netflix
            where title = '{title}'
            order by release_year desc
            limit 1         
            '''
    a = connection_date_base(sql)
    for i in a:
        return dict(i)


def get_years_db(year1, year2):
    sql = f'''select title,release_year
            from netflix
            where release_year between {year1} and {year2}
            limit 100           
            '''
    a = connection_date_base(sql)
    lists = []
    for i in a:
        lists.append(dict(i))
    return lists


def get_rating(rating):
    dicts = {
        "children": ("G"),
        "family": ("G", "PG", "PG-13"),
        "adult": ("R", "NC-17")
    }
    sql = f'''
            select title, rating, description
            from netflix
            where rating in {dicts.get(rating, ("G", "NC-17"))}'''
    a = connection_date_base(sql)
    lists = []
    for i in a:
        lists.append(dict(i))

    return lists


def get_genre(genre):
    sql = f'''select title, description
            from netflix
            where listed_in like '%{str(genre).title()}%'        
            '''
    a = connection_date_base(sql)
    lists = []
    for i in a:
        lists.append(dict(i))

    return lists


