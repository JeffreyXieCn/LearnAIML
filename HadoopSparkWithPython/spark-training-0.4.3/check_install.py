#!/usr/bin/env python

import sys

if sys.version_info < (3,6):
    print('Python >= 3.6 is required')
    sys.exit(1)

with open('requirements.txt', 'r') as f:
    packages = f.readlines()

for p in packages:
    p = p.strip()
    try:
        __import__(p)
    except:
        print('package ', p,'is missing')
        sys.exit(1)

print('All good!')