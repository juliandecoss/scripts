from datetime import datetime, date

def get_duration_commit(created_time:str, merged_time:str):
    created_time = created_time.split(".")[0]
    merged_time = merged_time.split(".")[0]
    created_time= datetime.strptime(created_time, '%Y-%m-%dT%H:%M:%S')
    merged_time= datetime.strptime(merged_time, '%Y-%m-%dT%H:%M:%S')
    return str(merged_time - created_time)
diff = get_duration_commit('2023-01-26T20:36:22.496Z','2023-01-26T20:46:14.607Z')
breakpoint()
print(diff.min)
print(type(diff))
print(dir(diff))