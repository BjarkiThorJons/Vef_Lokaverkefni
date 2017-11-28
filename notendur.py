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
        redirect("/Velkominn")
    for x in users:
        if notendanafn==x and lykilord==users[x]:
            redirect("/Velkominn")
    else:
        villa={"villa":"Notendanafn eða/og lykilorð rangt"}
        return template("templates_login/villa.tpl",villa)

@route('/Velkominn')
def login():
    return template("templates_login/leynisida.tpl")

@route('/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='css')

run(host='localhost', port=8080, debug=True)