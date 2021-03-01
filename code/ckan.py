import json
import ckanapi
from ckanapi import RemoteCKAN, NotAuthorized
import urllib.request

import time

import urllib.request
import cchardet

def group_list(url):

    obj = {
        'api': 'group_list',
        'count': 0,
        'results': []
    }

    try:
        apiserver = RemoteCKAN(url)

        rs = apiserver.action.group_list()
        if rs and len(rs) > 0:
            obj['results'].extend(rs)
            
        obj['count'] = len(obj['results'])

    except Exception as e:
        print('group_list ERROR:', e)
    
    return obj

def organization_list(url):

    obj = {
        'api': 'organization_list',
        'count': 0,
        'results': []
    }

    try:
        apiserver = RemoteCKAN(url)

        rs = apiserver.action.organization_list()
        if rs and len(rs) > 0:
            obj['results'].extend(rs)
            
        obj['count'] = len(obj['results'])

    except Exception as e:
        print('organization_list ERROR:', e)
    
    return obj

def organization_show(url, organization):

    obj = {
        'api': 'organization_show',
        'count': 0,
        'results': []
    }

    try:
        apiserver = RemoteCKAN(url)

        rs = apiserver.action.organization_show(
            id=organization
        )
        if rs:
            obj['results'].append(rs)
            
        obj['count'] = len(obj['results'])

    except Exception as e:
        print('organization_show ERROR:', e)
    
    return obj

def tag_list(url):

    obj = {
        'api': 'tag_list',
        'count': 0,
        'results': []
    }

    try:
        apiserver = RemoteCKAN(url)

        rs = apiserver.action.tag_list()
        if rs and len(rs) > 0:
            obj['results'].extend(rs)
            
        obj['count'] = len(obj['results'])

    except Exception as e:
        print('tag_list ERROR:', e)
    
    return obj

def package_search(url, organization):

    obj = {
        'api': 'package_search',
        'count': 0,
        'results': []
    }

    try:
        apiserver = RemoteCKAN(url)

        doLoop = True
        pos = 0
        count = 100
        while doLoop:
            rs = apiserver.action.package_search(
                q="organization:{}".format(organization),
                start=pos,
                rows=count
            )
            if rs:
                n = len(rs['results'])
                if n > 0:
                    obj['results'].extend(rs['results'])
                    pos += n
                else:
                    doLoop = False

            else:
                doLoop = False

        obj['count'] = len(obj['results'])

    except Exception as e:
        print('package_search ERROR:', e)
    
    return obj

def download_resource(url, res_url):

    resource = ''

    try:
        with urllib.request.urlopen(res_url) as res:
            byte = res.read()
            resource = byte.decode(cchardet.detect(byte)['encoding'])

    except Exception as e:
        print('download_resource ERROR:', e)

    return resource
