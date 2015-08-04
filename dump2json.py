# -*- coding: utf-8 -*-

import json
import time
from xapian_weibo.xapian_backend import XapianSearch

XAPIAN_USER_DATA_PATH = '/home/xapian/xapian_user/'
xs = XapianSearch(path=XAPIAN_USER_DATA_PATH, name='master_timeline_user', schema_version=1)
with open('total_users.json', 'w') as f:
    record = 1
    ts = time.time()
    tm = ts
    for count, item in enumerate(xs.iter_all_docs()):#遍历数组的索引值和元素
        f.write(json.dumps(item) + '\n')
        if (count + 1) % 100000 == 0:
            te = time.time()
            span = round(te - tm)
            print '%s chunk spend: %s' % (record, span)
            record += 1
            tm = time.time()
    print 'total docs count: ', (count+1)
    te = time.time()
    total_span = round(te - ts)
    print 'total spend: %s' % total_span
