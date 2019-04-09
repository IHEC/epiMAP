#!/usr/bin/python

import json
import requests
import logging
import sys

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
logging.StreamHandler(sys.stderr)

epirr_api_url_base = 'https://www.ebi.ac.uk/vg/epirr/view/'
epirr_api_url_suffix = '?format=json'
headers = {'Content-Type': 'application/json'}


def main(argv):
    epirr_full_list = get_full_epirr_list()
    epirr_records = get_epirr_records(epirr_full_list)
    print(json.dumps(epirr_records, indent=2))


# Fetches all the JSON records for provided list
def get_epirr_records(epirr_list_json):
    accum_epirr = {}

    for epirr in epirr_list_json:
        logging.info('Fetching %s' % epirr['full_accession'])

        record = get_epirr_record(epirr['_links']['self'])

        accum_epirr[epirr['full_accession']] = {
            'experiment_list' : [{'experiment_type' : exp['experiment_type'],
                                  'primary_id': exp['primary_id'],
                                  'secondary_id': exp['secondary_id'],} for exp in record['raw_data']],
            'project': epirr['project'],
            'full_epirr_record': record
        }

    return accum_epirr


# Returns one EpiRR record for a given link
def get_epirr_record(link):
    response = requests.get(link, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        raise Exception('Encountered issue.')


# Returns the full list of EpiRR accessions
def get_full_epirr_list():
    response = requests.get(epirr_api_url_base + 'all' + epirr_api_url_suffix, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        raise Exception('Encountered issue.')


if __name__ == "__main__":
    main(sys.argv[1:])
