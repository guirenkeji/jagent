#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
logging.basicConfig(level=logging.DEBUG)
def disk_stat():  

    st = os.statvfs("/")
    logging.info(st)
    free = (st.f_bavail * st.f_frsize)
    total = (st.f_blocks * st.f_frsize)
    used = (st.f_blocks - st.f_bfree) * st.f_frsize

    try:
        free_percent = round((float(free) / total) * 100, 1)
    except ZeroDivisionError:
        free_percent = None

    return {
        'total': total,
        'used': used,
        'free': free,
        'free_percent': free_percent,
    }

if __name__ == '__main__':
    # for test & demo purpose.
    print disk_stat()
