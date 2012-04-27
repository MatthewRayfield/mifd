#!/usr/bin/env python

import json
import sys
import urllib
import urlparse

try:
    config_file = open('mifd.json', 'r')
    config_file_text = config_file.read()
    config_file.close()
except:
    sys.exit('could not open mifd.json')

try:
    config_data = json.loads(config_file_text)
except:
    sys.exit('error parsing mifd.json')

files = config_data['files']

for file_data in files:
    source = file_data['source']
    split_source = urlparse.urlsplit(source)
    filename = split_source.path.split('/')[-1]
    sys.stdout.write('downloading %s' % source)
    urllib.urlretrieve(source, filename)
    sys.stdout.write(' done\n')
