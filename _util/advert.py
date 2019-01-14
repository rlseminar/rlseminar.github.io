#!/usr/bin/env python

import os
import sys
import yaml
from datetime import datetime, timedelta
import glob

email = """
To: scan-seminar-l@cornell.edu
Subject: SCAN seminar: {name}, 1:25 pm, {date:%x}

Title: {title}
Speaker: {name}
Time: {date:%x}, 1:25-2:15
Location: 406 Gates

Abstract:
{abstract}
"""

if len(sys.argv) > 1:
    fnames = sys.argv[1:]
else:
    today = datetime.today()
    next_mon = today + timedelta(7-today.weekday())
    fnames = glob.glob("_posts/{0:%Y}-{0:%m}-{0:%d}-*.md".format(next_mon))

for fname in fnames:
    # Slurp up the post file
    with open(fname, 'r') as f:
        lines = f.readlines()

    # Extract date
    date = yaml.load(os.path.basename(fname)[0:10])

    # Split out header block and body text
    header = ""
    body = ""
    in_header = True
    for l in lines[1:]:
        if in_header:
            if l == "---\n":
                in_header = False
            else:
                header += l
        else:
            body += l

    # Parse header block and plug in date
    hdata = yaml.load(header)
    hdata['name'] = "{name} ({affil})".format(**hdata['speaker'])
    hdata['date'] = date
    hdata['abstract'] = body

    # Format the email
    print(email.format(**hdata))
