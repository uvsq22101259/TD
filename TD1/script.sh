#!/bin/sh

mkdir project2
cd project2
echo "KANGA elie"> README
mkdir data doc module
touch module/core.py module/main.py
touch data/matrix.csv
ls -R > contents.txt
cp -r  . ../projectv2
cd ..
tar -cf pv2.tar project2