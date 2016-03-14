from bottle import run, get, post, view, request, redirect, route, static_file
import threading

messages = [("Nobody", "Hello!")]
nick = "Nobody"


@route('/<nome>')
@view('index')
def index(nome='Nobody'):
    return {'messages': messages, 'nick': nick}


@get('/')
@view('index')
def index():
    return {'messages': messages, 'nick': nick}


@post('/send')
def sendMessage():
    #global nick
    m = request.forms.get('message')
    n = request.forms.get('nick')
    messages.append([n, m])
    #nick = n
    redirect('/'+n)


#para rodar a thread
#threading.Thread(target=run, kwargs=dict(host='localhost', port=8080)).start()

run(host='localhost', port=8080)
#tanto a thread como o servidor compartilham as mesmas variáveis
#manda conectar em várias portas para fazer os testes
#localmente basta conhecer as portas.
#cada servidor tem a sua lista de portas que conhece

