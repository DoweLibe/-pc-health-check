import psutil
import platform
import subprocess
from datetime import datetime

def get_system_info():
    print("System Information")
    print("------------------")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Machine Name: {platform.node()}")
    print()

def get_uptime():
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    print("System Uptime")
    print("-------------")
    print(f"Last Boot Time: {boot_time}")
    print()

def get_cpu_usage():
    print("CPU Usage")
    print("---------")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    print()

def get_memory_usage():
    memory = psutil.virtual_memory()
    print("Memory Usage")
    print("------------")
    print(f"Total: {memory.total / (1024 ** 3):.2f} GB")
    print(f"Used: {memory.used / (1024 ** 3):.2f} GB")
    print(f"Available: {memory.available / (1024 ** 3):.2f} GB")
    print(f"Percentage Used: {memory.percent}%")
    print()

def get_disk_usage():
    disk = psutil.disk_usage('/')
    print("Disk Usage")
    print("----------")
    print(f"Total: {disk.total / (1024 ** 3):.2f} GB")
    print(f"Used: {disk.used / (1024 ** 3):.2f} GB")
    print(f"Free: {disk.free / (1024 ** 3):.2f} GB")
    print(f"Percentage Used: {disk.percent}%")
    print()

def check_network():
    print("Network Connectivity")
    print("--------------------")
    try:
        result = subprocess.run(
            ["ping", "-n", "1", "8.8.8.8"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode == 0:
            print("Internet Connection: Active")
        else:
            print("Internet Connection: Inactive")
    except Exception as e:
        print(f"Error checking network: {e}")
    print()

def main():
    print("PC Health Check Report")
    print("======================")
    print()

    get_system_info()
    get_uptime()
    get_cpu_usage()
    get_memory_usage()
    get_disk_usage()
    check_network()

if __name__ == "__main__":
    main()
