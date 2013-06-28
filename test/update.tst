#!/bin/bash
# Check the platform files

x=~/Projects/jack-hammer


cd $x

# bin  test  app  app/views

for f in `ls bin/* test/*.tst  app/*.js app/views/*.j*`
do
    echo ____________________
    echo $f
    diff $p/$f $x/$f
done

