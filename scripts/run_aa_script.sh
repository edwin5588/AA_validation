#!/bin/bash


tar -xf /home/data_repo/$1.tar.gz
cp $2 /home/programs/mosek/8/licenses/
cp $2 /home/programs/mosek/
cp $2 /root/mosek/mosek.lic
export MOSEKLM_LICENSE_FILE=$2 >> ~/.bashrc && source ~/.bashrc

MOSEKLM_LICENSE_FILE=/home/programs/mosek/8/licenses
export MOSEKLM_LICENSE_FILE
BAMFILE=$3
bambase="$(basename -- $BAMFILE)"
BEDFILE=$4
bedbase="$(basename -- $BEDFILE)"
BAIFILE=$6
baibase="$(basename -- $BAIFILE)"

mv $3 /home/input/
mv $4 /home/input/
mv $6 /home/input/

bam="/home/input/$bambase"
bed="/home/input/$bedbase"
bai="/home/input/$baibase"


python2 /home/AA/AmpliconArchitect.py --bam $bam --bed $bed --out $5 --ref $1
