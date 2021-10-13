import requests as rq

import sys

subdom_list = open("subdomain.txt").read()
subdoms = subdom_list.splitlines()

for sub in subdoms:
    sub_domains = f"http://{sub}.{sys.argv[1]}"

    try:

        rq.get(sub_domains)
    except rq.ConnectionError:

        pass

    else:
        print("Valid domain:", sub_domains)