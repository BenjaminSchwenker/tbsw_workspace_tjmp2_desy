
#!/bin/bash

START=$1
STOP=$2


for run in $(seq $START 1 $STOP); do
    echo "analyzing: run $run"
    if [ $# -eq 4 ]; then
        python3 tj2-reco.py   --runno $run  --gearfile $3 --datapath $4
    else
        echo "Using caltag $4"
        python3 tj2-reco.py   --runno $run  --gearfile $3 --datapath $4 --caltag $5
    fi
done
echo "done"
