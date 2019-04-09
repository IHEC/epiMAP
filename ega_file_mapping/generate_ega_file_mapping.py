#!/usr/bin/python

# ./ingest_ega_csv.py ./EGA_files_metadata/ > datasets.json


import json
import logging
import sys
import csv

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
logging.StreamHandler(sys.stderr)

def main(argv):
    path = argv[0]
    datasets = {}

    with open(path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headers = next(csv_reader)

        for row in csv_reader:
            row_dict = {key: value for key, value in zip(headers, row)}
            egad = row_dict['DATASET_ACCESSION']
            egax = row_dict['EXPERIMENT_ACCESSION']
            egar = row_dict['RUN_OR_ANALYSIS_ACCESSION']
            egaf = row_dict['FILE_ACCESSION']

            datasets.setdefault(egad, {}).setdefault(egax, {}).setdefault(egar, []).append(egaf)

    print(json.dumps(datasets, indent=2))


if __name__ == "__main__":
    main(sys.argv[1:])
