from psutil import process_iter

p_list = []
for proc in process_iter():
    proc_info = proc.as_dict(['name', 'cpu_percent'])
    if proc_info['cpu_percent'] > 0:
        p_list.append(proc_info)

sorted(
    p_list,
    key=lambda p: p['cpu_percent'],
    reverse=True
)