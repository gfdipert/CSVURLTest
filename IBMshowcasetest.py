import csv
import sys
import requests
 
FILE='/Users/gwendipert/Repos/IBM/IBMAssets_Systems.csv'
 
with open(FILE, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        for col in row:
            if col.startswith('http'):
                try:
                    r = requests.get(col)
                    status = r.status_code
                    if status == 200:
                        print "{0} was successful".format(col)
                        """
                        if "IBM Showcase" in r.text:
                            if "id=idSVNavLang" in r.text:
                                print "Old plugin was found on {0}!\n".format(col)
                            else:
                                print "Correct plugin was found on {0}\n".format(col)
                        else:
                            print "No plugin was found on {0}!\n".format(col)
                        """
                    else:
                        print "{0} FAILED WITH STATUS CODE {1}".format(col, status)
                except:
                    print "{0} FAILED because the domain name isn't valid"