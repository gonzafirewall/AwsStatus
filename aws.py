#!/usr/bin/env python

import urllib2
import BeautifulSoup
import re
import sys
import os

FILE_PATH = os.path.dirname(os.path.abspath(__file__))

def create_example():
    status_url = "http://status.aws.amazon.com"
    r = urllib2.urlopen(status_url)
    print 'Descargando las notificaciones posibles...'
    soup = BeautifulSoup.BeautifulSoup(r.read())
    As = soup.findAll(href=re.compile('rss$'))
    status_url = [a['href'].split('/')[1] for a in As]
    print 'Escribiendo el archivo de configuracion'
    with open('aws_status.conf', 'w+') as f:
        f.write('#MAILS=asd@asd.com\n')
        for stat_url in status_url:
            f.write('#%s\n' % stat_url)
    print 'Por favor descomenta la notificacion que quieras recibir'

def load():
    os.chdir(FILE_PATH)
    if not os.path.exists('data'):
        os.mkdir('data')
    try:
        with open('aws_status.conf') as f:
            print f.read()
    except IOError, e:
        print 'No se encuentra el archivo crealo con el comando "create_example"'

def run():
    pass

if sys.argv[1] == 'create_example':
    create_example()
else:
    print """Usage [create_example]"""

load()
