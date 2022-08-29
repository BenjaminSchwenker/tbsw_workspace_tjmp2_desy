
#!/bin/bash

python3 tj2-reco.py   --runno 451  --gearfile geoid27.xml  --prefix _clustdb
python3 tj2-reco.py   --runno 452  --gearfile geoid27.xml  --prefix _clustdb

python3 tj2-reco.py   --runno 454  --gearfile geoid28.xml  --prefix _clustdb
python3 tj2-reco.py   --runno 453  --gearfile geoid28.xml  --prefix _clustdb

python3 tj2-reco.py   --runno 455  --gearfile geoid29.xml  --prefix _clustdb
python3 tj2-reco.py   --runno 456  --gearfile geoid29.xml  --prefix _clustdb

python3 tj2-reco.py   --runno 460  --gearfile  geoid30.xml  --prefix _clustdb
python3 tj2-reco.py   --runno 459  --gearfile  geoid30.xml  --prefix _clustdb

python3 tj2-reco.py   --runno 461  --gearfile geoid31.xml  --prefix _clustdb
python3 tj2-reco.py   --runno 463  --gearfile geoid31.xml  --prefix _clustdb


# fix planes issue
python3 tj2-reco.py   --runno 464  --gearfile geoid32.xml  --prefix _clustdb
python3 tj2-reco.py   --runno 465  --gearfile geoid32.xml  --prefix _clustdb


