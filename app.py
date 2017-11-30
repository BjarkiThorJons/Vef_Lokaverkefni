from bottle import *
from beaker.middleware import SessionMiddleware
session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data2',
    'session.auto': True
}
app = SessionMiddleware(app(), session_opts)

@route('/')
def verslun():
    return template('templates/index.tpl')
@route('/rsadea', method="POST")
def d():
    session=request.environ.get('beaker.session')
    vara_nafn="vara"
    vara_nafn2="vara2"
    fjoldi=request.forms.get('fjoldi')
    session[vara_nafn]=session.get(vara_nafn,0)+int(fjoldi)
    session.save()
    print(session)

    redirect('/')

@route('/karfa', method="POST")
def karfa():
    listi = ["vara", "vara2"]
    session = request.environ.get('beaker.session')
    karfan = []
    for x in session:
        if x in listi:
            hlutur = {}
            hlutur[x] = session[x]
            karfan.append(hlutur)
            print(x)
            print(session[x])
    print(karfan)
    return template('templates/karfa.tpl',posts=karfan)

run(app=app)