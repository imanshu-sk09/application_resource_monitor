import psutil
import time

def monitor_resource_usage(application_name):
    try:
        # Find the process by its name
        app_process = None
        for proc in psutil.process_iter(['pid', 'name']):
            if application_name in proc.info['name']:
                app_process = psutil.Process(proc.info['pid'])
                break

        if app_process:
            print(f"Monitoring resource usage of {application_name}...")

            while app_process.is_running():
                cpu_percent = app_process.cpu_percent()
                gpu_percent = 0  # This value depends on the library you use to monitor GPU

                print(f"CPU Usage: {cpu_percent}%  |  GPU Usage: {gpu_percent}%")
                time.sleep(1)
        else:
            print(f"No process found for {application_name}")

    except psutil.NoSuchProcess:
        print(f"Process {application_name} not found")

if __name__ == "__main__":
    application_name = input("Enter the application name: ")
    monitor_resource_usage(application_name)
