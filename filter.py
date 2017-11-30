# Filter

from bottle import *
from pymysql import *



db=Connect(host="tsuts.tskoli.is",user="0207002620",password="snotra2000",db="0207002620_vef_lokaverkefni")
cursor=db.cursor()
cursor.execute("select * from vorur")
leita = []
vorur = []
numrows=int(cursor.rowcount)
for i in range(numrows):
    row=cursor.fetchone()
    if row:
        vara = {}
        vara["nafn"] = row[0]
        vara["verð"] = row[1]
        vara["hopur"] = row[2]
        vara["lysing"] = row[3]
        vara["myndir"] = row[4]
        vorur.append(vara)
        '''vorur[row[0]] = vara'''


@route("/skjakort")
def filter():
    val = []
    for x in vorur:
        if x["hopur"] == "skjakort":
           val.append(x)
    return template("template/filter_display.tpl", posts = val)

@route("/turnkassar")
def skjakort():
    val = []
    for x in vorur:
        if x["hopur"] == "turnkassar":
           val.append(x)
    return template("template/filter_display.tpl", posts = val)

@route("/check", method="POST")
def check():
    global skraning
    skraning = request.forms.get("search")
    leita = []
    hopur = False
    for x in vorur:
        ord = skraning

        if ord.lower() in x["nafn"].lower():
            leita.append(x)

        if ord.lower() == x["hopur"]:
            hopur = True
            return redirect("/{result}".format(result = x["hopur"]))

    return template("template/results.tpl", posts = leita)



@route('/myndir/<filename>')
def server_static(filename):
    return static_file(filename, root="myndir")

@route('/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='css')

run(host='localhost', port=8080, debug=True)