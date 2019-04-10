Collection of scripts to get metadata on datasets located at EGA, such as the EGAD -> EGAX -> EGAR -> EGAF relationship.

Requires Python 3.

## Step 0: Initial setup
```
python -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
```

## Step 1: Get list of reference epigenomes from EpiRR
``````
python ./get_epirr_records.py.py > ./epirr_dump.json
``````
## Step 2: Request report from EGA

Get list of all IHEC EGAD to get a report. Request from EGA support the same query that was ran for case #330366.

To get the list of EGAD:
```
grep 'EGAD[0-9]\+' epirr_dump.json -o | sort | uniq > EGAD_list.txt
```

## Step 3: Use EGA webAPI to extract files information
```
python get_files_metadata.py EGAD_list.txt > file_metadata.json
```

## Step 4: Build a map of EGAD->EGAX->EGAR->EGAF

This script take as input a report requested to the EGA support (ref. case #330366), and formatted like this:
```
"DATASET_ACCESSION","EXPERIMENT_ACCESSION","RUN_OR_ANALYSIS_ACCESSION","FILE_ACCESSION","UNENCRYPTED_MD5","MD5"
"EGAD00001001276","EGAX00001273375","EGAR00001301113","EGAF00000773228","15037ce66df757e9dd0157b5c6b13a60",
"EGAD00001001276","EGAX00001273375","EGAR00001301113","EGAF00000773229","65cd855261498d89597352e6deccfa35",
"EGAD00001001276","EGAX00001273376","EGAR00001301114","EGAF00000773230","3b2e4b98f6b9cb0dc79eace99943f35c",
[...]
```

```
python generate_ega_file_mapping.py ./input/results.csv > egad_file_mapping.json
```

## Step 5: Generate report

Compute basic stats on IHEC datasets 
```
python generate_report.py file_metadata.json egad_file_mapping.json epirr_dump.json
```



