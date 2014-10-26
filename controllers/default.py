# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - api is an example of Hypermedia API support and access control
#########################################################################

import config
import pylintanalzyer
import authormapper
import filehelper

def fusion():
    """ """
    info = config.create_preferences()
    path = info['arjun']['plumbum']
    #path = info['jason']['plumbum']
    code_base = path + '/plumbum/cli'

    files = filehelper.find_python_files_in_project(code_base)
    git = authormapper.get_git_analysis(path, files)
    print 'DONE GIT'
    pylint = pylintanalzyer.get_pylint_analysis(files)
    print 'DONE PYLINT'
    solution = {}
    print 'START'
    for element in git:
        print 'ELEMENT:'
        for file_name in element:
            solution[file_name] = {}
            print 'FILE_NAME:', file_name
            if file_name in pylint:
                print 'INSIDE PYLINT'
                for line_number in element[file_name]:
                    print "GIT", line_number, element[file_name][line_number]['code']
                    if (line_number in pylint[file_name]):
                        print "PYLINT", line_number, pylint[file_name][line_number]
                        solution[file_name][line_number] = {'category':pylint[file_name][line_number]['category'],
                                                            'color':pylint[file_name][line_number]['color'],
                                                            'author':element[file_name][line_number]['author'],
                                                            'code':element[file_name][line_number]['code']}
                    else:
                        solution[file_name][line_number] = {'category':'N',
                                                            'color':'black',
                                                            'author':element[file_name][line_number]['author'],
                                                            'code':element[file_name][line_number]['code']}
            else:
                solution[file_name][line_number] = {'category':'N',
                                                    'color':'black',
                                                    'author':element[file_name][line_number]['author'],
                                                    'code':element[file_name][line_number]['code']}

    print solution
    return solution

def index():
    path_to_root = {"Arjun" : "/home/asumal/git/cs410", "Jason" : "/Users/jasonpinto"}

    name, path = "plumbum", "%s/plumbum" % (path_to_root["Arjun"])
    #name, path = "plumbum", "%s\plumbum\plumbum" % (path_to_root["Jason"])

    # obtain the file structure of the code base
    plumbum_structure = Code_Structure(name, path)
    code_structure = plumbum_structure.get_path()
    print "code structure\n", code_structure

    # give first analyzer the code base information
#    plumbum_pylint = Pylint_Analyzer(name, path)
#    analysis = plumbum_pylint.get_analysis()
#    for key in analysis:
#        print key

    return dict(message=T('Hello World'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_login() 
def api():
    """
    this is example of API with access control
    WEB2PY provides Hypermedia API (Collection+JSON) Experimental
    """
    from gluon.contrib.hypermedia import Collection
    rules = {
        '<tablename>': {'GET':{},'POST':{},'PUT':{},'DELETE':{}},
        }
    return Collection(db).process(request,response,rules)
