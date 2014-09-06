#!/bin/bash
# Projects list

[ `hostname` != production.impact.com ] && ls ~/Projects && exit 0
[ `hostname` == seaman-sws ] && cat $pt/projects.correct && exit 0

ls ~/Projects

