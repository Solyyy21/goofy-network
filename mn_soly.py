import random
import matplotlib.pyplot as plt
import tkinter as tk

# list of users with their current status and application usage
users = [
    {'id': 1, 'status': 'online', 'applications': {'Spotify': 5, 'Valorant': 15, 'YouTube': 10}},
    {'id': 2, 'status': 'offline', 'applications': {'Spotify': 2, 'Instagram': 8}},
    {'id': 3, 'status': 'online', 'applications': {'Genshin': 30}},
    {'id': 4, 'status': 'online', 'applications': {'Spotify': 8, 'Instagram': 12}},
    {'id': 5, 'status': 'offline', 'applications': {}},
]

# dictionary to store the total bandwidth assigned to each user
total_bandwidth = {}
weights = {'Spotify': 15, 'Valorant': 30, 'YouTube': 25, 'Whatsapp': 10,'Genshin':50,'Instagram':10}

def calculate_weights():
    for user in users:
        if user['status'] == 'offline':
            total_bandwidth[user['id']] = 0
            continue
        bandwidth = 0
        for app in user['applications']:
            user['applications'][app] = random.randint(1, 20) * 5  # assign 5 times more bandwidth every time code is run
            bandwidth += weights.get(app, 0) * user['applications'][app]
        total_bandwidth[user['id']] = bandwidth

def assign_bandwidth():
    for user in users:
        if user['status'] == 'offline':
            continue
        for app in user['applications']:
            if user['applications'][app] > 0:
                allocated_bandwidth = int((weights.get(app, 0) * user['applications'][app] / total_bandwidth[user['id']]) * 100)
                print(f"User {user['id']} was given {allocated_bandwidth}% ({allocated_bandwidth * total_bandwidth[user['id']] / 100}MB) of bandwidth for {app}")

def display_graphs():
    # plot the graph showing the total bandwidth assigned to each user
    fig, axs = plt.subplots(1, 2, figsize=(10, 4))
    fig.set_facecolor('#696969')

    axs[0].bar(range(len(total_bandwidth)), list(total_bandwidth.values()), align='center',color='#EE3D12')
    axs[0].set_xticks(range(len(total_bandwidth)))
    axs[0].set_xticklabels(list(total_bandwidth.keys()))
    axs[0].set_ylabel('Total Bandwidth (MB)')
    axs[0].set_title('Total Bandwidth Assigned to Each User')

    # plot the graph showing the bandwidth consumed by each application
    bandwidth_by_app = {}
    for user in users:
        for app, usage in user['applications'].items():
            bandwidth_by_app[app] = bandwidth_by_app.get(app, 0) + usage

    axs[1].bar(range(len(bandwidth_by_app)), list(bandwidth_by_app.values()), align='center',color='#27E9E3')
    axs[1].set_xticks(range(len(bandwidth_by_app)))
    axs[1].set_xticklabels(list(bandwidth_by_app.keys()))
    axs[1].set_ylabel('Bandwidth (MB)')
    axs[1].set_title('Bandwidth Consumed by Each Application')

    plt.show()

def run_program():
    calculate_weights()
    assign_bandwidth()
    display_graphs()
window = tk.Tk()
window.title("Bandwidth Allocation")
window.geometry("300x150")
window.configure(bg='#1E96DA')

# add a button to run the program
button = tk.Button(text="Allocate Bandwidth", command=run_program,bg='#1C428D',fg='#EEEB12')
button.pack(pady=20)

window.mainloop()