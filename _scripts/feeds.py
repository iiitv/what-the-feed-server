import requests

url = 'http://localhost/api/feed/'

def addsubs():
    r = requests.post(url + 'addsubscription', data = {'id': 1, 'password': 'something', 'searchparam': 'Batman vs Superman'})
    print(r.content)

def login():
    r = requests.post(url + 'login', data = {'username': 'aviaryan', 'password': 'something'})
    print(r.content)

if __name__ == '__main__':
    addsubs()
    #login()