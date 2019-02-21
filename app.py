from flask import Flask, request, render_template

from dbconnection import DBconnection

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def post_form():
    if request.method == "GET":
        return render_template("app.html")
    else:
        db = DBconnection()
        if request.form["submit"] == "search_tester":
            table = "testers"
            country = request.form["country"]
            device = request.form["device"]
            #print(len(country))
            if country == "":
                sql = 'SELECT * FROM {}'.format(table)
            elif len(country) == 2:
                country = "'" + country + "'"
                sql = 'SELECT * FROM {} WHERE country = {}'.format(table, country)
            else:
                list_country = country.split(",")
                #print(list_country)

                sql = "SELECT * FROM {} WHERE country IN {}".format(table,tuple(list_country))

            #print(sql)
            try:
                db.cursor.execute(sql)
            except Exception:
                return render_template("app.html", err = 'podaj poprawne dane')

            results = []
            resultsInfo = []
            for record in db.cursor:
                text1= "tester " + record[1] +" "+ record[2]
                print(text1)
                text2 = " for device o ID " + device
                bugs = devices(record[0], device)
                resultsInfo.append(text1 + text2 + bugs)
                results.append(bugs)
            return render_template('app_result.html', result = resultsInfo)


def devices(user_id, device_id):
    #print(user_id, device_id)
    list_deviceId = device_id.split(",")

    if device_id == "":
        sql = 'SELECT * FROM bugs WHERE testerId = {}'.format(user_id)
    elif len(list_deviceId)>1:
        for id in list_deviceId:
            try:
                int(id)
            except ValueError:
                return " - not able to check - wrong input "

        sql = 'SELECT * FROM bugs WHERE testerId = {} AND ' \
          'deviceId IN {}'.format(user_id, tuple(list_deviceId))
    else:
        try:
            int(device_id)
        except ValueError:
            return " - not able to check - wrong input "

        sql = 'SELECT * FROM bugs WHERE testerId = {} AND ' \
          'deviceId = {}'.format(user_id, device_id)
    db = DBconnection()
    db.cursor.execute(sql)
    bugs = []
    for record in db.cursor:
        bugs.append(record)
    text3 = " filled " + str(len(bugs)) + " bugs"
    print(bugs)
    return text3

app.run()


