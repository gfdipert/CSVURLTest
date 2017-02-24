import csv
import sys
import requests
 
FILE = "Insert file path here"
 
with open(FILE, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        for col in row:
            if col.startswith('http'):
                try:
                    r = requests.get(col)
                    status = r.status_code
                    if status == 200:
                        pass
                    else:
                        print "{0} FAILED WITH STATUS CODE {1}".format(col, status)
                except:
                    print "{0} FAILED because the domain name isn't valid"