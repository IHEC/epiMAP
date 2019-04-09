#!/usr/bin/python

import json
import logging
import sys
import requests
import os
import csv
from collections import defaultdict

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
logging.StreamHandler(sys.stderr)

epirr_api_url_base = 'https://ega-archive.org/metadata/v2/files?queryBy=dataset&limit=0&queryId='
headers = {'Content-Type': 'application/json'}

def main(argv):
    path = argv[0]

    # datasets = {}
    egaf_metadata = {}

    with open(path, 'r') as egad_list:
        for egad in egad_list:
            logging.info('Fetching metadata for %s' % egad)

            egad = egad.rstrip()
            if len(egad) == 0:
                continue

            egad_files = get_dataset_files(egad)
            egad_files.pop('header')

            def process_file_metadata(file_metadata):
                egaf = file_metadata['egaStableId']
                file_metadata.pop('locations')
                file_metadata.pop('egaStableId')
                file_metadata.pop('hasReport')
                egaf_metadata[egaf] = file_metadata

            [process_file_metadata(x) for x in egad_files['response']['result']]
            # datasets[egad] = egad_files

    print(json.dumps(egaf_metadata, indent=2))


def get_dataset_files(egad):
    response = requests.get(epirr_api_url_base + egad, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        raise Exception('Encountered issue.')



if __name__ == "__main__":
    main(sys.argv[1:])
