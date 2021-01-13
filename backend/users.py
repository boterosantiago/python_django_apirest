import hashlib
import copy

users = [{
    'code': 1,
    'user': 'admin',
    'password': '78b0fb9876ff57129ea2e2c49a1b93d4f8c676c43d89b7c06c2ad4188acafcab',
    'admin': True
}]

def encodePassword(password):
    m = hashlib.sha256()
    m.update(b"%r" %password)
    return m.hexdigest()

def saveUser(user):
    user['password'] = encodePassword(user['password'])
    users.append(user)


def loadUser(id):
    user = None
    for u in users:
        if u['code'] == id:
            user = copy.copy(u)
            break
    if user is not None:
        return user
    else:
        return None


def loadUserName(username):
    user = None
    for u in users:
        if u['user'] == username:
            user = copy.copy(u)
            break
    if user is not None:
        return user
    else:
        return None


def removeUser(user):
    users.remove(user)


def listUsers():
    return users

def auth(username, password):
    user = loadUserName(username)
    if user is None:
        return False
    return user['password'] == encodePassword(password)

def user_auto_code():
    code = 1
    exist = True
    while exist:
        exist = False
        for u in users:
            if u['code'] == code:
                exist = True
                code += 1
                break
    return code