
 README.txt
 pauclair.github.io
 
 Created by Pierre AUCLAIR on 2014-02-08.
 Copyright 2014 Pierre AUCLAIR. All rights reserved.

#################################
###  to change a new year
#################################
#remove your local system 
rm -rf _site
#remove your cache 
#rm file__0.localstorage http_localhost_4000.localstorage located in ~/Library/Safari/LocalStorage
rm ~/Library/Safari/LocalStorage/file__0.localstorage ~/Library/Safari/LocalStorage/http_localhost_4000.localstorage

#change _config.yml unexclude generate_schedule, schedule.html

#Change create_period_schedule.py by changind year and adapting periods
#change legend.html
#generate file by starting ./generate_schedule/create_period_schedule.py This creates both planning.html and schedule.html
#Start your local system
bundle exec jekyll serve --watch

start schedule.html on your local system (SAFARI)
update the schedule
save
Launch generate_schedule/create_scedule.py
update git via github





#################################
### To update the web site
#################################

Start your local system
bundle exec jekyll serve --watch

start schedule.html on your local system (SAFARI)
update the schedule
save
Launch generate_schedule/create_scedule.py
update git via github