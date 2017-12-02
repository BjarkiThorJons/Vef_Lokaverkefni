from bottle import *
from pymysql import *
db=Connect(host="tsuts.tskoli.is",user="0207002620",password="snotra2000",db="0207002620_vef_lokaverkefni")
cursor=db.cursor()
cursor.execute("select * from notendur")

numrows=int(cursor.rowcount)
users={}
for i in range(numrows):
    row=cursor.fetchone()
    if row:
        users[row[0]]=row[1]
@route("/")
def index():
    return template("templates_login/index.tpl")
@route('/login' ,method="POST")
def login():
    cursor = db.cursor()
    cursor.execute("select * from notendur")
    numrows = int(cursor.rowcount)
    users = {}
    for i in range(numrows):
        row = cursor.fetchone()
        if row:
            users[row[0]] = row[1]
    notendanafn=request.forms.get("notendanafn")
    lykilord=request.forms.get("lykilord")
    submit=request.forms.get("submit")
    if notendanafn=="":
        villa={"villa":"Vantar notendanafn"}
        return template("templates_login/villa.tpl",villa)
    elif lykilord=="":
        villa={"villa":"Vantar lykilord"}
        return template("templates_login/villa.tpl",villa)
    elif submit=="Sign-up":
        for x in users:
            if notendanafn == x:
                villa={"villa":"Notendanafn í notkun"}
                return template("templates_login/villa.tpl",villa)
        cursor.execute("""insert into notendur(nafn,lykilord) values(%s,%s)""",(notendanafn,lykilord))
        db.commit()
        cursor.close()
        redirect("/skjakort")
    for x in users:
        if notendanafn==x and lykilord==users[x]:
            redirect("/skjakort")
    else:
        villa={"villa":"Notendanafn eða/og lykilorð rangt"}
        return template("templates_login/villa.tpl",villa)

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
        link=""
        for x in vara["nafn"]:
            if x==" ":
                x="-"
            link+=x.lower()
        vara["link"]=link
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
    for x in vorur:
        ord = skraning

        if ord.lower() in x["nafn"].lower():
            leita.append(x)

        if ord.lower() == x["hopur"]:
            return redirect("/{result}".format(result = x["hopur"]))

    return template("template/results.tpl", posts = leita)

@route("/<vara>")
def vara(vara):
    for x in vorur:
        if vara==x["link"]:
            return template("template/vara.tpl",posts=x)

@route('/myndir/<filename>')
def server_static(filename):
    return static_file(filename, root="myndir")

@route('/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='css')

run(host='localhost', port=8080, debug=True)