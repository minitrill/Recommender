# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import random

VIDEONUM = 1000000



def LoadUserAgents(uafile):
    uas = []
    with open(uafile, 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[1:-1 - 1])
    random.shuffle(uas)
    return uas