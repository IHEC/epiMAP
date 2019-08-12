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



    report = {}

    egax_stack = {}
    egaf_stack = {}

    for epirr in epirr_json:
        logging.info('Processing record %s' % epirr)
        record = epirr_json[epirr]

        for experiment in record['experiment_list']:
            egax = experiment['primary_id']
            egad = experiment['secondary_id']

            experiment['file_list'] = {}
            if egax.startswith('EGAX'):
                egax_stack[egax] = 1


                #Fetch all EGAF
                for egar in egad_json[egad][egax]:
                    file_list = egad_json[egad][egax][egar]
                    for file in file_list:
                        if file in egaf_json:
                            experiment['file_list'][file] = egaf_json[file]
                        else:
                            experiment['file_list'][file] = {}

                        egaf_stack[file] = 1


        report[epirr] = {
            'consortium' : epirr_json[epirr]['project'],
            'experiments' : record['experiment_list']
        }


    # print('-------------')
    # difflist = list(set(egaf_json.keys()) - set(egaf_stack.keys()))
    # print(difflist)

    print(json.dumps(report, indent=2))

    # print('Total size: ', total_bytes)
    # print('Files: ', file_count)
    # print('Experiments: ', len(egax_stack))
    # print('Files 2: ', len(egaf_stack))



if __name__ == "__main__":
    main(sys.argv[1:])
