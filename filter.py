# Filter

from bottle import *
from pymysql import *



db=Connect(host="tsuts.tskoli.is",user="0207002620",password="snotra2000",db="0207002620_vef_lokaverkefni")
cursor=db.cursor()
cursor.execute("select * from vorur")

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

@route("/")
def filter():
    return template("filter_display.tpl", posts = vorur)


print(vorur)
for x in vorur:
    print(x)

@route('/myndir/<filename>')
def server_static(filename):
    return static_file(filename, root="myndir")

@route('/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='css')

run(host='localhost', port=8080, debug=True)