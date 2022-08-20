from flask import json

from load_db import connection_date_base


" Без вьюшек "


def get_two_actor(name1='Rose McIver', name2='Ben Lamb'):
    sql = f'''select *
                from netflix
                where "cast" like '%{name1}%' and "cast" like '%{name2}%'         
                '''
    result = connection_date_base(sql)
    lmp = []
    names_dict = {}
    for item in result:
        names = set(dict(item).get("cast").split(", ")) - {name1, name2}
        for name in names:
            names_dict[name.strip()] = names_dict.get(name.strip(), 0) + 1

    for key, value in names_dict.items():
        if value > 2:
            lmp.append(key)

    return lmp


print(get_two_actor())


def get_types_films_and_serials(types, year, genre):
    sql = f'''select *
            from netflix
            where type = '{types}' and
            release_year = '{year}' and
            listed_in like '%{genre}%'          
            '''
    a = connection_date_base(sql)
    lists = []
    for i in a:
        lists.append(dict(i))
    return json.dumps(lists,
                      ensure_ascii=False,
                      indent=4
                      ),


print (get_types_films_and_serials(types='TV Show', year='2020', genre='Dramas'))

