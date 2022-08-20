import flask
from flask import json

from function import get_title_db, get_years_db, get_rating, get_genre

app = flask.Flask(__name__)


@app.get("/movie/<title>")
def views_title(title):
    a = get_title_db(title)
    return app.response_class(
        response=json.dumps(a,
                            ensure_ascii=False,
                            indent=4
                            ),
        status=200,
        mimetype="application/json"
    )


@app.get("/movie/<int:year1>/to/<int:year2>")
def views_year(year1, year2):
    a = get_years_db(year1, year2)
    return app.response_class(
        response=json.dumps(a,
                            ensure_ascii=False,
                            indent=4
                            ),
        status=200,
        mimetype="application/json"
    )


@app.get("/rating/<rating>")
def views_rating(rating):
    a = get_rating(rating)
    return app.response_class(
        response=json.dumps(a,
                            ensure_ascii=False,
                            indent=4
                            ),
        status=200,
        mimetype="application/json"
    )


@app.get("/genre/<genre>")
def views_genre(genre):
    a = get_genre(genre)
    return app.response_class(
        response=json.dumps(a,
                            ensure_ascii=False,
                            indent=4
                            ),
        status=200,
        mimetype="application/json"
    )



if __name__ == '__main__':
    app.run(host='127.0.0.2', port=8001, debug=True)
