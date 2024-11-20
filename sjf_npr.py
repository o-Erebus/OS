import matplotlib.pyplot as plt
from matplotlib import cm

processes = [
    [1, 0, 10],  # Process ID, Arrival Time, Burst Time
    [2, 1, 8],
    [3, 2, 6],
    [4, 3, 4],
    [5, 4, 2]
]

# Sort processes by arrival time to handle processes as they arrive
processes.sort(key=lambda x: x[1])

n = len(processes)
completed = 0
time = 0
waiting_time = {p[0]: 0 for p in processes}
turnaround_time = {p[0]: 0 for p in processes}
remaining_burst = {p[0]: p[2] for p in processes}  # Remaining burst time for each process
start_time = {}
# Define a list of distinct colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',  # First 5 colors
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']  # More if needed
# List of processes ready to execute
queue = []
gantt_chart = []  # To store the Gantt chart as tuples (process_id, start_time, duration)

while completed < n:
    # Add processes that have arrived by the current time to the queue
    for i in range(n):
        if processes[i][1] <= time and processes[i] not in queue and remaining_burst[processes[i][0]] > 0:
            queue.append(processes[i])

    # If there are processes in the queue, execute the process with the shortest remaining burst time
    if queue:
        queue.sort(key=lambda x: remaining_burst[x[0]])  # Sort by remaining burst time (Shortest first)

        current_process = queue.pop(0)  # Get the process with the shortest remaining burst time
        pid, arrival_time, burst_time = current_process

        # Record start time if the process is starting
        if pid not in start_time:
            start_time[pid] = time

        # Execute the process for 1 unit of time
        remaining_burst[pid] =0
        gantt_chart.append((pid, time, burst_time))  # Record process execution in Gantt chart
        time += burst_time

        # If the process is completed, calculate waiting time and turnaround time
        if remaining_burst[pid] == 0:
            completed += 1
            # Calculate waiting and turnaround time
            waiting_time[pid] = time - arrival_time - burst_time
            turnaround_time[pid] = time - arrival_time

        # Add back the process to the queue if it still has remaining burst time
        if remaining_burst[pid] > 0:
            queue.append(current_process)

    else:
        time += 1  # Increment time if no processes are ready to execute

# Plot the Gantt chart
plt.figure(figsize=(10, 6))

# Map each process to its assigned color
for entry in gantt_chart:
    pid, start_time, duration = entry
    color = colors[pid-1]  # Get color from the colormap (indexed by process ID)
    plt.barh(y=f"P{pid}", width=duration, left=start_time, edgecolor='black', color=color, align='center')


plt.show()

# Display the results
print("\nProcess | Arrival Time | Burst Time | Waiting Time | Turnaround Time")
for p in processes:
    pid = p[0]
    print(f"P{pid: <7} | {p[1]: <12} | {p[2]: <10} | {waiting_time[pid]: <12} | {turnaround_time[pid]: <15}")
