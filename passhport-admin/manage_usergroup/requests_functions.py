# -*-coding:Utf-8 -*-

"""Contains functions which make requests to the server for usergroup's management"""

import requests

url_passhport = "http://127.0.0.1:5000/"

def requests_usergroup_list():
    """Get the list of all usergroups"""
    url_list = url_passhport + "usergroup/list"

    try:
        r = requests.get(url_list)
    except requests.RequestException, e:
        print("ERROR: " + str(e.message))
    else:
        print(r.text)

        if r.status_code == requests.codes.ok:
            return 0

    return 1

def requests_usergroup_search(pattern):
    """Get the list of usergroups following the pattern"""
    url_search = url_passhport + "usergroup/search/" + pattern

    try:
        r = requests.get(url_search)
    except requests.RequestException, e:
        print("ERROR: " + str(e.message))
    else:
        print(r.text)

        if r.status_code == requests.codes.ok:
            return 0

    return 1

def requests_usergroup_create(usergroupname, comment):
    """Usergroup creation on passhportd via API"""
    usergroup_data = {'usergroupname': usergroupname, 'comment': comment}
    url_create = url_passhport + "usergroup/create"

    try:
        r = requests.post(url_create, data = usergroup_data)
    except requests.RequestException, e:
        print("ERROR: " + str(e.message))
    else:
        print(r.text)

        if r.status_code == requests.codes.ok:
            return 0

    return 1

def requests_usergroup_show(usergroupname):
    """Get data about a usergroup"""
    url_show = url_passhport + "usergroup/show/" + usergroupname

    try:
        r = requests.get(url_show)
    except requests.RequestException, e:
        print("ERROR: " + str(e.message))
    else:
        print(r.text)

        if r.status_code == requests.codes.ok:
            return 0

    return 1

def requests_usergroup_edit(usergroupname, new_usergroupname, new_comment):
    """Usergroup modification on passhportd via API"""
    usergroup_data = {'usergroupname': usergroupname, 'new_usergroupname': new_usergroupname, 'new_comment': new_comment}
    url_edit = url_passhport + "usergroup/edit"

    try:
        r = requests.post(url_edit, data = usergroup_data)
    except requests.RequestException, e:
        print("ERROR: " + str(e.message))
    else:
        print(r.text)

        if r.status_code == requests.codes.ok:
            return 0

    return 1

def requests_usergroup_del(usergroupname):
    """Usergroup deletion on passhportd via API"""
    url_del = url_passhport + "usergroup/del/" + usergroupname

    try:
        r = requests.get(url_del)
    except requests.RequestException, e:
        print("ERROR: " + str(e.message))
    else:
        print(r.text)

        if r.status_code == requests.codes.ok:
            return 0

    return 1
