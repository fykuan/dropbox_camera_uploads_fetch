#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dropbox
import json
import re
import sys

apikey = ''
apisecret = ''
accesstoken=''
path = ''

if len(sys.argv) != 2:
    print "Please specify file saving directory"
    sys.exit(0)
else:
    path = sys.argv[1]

try:
    with open('.accesstoken'):
        f_accesstoken = open('.accesstoken', 'r')
        accesstoken = f_accesstoken.read()
except IOError:
    print ".accesstoken not found"
    try:
        with open('apikey.json'):
            f_apikey = open('apikey.json', 'r');
            json_apikey = json.loads(f_apikey.read())
            flow = dropbox.client.DropboxOAuth2FlowNoRedirect(json_apikey['key'], json_apikey['secret'])
            authorize_url = flow.start()
            print '1. Go to: ' + authorize_url
            print '2. Click "Allow" (you might have to log in first)'
            print '3. Copy the authorization code.'
            code = raw_input("Enter the authorization code here: ").strip()
            accesstoken, user_id = flow.finish(code)
            # Write accesstoken to .accesstoken
            f_accesstoken = open ('.accesstoken', 'a+')
            f_accesstoken.write(accesstoken)
    except IOError:
        print "apikey.json not found"
        sys.exit(0)

client = dropbox.client.DropboxClient(accesstoken)

# 取得/Camera Uploads資料夾內容
folder_metadata = client.metadata('/Camera Uploads')

for i in range(0,len(folder_metadata['contents'])):
    abs_filepath = folder_metadata['contents'][i]['path']
    filename = re.match("^.*/(.*)$", abs_filepath).group(1)
    ofile = open(path + "/" + filename, "w+")
    f, metadata = client.get_file_and_metadata(abs_filepath)

    # 寫入檔案
    ofile.write(f.read())
    ofile.close()
    print "dropbox:" + abs_filepath + " has downloaded to " + path + "/" + filename

    # 刪除Dropbox上的檔案
    client.file_delete(abs_filepath)
