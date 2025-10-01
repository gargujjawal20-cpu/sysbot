import psutil

def get_cpu_info():
    return f"CPU usage is at {psutil.cpu_percent()}%"

def get_memory_info():
    mem = psutil.virtual_memory()
    return f"Memory usage: {mem.percent}%"

def get_battery_info():
    batt = psutil.sensors_battery()
    temp = batt[0]
    if batt:
        return f"Battery: {batt[0]}%"
    return "Battery information not available."

def get_network_info():
    net = psutil.net_io_counters()
    return f"Sent: {net.bytes_sent // (1024**2)} MB, Received: {net.bytes_recv // (1024**2)} MB."