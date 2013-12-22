#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 
#  create_schedule.py
#  pauclair.github.io
#  
#  Created by Pierre AUCLAIR on 2013-12-21.
#  Copyright 2013 Pierre AUCLAIR. All rights reserved.
# 

import sys
import sqlite3 as lite
import codecs

from BeautifulSoup import BeautifulSoup, Tag

connection = None

try:
   connection = lite.connect('/Users/pa/Library/Safari/LocalStorage/file__0.localstorage')
   cursor = connection.cursor()
   cursor.execute('SELECT value FROM ItemTable where key="planning"')
   data = cursor.fetchone()
   planning_string = unicode(data[0], 'utf-16', errors='ignore')
   cursor.close()
   soup = BeautifulSoup(open("../planning.html"))
   planning = soup.find(id='planning')
   planning.clear()
   new_soup = BeautifulSoup(planning_string)
   planning.append(new_soup)
   file = codecs.open("../planning.html", 'w').write(str(soup.prettify()))

except lite.Error, e:
   print "Error %s:" % e.args[0]
   raise e
finally:
   if connection:
      connection.close()