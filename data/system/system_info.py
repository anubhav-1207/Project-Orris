import platform
import psutil

def osinfo():
    system = platform.system()
    release = platform.release()
    version = platform.version()
    architecture = platform.architecture()[0]

    print(f"Operating System  : {system}")
    print(f"Release           : {release}")
    print(f"Version           : {version}")
    print(f"Architecture      : {architecture}")
    
def cpuinfo():
    cpuname = platform.processor()
    cpucore = psutil.cpu_count(logical=False)
    cputhread = psutil.cpu_count(logical=True)
    cpufreq = psutil.cpu_freq()
    usage = psutil.cpu_percent()
    
    print(f"""
    Processor: {cpuname}
    Cores: {cpucore}
    Threads: {cputhread}
    Clock Speed: {cpufreq}
    Usage: {usage}
    """)

def raminfo():
    mem = psutil.virtual_memory()
    total = mem.total/(1024**3)
    used = mem.used/(1024**3)
    avail = mem.available/(1024**3)
   

    print(f"""
    RAM Size: {total}
    RAM Used: {used}
    RAM Available: {avail}
    
    
    """)