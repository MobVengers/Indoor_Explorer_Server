door_to_loc_distance = 0.5

graph2 = {
    'Seminar_Room_Door': [['L_Seminar_Room', door_to_loc_distance], ['J1', 4], ['E-wis_Lab_Door', 3], ['CIT_Door', 7]],
    'CIT_Door': [['L_CIT', door_to_loc_distance], ['Studio_Door', 10]]
}

def heuristic(node, goal):
    return 0

def a_star(graph, start, goal):
    closed_set = set()
    open_set = set([start])
    came_from = {}
    g_score = {}
    f_score = {}

    for node in graph:
        g_score[node] = float('inf')
        f_score[node] = float('inf')

    g_score[start] = 0
    f_score[start] = heuristic(start, goal)

    while open_set:
        current = None
        min_f_score = float('inf')

        # Find the node in open_set with the lowest f_score
        for node in open_set:
            if f_score[node] < min_f_score:
                min_f_score = f_score[node]
                current = node

        if current == goal:
            # Reconstruct path and return
            path = [current]
            while current != start:
                current = came_from[current]
                path.insert(0, current)
            return path

        open_set.remove(current)
        closed_set.add(current)

        for neighbor, weight in graph[current]:
            if neighbor in closed_set:
                continue

            tentative_g_score = g_score[current] + weight

            if neighbor not in open_set:
                open_set.add(neighbor)
            elif tentative_g_score >= g_score[neighbor]:
                continue  # This is not a better path

            # This path is the best until now, record it!
            came_from[neighbor] = current
            g_score[neighbor] = tentative_g_score
            f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)

    return None  # If there is no path

graph = {
    'A': [['Final_Year_Lab', 1], ['B', 30], ['U', 46]],
    'B': [['SE', 1], ['Fabric_Lab', 1], ['C', 74], ['A', 30]],
    'C': [['Washroom', 1], ['Embedded_Enginnering_Lab', 1], ['D', 44], ['B', 74]],
    'D': [['Research_lab', 1], ['E', 80], ['C', 44]],
    'E': [['Old_Advanced_Lab', 1], ['F', 38], ['D', 80]],
    'F': [['RA_Lab', 1], ['G', 78], ['E', 38]],
    'G': [['A1', 1], ['F', 78], ['H', 44]],
    'H': [['G', 44], ['I', 78], ['W', 36]],
    'I': [['A2', 1], ['H', 78], ['J', 50]],
    'J': [['Systems_Lab', 1], ['ICE_Room', 1], ['I', 50], ['K', 28]],
    'K': [['J', 28], ['L', 36], ['Staff_Washroom', 1]],
    'L': [['K', 36], ['M', 52], ['Old_Codegen_Lab', 1]],
    'M': [['L', 52], ['N', 36], ['A3', 1], ['Seminar_Room', 1], ['E_Wis_Lab', 1]],
    'N': [['M', 36], ['O', 72], ['Codegen_Lab', 1]],
    'O': [['N', 72], ['P', 18], ['Sysco_Lounge', 1]],
    'P': [['O', 18], ['Q', 34], ['V', 42], ['Insight_Hub', 30]],
    'Q': [['P', 34], ['R', 62], ['Insight_Hub', 30]],
    'R': [['Q', 62], ['S', 36], ['A4', 1]],
    'S': [['R', 36], ['T', 36], ['HPC_Lab', 1]],
    'T': [['S', 36], ['U', 70], ['IntelliSense_Lab', 1]],
    'U': [['T', 70], ['A', 46], ['L1_Lab', 1]],
    'V': [['P', 42], ['W', 28], ['CSE_Office', 1]],
    'W': [['V', 28], ['H', 36], ['HoD_Office', 1]],
    'A1': [['G', 1], ['Staff_Rooms', 44]],
    'A2': [['I', 1], ['Staff_Rooms', 78], ['Conference_Room', 1], ['Lunch_Room', 1]],
    'A3': [['M', 1], ['Studio', 1]],
    'A4': [['R', 1], ['Embedded_Lab', 1], ['Network_Lab', 1]],
    'Final_Year_Lab': [['A', 1]],
    'SE': [['B', 1]],
    'Fabric_Lab': [['B', 1]],
    'Washroom': [['C', 1]],
    'Embedded_Enginnering_Lab': [['C', 1]],
    'Research_lab': [['D', 1]],
    'Old_Advanced_Lab': [['E', 1]],
    'RA_Lab': [['F', 1]],
    'Staff_Rooms': [['A1', 44], ['A2', 78]],
    'Conference_Room': [['A2', 1]],
    'Lunch_Room': [['A2', 1]],
    'Systems_Lab': [['J', 1]],
    'ICE_Room': [['J', 1], ['Server_Room', 1]],
    'Server_Room': [['ICE_Room', 1]],
    'Staff_Washroom': [['K', 1]],
    'Old_Codegen_Lab': [['L', 1]],
    'Studio': [['A3', 1]],
    'Embedded_Lab': [['A4', 1]],
    'Network_Lab': [['A4', 1]],
    'Seminar_Room': [['M', 1]],
    'E_Wis_Lab': [['M', 1]],
    'Codegen_Lab': [['N', 1]],
    'Sysco_Lounge': [['O', 1]],
    'Insight_Hub': [['P', 30], ['Q', 30]],
    'HPC_Lab': [['S', 1]],
    'IntelliSense_Lab': [['T', 1]],
    'L1_Lab': [['U', 1]],
    'CSE_Office': [['V', 1]],
    'HoD_Office': [['W', 1]]
}

# Example usage:
start_node = 'Final_Year_Lab'
goal_node = 'Server_Room'
shortest_path = a_star(graph, start_node, goal_node)
print("Shortest Path:", shortest_path)