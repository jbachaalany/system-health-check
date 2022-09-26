import psutil

# set system thresholds
max_cpu_usage_percent = 80
max_disk_usage_percent = 80
max_memory_available_mb = 500

def checkCPU():
    """check if CPU usage % exceeds max threshold"""
    cpu_usage_percent = psutil.cpu_percent(interval=3)
    print(cpu_usage_percent)
    return cpu_usage_percent > max_cpu_usage_percent

def checkDisk():
    """check if Disk usage exceeds max threshold"""
    disk_usage_percent = psutil.disk_usage("/").percent
    print(disk_usage_percent)
    return disk_usage_percent > max_disk_usage_percent

def checkMemory():
    """check if Memory usage % exceeds max threshold"""
    one_mb = 2 ** 20
    max_memory_available = one_mb * max_memory_available_mb
    memory_available = psutil.virtual_memory().available
    print(memory_available)
    return memory_available < max_memory_available

if __name__ == "__main__":
    # check system resources:
    print("checking system resources")
    if checkCPU():
        print(f"Error - CPU usage is over {max_cpu_usage_percent}%")
    elif checkDisk():
        print(f"Error - Available disk space is over {max_disk_usage_percent}%")
    elif checkMemory():
        alert = f"Error - Available memory is less than {max_memory_available_mb}MB"
    else:
        print("System OK")