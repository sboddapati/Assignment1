import psutil
import time
import signal
import sys

def signal_handler(sig, frame):
    print('Exiting health monitor...')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    return psutil.virtual_memory().percent

def get_disk_usage():
    return psutil.disk_usage('/').percent

def check_cpu_threshold(cpu_usage, threshold=85):
        if cpu_usage > threshold:
            print("Alert! CPU usage is above the threshold " + str(threshold) + "%")
            print("Current CPU usage is: " + str(cpu_usage) + "%")
        return False   
def get_network_usage():
    net_info = psutil.net_io_counters()
    return net_info.bytes_sent, net_info.bytes_recv

def monitor_health(interval=5):
    while True:
        cpu_usage = get_cpu_usage()
        memory_usage = get_memory_usage()
        disk_usage = get_disk_usage()
        sent, received = get_network_usage()
        
        
        try:
            cpu_usage = get_cpu_usage()
            memory_usage = get_memory_usage()
            disk_usage = get_disk_usage()
            sent, received = get_network_usage()
        except Exception as e:
            print(f"An error occurred: {e}")
            continue
        
        
        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory_usage}%")
        print(f"Disk Usage: {disk_usage}%")
        print(f"Network Usage: Sent = {sent}, Received = {received}")
        print("-" * 40)
        check_cpu_threshold(cpu_usage)
        
        time.sleep(interval)