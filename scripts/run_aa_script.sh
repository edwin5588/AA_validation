#!/bin/sh

tar -xf /home/data_repo/$1.tar.gz
COPY $2 /programs/mosek/8/licenses/
mv "$3" "/home/input/"
mv "$4" "/home/input/"
mv "$6" "/home/input/"
bambase = $(basename $3 .bam)
baibase = $(basename $6 .bai)
bedbase = $(basename $4 .bed)
bam = "/home/input/${bambase}"
bed= "/home/input/${bedbase}"
bai= "/home/input/${baibase}"


python2 /home/AA/AmpliconArchitect.py --bam bam --bed bed --out $5 --ref $1
