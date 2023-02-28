from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    id = args.get('id')
    name = args.get('name')
    age = args.get('age')
    occupation  = args.get('occupation')
    
    users = []
    
    id_find = []
    name_find = []
    age_find = []
    occupation_find = []
    
    if args == {}:
        return USERS
    
    for idx, user in enumerate(USERS):
        if id != None:
            if id == user['id']:
                id_find.append((user['id'], idx))
                continue
        if name != None:
            if name.lower() in user['name'].lower():
                name_find.append((user['name'].lower(), idx))
                continue
        if age != None:
            if (int(age) - 1) <= int(user['age']) <= (int(age) + 1):
                age_find.append((int(user['age']), idx))
                continue
        if occupation != None:
            if occupation.lower() in user['occupation'].lower():
                occupation_find.append((user['occupation'].lower(), idx))
                continue
                
    if len(id_find) > 0:
        users.append(USERS[id_find[0][1]])
    
    name_find = sorted(name_find)
    age_find = sorted(age_find)
    occupation_find = sorted(occupation_find)
    
    for e in name_find:
        users.append(USERS[e[1]])
    
    for e in age_find:
        users.append(USERS[e[1]])
    
    for e in occupation_find:
        users.append(USERS[e[1]])
    
    return users
