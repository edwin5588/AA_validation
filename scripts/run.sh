#!/bin/bash

tar -xf data_repo/$1.tar.gz
COPY $2 /programs/mosek/8/licenses/
python2 /home/AA/AmpliconArchitect.py --bam $3 --bed $4 --out $5 --ref $1
