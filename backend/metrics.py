## this will be for gathering my metrics
## backend/metrics.py
## please see requirements.txt to see what should be in there

##      IMPORTS     ##

import psutil ## this library allows us to monitor our system
import time
import os 
from datetime import datetime , timezone 

##      VARIABLES       ##

START_TIME = time.time() ## record start time of this script

##      FUNCTIONS   ##

    ## get cpu temp

def get_temperature_c():
    ## Reads CPU temp on raspberry pi
    ## Returns none if not available

    thermal_path = "/sys/class/thermal/thermal_zone0/temp"
    try:
        with open(thermal_path , "r" ) as f:
            ## often times the temperature is read as something like 5300
            ## we want it to just say 53 degrees celsius
            temp_milideg = int(f.read().strip())
        return temp_milideg / 1000.0
    except( FileNotFoundError , ValueError ):
        return None

    ## get up time for future use

def get_uptime_seconds():
    return int(time.time() - START_TIME )

def get_system_metrics():
    ## Collect current system metrics and return as a dict
    cpu_percent = psutil.cpu_percent(interval=0.5)
    virtual_mem = psutil.virtual_memory()
    disk_usage = psutil.disk_usage("/")
    net_io = psutil.net_io_counters()

    metrics = {
        "timestamp" : datetime.now(timezone.utc).isoformat(),
        "cpu_percent": cpu_percent,
        "ram_percent": virtual_mem.percent,
        "ram_used_mb": round(virtual_mem.used / (1024 ** 2), 2),
        "ram_total_mb": round(virtual_mem.total / (1024 ** 2), 2),
        "disk_percent": disk_usage.percent,
        "disk_used_gb": round(disk_usage.used / (1024 ** 3), 2),
        "disk_total_gb": round(disk_usage.total / (1024 ** 3), 2),
        "net_bytes_sent_mb": round(net_io.bytes_sent / (1024 ** 2), 2),
        "net_bytes_recv_mb": round(net_io.bytes_recv / (1024 ** 2), 2),
        "temperature_c": get_temperature_c(),
        "uptime_seconds": get_uptime_seconds(),
    }
    return metrics