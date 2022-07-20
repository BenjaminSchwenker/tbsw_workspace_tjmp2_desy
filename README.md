# tbsw_workspace_tjmp2_desy
Workspace for analyzing TJMP2 testbeam at Desy with tbsw


Need to copy the `init_tbsw.sh` from your local tbsw installation into this folder. Do no forget to executer this bash 
script each time before you use this workspace. 

The main script that executed alignment and data reconstruction up to analysis TTrees is `tj2-reco.py`. The basic usage is

```
python3 tj2-reco.py   --runno $run  --gearfile $gearfile 
```

Some default plotting is defined in the script `histo-plotter-tj2.py`. It runs on .root files and the basic usage is: 
 
```
python3 histo-plotter-tj2.py --ifile=root-files/Histos-<something>.root
```

In case of questions, please contact benjamin.schwenker@phys.uni-goettingen.de
