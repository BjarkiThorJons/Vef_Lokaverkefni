from bottle import *
from pymysql import *
from beaker.middleware import SessionMiddleware
db=Connect(host="tsuts.tskoli.is",user="0207002620",password="snotra2000",db="0207002620_vef_lokaverkefni")
cursor=db.cursor()
cursor.execute("select * from notendur")
session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data2',
    'session.auto': True
}
app = SessionMiddleware(app(), session_opts)
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

@route('/rsadea', method="POST")
def d():
    session=request.environ.get('beaker.session')
    vara=request.forms.get("vara")
    print(vara)
    fjoldi=request.forms.get('fjoldi')
    if int(fjoldi)<0:
        fjoldi=int(fjoldi)*-1
    session[vara]=session.get(vara,0)+int(fjoldi)
    session.save()
    print(session)
    for x in vorur:
        if x["nafn"]==vara:
            linkurinn=x["link"]
    link="/"+linkurinn
    redirect(link)

@route('/karfa', method="POST")
def karfa():
    session = request.environ.get('beaker.session')
    karfan = []
    for x in session:
        for y in vorur:
            if x==y["nafn"]:
                hlutur = {}
                hlutur[x] = session[x]
                karfan.append(hlutur)
                print(x)
                print(session[x])
    print(karfan)
    return template('templates/karfa.tpl',posts=karfan)


@route('/myndir/<filename>')
def server_static(filename):
    return static_file(filename, root="myndir")

@route('/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='css')
run(app=app)