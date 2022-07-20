#!/bin/bash

START=$1
STOP=$2


for run in $(seq $START 1 $STOP); do
    echo "plotting: run $run"
    
    python3 histo-plotter-tj2.py --ifile=root-files/Histos-TJ2-run$run-reco.root  --colstart $3 --colstop $4 --rowstart $5 --rowstop $6

done
echo "done"
