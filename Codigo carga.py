import requests
import json
import argparse
import os
 
api_key = os.environ['secret']
api_url = 'http://18.218.244.166:8080/api/v2/{method}'

def upload(file_report, type_scan): 
    headers = {
        'Accept': 'application/json',
        'Authorization': api_key,

    }

    report = {
        'file': open(file_report, 'rb'), 
    }

    body = {
        'product_name': 'WebGoat',
        'engagement_name': 'giselle',
        'product_type_name': 'Research and Development', 
        'active': True,
        'verified': True,
        'scan_type': type_scan
    }


    r = requests.post(api_url.format(method = 'import-scan/'), data = body, files = report, headers = headers, verify = False)
 
    if r.status_code == 201: 
        print(json.dumps(r.json(), indent=4)) 
        print('Trivy report uploaded successfully.')

if __name__ == '__main__':

    parse = argparse.ArgumentParser()

    parse.add_argument('--file', '-f', dest='file', help='Nombre del reporte', required=True)
    parse.add_argument('--type-scan', '-t', dest='type_scan', help='Nombre del reporte', required=True)

    args = parse.parse_args()

    upload(args.file, args.type_scan)