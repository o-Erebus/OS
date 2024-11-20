import matplotlib.pyplot as plt

processes = [
    [1, 0, 10],  # Process ID, Arrival Time, Burst Time
    [2, 1, 8],
    [3, 2, 6],
    [4, 3, 4],
    [5, 4, 2]
]

burst = [process[2] for process in processes]

# Sort processes by arrival time (AT) to handle them in FCFS order
processes.sort(key=lambda x: x[1])

current = 0  # Keeps track of the current process index in the queue
time = 0  # Current time in the simulation
completed = 0  # Count of completed processes
queue = []  # Queue of processes that are ready to execute
waiting_time = {p[0]: 0 for p in processes}  # Track waiting times
turnaround_time = {p[0]: 0 for p in processes}  # Track turnaround times
remaining_time = {p[0]: p[2] for p in processes}
start_time = {}  # Store start time for each process
gantt_chart = []
print("Process | Arrival Time | Burst Time | Waiting Time | Turnaround Time")
while completed < len(processes):
    # Add processes to queue that have arrived by the current time
    for i in range(len(processes)):
        if processes[i][1] <= time and processes[i] not in queue and remaining_time[processes[i][0]] > 0:
            queue.append(processes[i])

    if queue:
        # Process execution: FCFS means processing the first in the queue
        current_process = queue[0]
        pid, arrival_time, burst_time = current_process

        if pid not in start_time:  # Set start time for the process
            start_time[pid] = time

        # Execute the process (decrease remaining time)
        remaining_time[pid] -= burst_time
        gantt_chart.append((pid,time,burst_time))
        time += burst_time


        # When burst time reaches 0, process is completed
        if remaining_time[pid] == 0:
            completed += 1
            queue.pop(0)  # Remove the completed process
            # Calculate waiting time and turnaround time
            waiting_time[pid] = start_time[pid] - arrival_time
            turnaround_time[pid] = time - arrival_time
            print(f"P{pid: <7} | {arrival_time: <12} | {burst_time: <10} | {waiting_time[pid]: <12} | {turnaround_time[pid]: <15}")
    else:
        time += 1  # Increment time

plt.figure(figsize=(10,6))
for entry in gantt_chart:
    pid, start_time, burst_time = entry
    plt.barh(y=f"P{pid}",width=burst_time,left=start_time)
plt.show()