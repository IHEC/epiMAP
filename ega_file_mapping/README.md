Collection of scripts to get metadata on datasets located at EGA, such as the EGAD -> EGAX -> EGAR -> EGAF relationship.

Requires Python 3.

## Step 0: Initial setup

python -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt

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
```
python generate_ega_file_mapping.py ./input/results.csv > egad_file_mapping.json
```

## Step 5: Generate report

Compute basic stats on IHEC datasets 
```
python generate_report.py file_metadata.json egad_file_mapping.json epirr_dump.json
```



