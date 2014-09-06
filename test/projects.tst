#!/bin/bash
# Projects list

[ `hostname` != production.impact.com ] && ls ~/Projects && exit 0

cat $pt/projects.correct
