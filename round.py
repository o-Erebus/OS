import matplotlib.pyplot as plt

processes = [
    [1, 0, 3],  # Process ID, Arrival Time, Burst Time
    [2, 1, 3],
    [3, 2, 3],
    [4, 3, 3],
    [5, 4, 3]
]

# Sort processes by arrival time
processes.sort(key=lambda x: x[1])

quantum = 1
time = 0  # Current time in the simulation
completed = 0  # Count of completed processes
queue = []  # Queue of processes that are ready to execute
waiting_time = {p[0]: 0 for p in processes}  # Track waiting times
turnaround_time = {p[0]: 0 for p in processes}  # Track turnaround times
remaining_time = {p[0]: p[2] for p in processes}  # Track remaining burst time
start_time = {}  # Store start time for each process
gantt_chart = []  # List to store Gantt chart

# To track completion time
arrival_time = {p[0]: p[1] for p in processes}

while completed < len(processes):
    # Add processes to queue that have arrived by the current time
    for i in range(len(processes)):
        if processes[i][1] <= time and processes[i][0] not in [p[0] for p in queue] and remaining_time[processes[i][0]] > 0:
            queue.append(processes[i])

    if queue:
        queue.sort(key=lambda x: x[1])
        # Process execution: Round Robin means processing the first in the queue
        current_process = queue.pop(0)
        pid, arrival_time1, burst_time = current_process

        if pid not in start_time:  # Set start time for the process
            start_time[pid] = time

        if remaining_time[pid] <= quantum:
            gantt_chart.append((pid, time, remaining_time[pid]))  # Record execution
            time += remaining_time[pid]
            remaining_time[pid] = 0  # Process is completed
        else:
            remaining_time[pid] -= quantum
            gantt_chart.append((pid, time, quantum))  # Record execution
            time += quantum
            queue.append([pid, time, remaining_time[pid]])  # Re-add to the queue

        # When the process is completed, calculate waiting and turnaround times
        if remaining_time[pid] == 0:
            completed += 1
            # Calculate waiting time and turnaround time
            turnaround_time[pid] = time - arrival_time[pid]
            waiting_time[pid] = turnaround_time[pid] - burst_time
    else:
        time += 1  # Increment time if no processes are ready to execute

# Display results
print("Process | Arrival Time | Burst Time | Waiting Time | Turnaround Time")
for p in processes:
    pid = p[0]
    print(f"P{pid: <7} | {p[1]: <12} | {p[2]: <10} | {waiting_time[pid]: <12} | {turnaround_time[pid]: <15}")

# Gantt chart plotting
plt.figure(figsize=(10, 6))
for entry in gantt_chart:
    pid, start_time, burst_time = entry
    plt.barh(y=f"P{pid}", width=burst_time, left=start_time,align='center')

plt.show()
