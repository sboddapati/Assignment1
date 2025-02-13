import psutil
import time

def monitor_cpu_usage(threshold=80):
    #Start monitoring CPU usage continuously.
    print("Monitoring CPU usage... Press Ctrl+C to stop.")
    
    
       try:
        while True:
            # Current CPU usage percentage
            cpu_usage = psutil.cpu_percent(interval=1)
            print(f"Current CPU Usage: {cpu_usage}%")
            
            # Check if CPU usage exceeds the threshold
            if cpu_usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}% ")
            
            # Wait for 1 second before checking again
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
        
        
    except Exception as e:
        print(f" Error occurred: {e}")
