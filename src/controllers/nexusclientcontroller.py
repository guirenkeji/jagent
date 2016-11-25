# -*- coding: UTF-8 -*-
from flask import Module,render_template,jsonify, redirect, request, session, g
# import requests
import os
import logging
import json
logging.basicConfig(level=logging.DEBUG)
#===============================================================================
# NEXUS_REPOS_LAYER 资源库层数 
#  <groupId>com_acme</groupId>
#   <artifactId>disconf</artifactId>
#   <version>2.6.10</version>
#===============================================================================
NEXUS_REPOS_LAYER = 3
nexus = Module(__name__)

@nexus.route('/agent/nexus')
def hello_svn_repo_info():
    return 'Hello agent nexus !'
@nexus.route('/agent/nexus/1.0/push',methods=['POST'])
def pushToNexus ():  
    r = request.json['r']
    g = request.json['g']
    a = request.json['a']
    v = request.json['v']
    p = request.json['p']
    file_name = request.json['file_name']
    file_path = request.json['file_path']
    username = request.json['username']
    password = request.json['password']
    nexus_repos_url = request.json['nexus_repos_url']
#     print os.path.abspath(os.curdir)
    try:
        file_push_repos = os.popen('curl -v \
                            -F "r=%s" \
                            -F "g=%s" \
                            -F "a=%s" \
                            -F "v=%s" \
                            -F "p=%s" \
                            -F "file=@%s/%s" \
                            -u %s:%s \
                            %s/service/local/artifact/maven/content'
                            %(r,g,a,v,p,file_path,file_name,username,password,nexus_repos_url)).readlines()

                 
        if file_push_repos==[] or 'error' in file_push_repos[0] :
            raise ValueError,"file push error :"+file_name                 

    except ValueError as e:
         print e
    
    logging.info(file_push_repos)
    return 'ok'
@nexus.route('/agent/nexus/1.0/pull',methods=['POST'])
def pullToLocal ():
    version = request.josn['version']
    username = request.json['username']
    password = request.json['password']
    nexus_repos_url = request.json['nexus_repos_url']
    push_repos = os.popen('curl -v \
                        -u admin:admin123 \
                        %s/service/local/attributes/pro/com_acme_widgets/content/').readlines()
    
    logging.info(push_repos)
    return 'download'  


if __name__ ==  '__main__':
    print 'test'
#      nexusMetadata()
#     pushToNexus()
#     getNexus()
    
    
    
      