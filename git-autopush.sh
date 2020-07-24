#!/bin/sh
git pull origin master
git add .
git commit -m "Update Python Quiz Project at `date +%F-%T`"
git push -f origin master