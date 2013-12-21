#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 
#  create_period_schedule.py
#  Desktop
#  
#  Created by Pierre AUCLAIR on 2013-11-16.
#  Copyright 2013 Pierre AUCLAIR. All rights reserved.
# 

import calendar
import sys
from datetime import datetime
import locale
import codecs
from BeautifulSoup import BeautifulSoup, Tag

# Change year and adapt timetable periods
# period format is mm/dd

year = 2014

class period(object):
    """docstring for period"""
    def __init__(self, startDate, stopDate, color):
        super(period, self).__init__()
        startDate = "%s/%s" %(startDate,year)
        stopDate = "%s/%s" %(stopDate, year)
        self.startDate = datetime.strptime(startDate, '%m/%d/%Y')
        self.stopDate = datetime.strptime(stopDate, '%m/%d/%Y')
        self.color = color
        
    def include(self, date):
        if date>=self.startDate and date<=self.stopDate :
            return self.color
        else :
            return
    
    
class timetable(object):
    """docstring for timetable"""
    def __init__(self):
        super(timetable, self).__init__()
        self.periodArray = [
            period('01/01', '01/03', "green",),
            period('01/04', '04/11', "blue"),
            period('04/12', '04/18', "green"),
            period('04/19', '05/09', "yellow"),
            period('05/10', '05/23', "green"),
            period('05/24', '05/30', "yellow"),
            period('05/31', '06/06', "green"),
            period('06/07', '07/04', "yellow"),
            period('07/05', '07/11', "orange"),
            period('07/12', '08/22', "red"),
            period('08/23', '08/29', "orange"),
            period('08/30', '09/12', "yellow"),
            period('09/13', '09/26', "green"),
            period('09/27', '10/17', "blue"),
            period('10/18', '10/31', "green"),
            period('11/01', '12/19', "blue"),
            period('12/20', '12/31', "green"),
           ]
           
    def periodColor(self, year, month, day):
      dateString = "%02d-%02d-%04d" % (month, day, year)
      searchDate = datetime.strptime(dateString, '%m-%d-%Y')
      for period in self.periodArray:
         periodColor = period.include(searchDate)
         if periodColor is not None:
            return periodColor
        
class TroussCalendar(calendar.LocaleHTMLCalendar):
   def __init__(self, year, locale):
        super(TroussCalendar, self).__init__(year, locale)
        self.timetable = timetable()

   def addJs(self, script=None):
      """docstring for addJs"""
      if script == None:
         return
      string = codecs.open(script, 'r', encoding='utf-8').read()
      return '%s' % string

   def addLegend(self, legend=None):
      """docstring for addLegend"""
      if legend == None:
         return
      string = codecs.open(legend, 'r', encoding='utf-8').read()
      return '%s' % string
   
   def addCss(self, css=None):
      """docstring for addCss"""
      if css == None:
         return
      
      import ipdb
      ipdb.set_trace()
      
      string = codecs.open(css, 'r', encoding='utf-8').read()
      return '%s' % string
     
   
   def formatyear(self, theyear, width=3):
      """
      Return a formatted year as a table of tables.
      """
      v = [] 
      a = v.append
      width = max(width, 1)
      for i in range(calendar.January, calendar.January+12, width):
         a('<div class="row">')
         # months in this row
         months = range(i, min(i+width, 13))
         for m in months:
            a(self.formatmonth(theyear, m, withyear=False))
         a('</div>')
      return ''.join(v)
   
   def formatmonth(self, theyear, themonth, withyear=True):
      """
      Return a formatted month as a table.
      """
      v = []
      a = v.append
      a('<div class="large-3 medium-3 small-12 columns">\n')
      a('<table border="0" cellpadding="0" cellspacing="0" class="month">')
      a('\n')
      a(self.formatmonthname(theyear, themonth, withyear=withyear))
      a('\n')
      a(self.formatweekheader())
      a('\n')
      counter = 0
      for week in self.monthdays2calendar(theyear, themonth):
         a(self.formatweek(week, themonth))
         counter = counter+1
         a('\n')

      if counter < 5:
         a('<tr>\n')
         for i in range(7):
            a('<td class="noday">&nbsp;</td>')
         a('</tr>\n')
      a('</table>')
      a('\n')
      a('</div>')
      return ''.join(v)
    
   def formatday(self, day, weekday, themonth):
      """
      Return a day as a table cell.
      """
      if day == 0:
         return '<td class="noday">&nbsp;</td>' # day outside month
      else:
         return '<td class="%s %s">%d</td>' % (self.cssclasses[weekday], self.timetable.periodColor(year, themonth, day), day)
    
   def formatweek(self, theweek, themonth):
      """
      Return a complete week as a table row.
      """
      s = ''.join(self.formatday(d, wd, themonth) for (d, wd) in theweek)
      return '<tr>%s</tr>' % s
   
   def formatyearpage(self, theyear, width=4, encoding=None, legend=None):
      """
      Return a formatted year as a complete HTML page.
      """
      if encoding is None:
         encoding = sys.getdefaultencoding()
      
      v = []
      a = v.append
      a('<?xml version="1.0" encoding="%s"?>\n' % encoding)
      a('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n')
      a('<html>\n')
      a('<head>\n')
      a('<meta http-equiv="Content-Type" content="text/html; charset=%s" />\n' % encoding)
      a('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
      a('<title>Calendrier pour %d</title>\n' % theyear)
      a('<link rel="stylesheet" href="css/normalize.css" type="text/css">\n')
      a('<link rel="stylesheet" href="css/foundation.css" type="text/css">\n')
      a('<link rel="stylesheet" href="css/trouss.css">\n')
      a('<script src="js/vendor/custom.modernizr.js" type="text/javascript"></script>\n')
      a('</head>\n')
      a('<body>\n')
      a('<div id="planning">\n')
      a('<div class="row deepred">\n')
      a('</div>\n')   
      
      a('<div class="row">\n')
      a('  <div class="large-12 medium-12 small-12 columns">\n')
      a('     <h1 class="text-center">Tarifs %d</h1>\n' %theyear)
      a('  </div>\n')
      a('</div>\n')
      if (legend != None):
         a(self.addLegend(legend))

      a(self.formatyear(theyear, width))
      a('<div class="row deepred">\n')
      a('</div>\n')   
      
      a('</div>\n')
      a('<div class="row">\n')
      a('  <div class="large-3 small-10 columns">\n')
      a('     <a href="./index.html" class="button postfix">Retour</a>\n')
      a('  </div>\n')
      a('</div>\n')
      a('<div class="row">\n')
      a('  <div class="large-3 columns">\n')
      a('     <a href="#" class="button postfix">Planning</a>\n')
      a('  </div>\n')
      a('</div>\n')
      
      a('</body>\n')
      a('</html>\n')
      return ''.join(v)

currentloc = locale.getlocale()
locale.setlocale(locale.LC_ALL, 'fr_FR')
myCal = TroussCalendar (calendar.SATURDAY, locale.getlocale())

schedule = myCal.formatyearpage(year, 4, 'utf-8', "legend.html")
codecs.open("../src/tarifs.html", 'w', encoding='utf-8').write(schedule)
locale.setlocale(locale.LC_ALL, currentloc)
