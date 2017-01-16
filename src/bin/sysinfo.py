# -*- coding: utf-8 -*-
import os
import psutil
import socket
import logging
logging.basicConfig(level=logging.DEBUG)
#===============================================================================
# 获取系统信息
#===============================================================================
def systemHostInfo():
    hostName = socket.gethostname() 
    hostIp = socket.gethostbyname(hostName) 
    host_info = hostName+':'+hostIp
    logging.info(host_info)
    data = {
        'hostName':hostName,
        'hostIp':hostIp}
    return data
#===============================================================================
# 获取cpu信息
#===============================================================================
def cpuResouse():
    cpu_count = psutil.cpu_count()
    cpu_percent = psutil.cpu_percent()
    system_users = psutil.users()#系统登录用户信息
    data = {
        'cpu_count':cpu_count,
        'cpu_percent':cpu_percent}
    return data
#===============================================================================
# 获取内存信息    
#===============================================================================
def memResouse():
    mem = psutil.virtual_memory() 
    mem_total = float(mem.total)/1024/1024/1024#单位G
    mem_free = float(mem.free)/1024/1024/1024#单位G
    data = {
        'mem_total':mem_total,
        'mem_free':mem_free}
     
    return data
if __name__ == '__main__':
    print cpuResouse()
    print systemHostInfo()
