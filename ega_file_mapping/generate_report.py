#!/usr/bin/python

import json
# import requests
import logging
import sys
import fileinput

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
logging.StreamHandler(sys.stderr)


def main(argv):
    egaf_file_path = argv[0]
    egad_mapping_path = argv[1]
    epirr_path = argv[2]

    #Load EGAF metadata JSON
    #Load CSV

    with open(egaf_file_path, 'r') as f_egaf:
        egaf_json = json.loads(f_egaf.read())

    with open(egad_mapping_path, 'r') as f_egad:
        egad_json = json.loads(f_egad.read())

    with open(epirr_path, 'r') as f_epirr:
        epirr_json = json.loads(f_epirr.read())


    total_bytes = 0
    file_count = 0
    for egaf in egaf_json:
        total_bytes += egaf_json[egaf]['fileSize']
        file_count += 1

    print('Total size: ', total_bytes)
    print('Files: ', file_count)


    # consortium = {}
    # for epirr in epirr_json:
    #     logging.info('Processing record %s' % epirr)
    #     record = epirr_json[epirr]
    #     for experiment in record['experiment_list']:
    #         egad = experiment['secondary_id']
    #         egax = experiment['primary_id']

        # struct = consortium.setdefault(record['project'], {'file_count': 0, 'size_count': 0})
        # struct['file_count'] = egad_json[]



if __name__ == "__main__":
    main(sys.argv[1:])
