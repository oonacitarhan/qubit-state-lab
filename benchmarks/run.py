import sys,time,statistics,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from qstate.features import *
durations=[]
for _ in range(5):
    start=time.perf_counter()
    execute(8,[{'gate':'h','target':q} for q in range(8)])
    durations.append(time.perf_counter()-start)
print(json.dumps({'workload':"execute(8,[{'gate':'h','target':q} for q in range(8)])",'repetitions':len(durations),'median_seconds':statistics.median(durations),'min_seconds':min(durations)}))
