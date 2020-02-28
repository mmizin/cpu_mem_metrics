import sys
from pprint import pprint
import psutil

if len(sys.argv) == 2 and sys.argv[1] == "cpu" or sys.argv[1] == "mem":
    if sys.argv[1] == "cpu":
        print("CPU metrics")
        pprint(dict(psutil.cpu_times_percent(interval=1, percpu=False)._asdict()))
    elif sys.argv[1] == "mem":
        print("RAM metrics")
        pprint(dict(psutil.virtual_memory()._asdict()))
else:
    print("Enter please what metric do you want to see 'cpu' or 'mem'")
