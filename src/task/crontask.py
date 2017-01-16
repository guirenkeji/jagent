from apscheduler.schedulers.blocking import BlockingScheduler
import time 
from src.bin import cpu,disk,memory,sysinfo
sched = BlockingScheduler()  
  
def job_function():  
    cpu.cpu(frist_invoke)
    disk.disk_stat()
    memory.monitor(frist_invoke)
    sysinfo.
def job_status():  
    models.gettaskstatus()
 
def run ():
    job1 = sched.add_job(job_function, 'interval', seconds=10)

    job2 = sched.add_job(job_status, 'interval', seconds=30)
    try:
            sched.start() 
    
    except (KeyboardInterrupt, SystemExit):
            sched.shutdown()
            
            
if __name__ == '__main__':
    run()     