# epiMAP
epiMAP data re-processing initiative


## Datasets

Metadata sources are the EpiRR database and a CSV mapping EGAX -> EGAR -> EGAF relationship.


### Step 1: Get list of reference epigenomes from EpiRR
``````
pip install -r requirements.txt
python ./get_epirr_records.py.py > ./epirr_dump.json
``````
### Step 2: Request report from EGA

Get list of all IHEC EGAD to get a report. Request from EGA support the same query that was ran for case #330366.

To get the list of EGAD:
```
grep 'EGAD[0-9]\+' epirr_dump.json -o | sort | uniq > EGAD_list.txt
```

### Step 3: Use EGA webAPI to extract files information
```
python get_files_metadata.py EGAD_list.txt > file_metadata.json
```


### Step 4: Build a map of EGAX->EGAR->EGAF
```

``` 


