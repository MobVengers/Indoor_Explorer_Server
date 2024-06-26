from fastapi.responses import JSONResponse


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
            return path, f_score[goal]

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

mapping = {
    "Final_Year_Lab": ['K'],
    "L1_Lab": ['K', 'L'],
    "IntelliSense_Lab": ['M'],
    "HPC_Lab": ['N'],
    "Embedded_Lab": ['O'],
    "Network_Lab": ['O'],
    "Insight_Hub": ['P'],
    "Sysco_Lounge": ['Q'],
    "Codegen_Lab": ['R'],
    "E_Wis_Lab": ['S'],
    "Seminar_Room": ['S'],
    "CIT_Studio": ['e'],
    "Studio": ['d'],
    "Old_Codegen_Lab": ['A'],
    "Server_Room": ['c', 'b'],
    "ICE_Room": ['b', 'B'],
    "Systems_Lab": ['a'],
    "Lunch_Room": ['Z'],
    "Conference_Room": ['B', 'Y'],
    "Staff_Room_1": ['X', 'D', 'W'],
    "Staff_Room_2": ['C', 'X', 'Y'],
    "Old_Advanced_Lab": ['F'],
    "FYP_Lab": ['G', 'f'],
    "LSF_Lab": ['f'],
    "Washroom": ['H'],
    "Stairs": ['I'],
    "Fabric_Lab": ['J'],
    "Instructor_Room": ['J'],
    "CSE_Office": ['U'],
    "HoD_Office": ['V'],
}

graph = {
    'K': [['J', 5], ['L', 7]],
    'L': [['K', 7], ['M', 11]],
    'M': [['L', 11], ['N', 6]],
    'N': [['M', 6], ['O', 5]],
    'O': [['N', 5], ['P', 7]],
    'P': [['O', 7], ['upq', 8]],
    'Q': [['R', 10], ['upq', 3]],
    'U': [['upq', 7], ['V', 8]],
    'upq': [['U', 7], ['P', 8], ['Q', 3]],
    'R': [['Q', 10], ['S', 6]],
    'S': [['R', 6], ['T', 3]],
    'T': [['S', 3], ['A', 7], ['d',4]],
    'd': [['T', 4], ['e', 3]],
    'e': [['d', 3]],
    'A': [['T', 7], ['ab', 10]],
    'ab': [['A', 10], ['B', 2]],
    'B': [['ab', 2], ['a', 5], ['b', 13], ['C', 15]],
    'a': [['B', 5], ['b', 5]],
    'b': [['a', 5], ['B', 13], ['c', 7]],
    'c': [['b', 7]],
    'C': [['B', 15], ['X', 8], ['Y', 10], ['vcd', 6]],
    'Y': [['C', 10], ['X', 15], ['Z', 1]],
    'Z': [['Y', 1]],
    'X': [['Y', 15], ['C', 8], ['D', 9], ['W', 14]],
    'D': [['X', 9], ['W', 11], ['E', 13], ['vcd', 7]],
    'W': [['X', 14], ['D', 11], ['E', 9]],
    'E': [['W', 9], ['F', 7], ['D', 13]],
    'F': [['E', 7], ['G', 13]],
    'G': [['F', 13], ['f', 15], ['hg', 7]],
    'f': [['G', 15]],
    'hg': [['G', 7], ['H', 3]],
    'H': [['hg', 3], ['I', 3]],
    'I': [['H', 3], ['J', 7]],
    'J': [['I', 7], ['K', 5]],
    'V': [['U', 8], ['vcd', 6]],
    'vcd': [['V', 6], ['D', 7], ['C', 6]],
}

mapped_coordinates = {
    'A': (107, 566),
    'B': (180, 558),
    'C': (180, 442),
    'D': (180, 348),
    'E': (180, 256),
    'F': (180, 207),
    'G': (180, 109),
    'H': (164, 64),
    'I': (146, 64),
    'J': (90, 64),
    'K': (59, 64),
    'L': (59, 109),
    'M': (59, 192),
    'N': (59, 242),
    'O': (59, 285),
    'P': (59, 338),
    'Q': (59, 427),
    'R': (59, 508),
    'S': (59, 548),
    'T': (59, 566),
    'U': (102, 395),
    'V': (140, 395),
    'W': (223, 292),
    'X': (223, 397),
    'Y': (211, 500),
    'Z': (226, 512),
    'a': (230, 574),
    'b': (234, 617),
    'c': (192, 637),
    'd': (59, 601),
    'e': (59, 623),
    'f': (192, 27),
    'ab': (180, 566),
    'upq': (59, 395),
    'hg': (180, 64),
    'vcd': (180, 395)
}


def get_mapped_node(node):
    for key, values in mapping.items():
        if key == node:
            return values

def find_path(start_node, goal_node):
    mapped_start_nodes = get_mapped_node(start_node)
    mapped_goal_nodes = get_mapped_node(goal_node)

    print("Mapped Start Nodes:", mapped_start_nodes, "Mapped Goal Nodes:", mapped_goal_nodes)

    shortest_path = None
    shortest_distance= float('inf')
    for node in mapped_start_nodes:
        for goal in mapped_goal_nodes:
            print("Node:", node, "Goal:", goal)
            path, current_distance = a_star(graph, node, goal)
            print("Distance from", node, "to", mapped_goal_nodes, ":", path)
            if current_distance < shortest_distance:
                shortest_path = path
                shortest_distance = current_distance

    print("Shortest Path:", shortest_path)
    # get the coordinates of the nodes
    coordinates = []
    for node in shortest_path:
        coordinates.append(mapped_coordinates[node])

    print("Coordinates:", coordinates)
    return coordinates

async def get_path(req):
    try:
        start_node = req.start
        goal_node = req.goal
        path = find_path(start_node, goal_node)
        return JSONResponse(content={"path": path})
    except Exception as err:
        return JSONResponse(content={"message": str(err)}, status_code=500)
    
# for local testing

# # Example usage:
# start_node = 'Conference_Room'
# goal_node = 'Sysco_Lounge'
# mapped_start_nodes = get_mapped_node(start_node)
# mapped_goal_nodes = get_mapped_node(goal_node)
# print("Mapped Start Nodes:", mapped_start_nodes, "Mapped Goal Nodes:", mapped_goal_nodes)


# shortest_path = None
# shortest_distance= float('inf')
# for node in mapped_start_nodes:
#     for goal in mapped_goal_nodes:
#         path, current_distance = a_star(graph, node, goal)
#         print("Distance from", node, "to", mapped_goal_nodes, ":", path)
#         if current_distance < shortest_distance:
#             shortest_path = path
#             shortest_distance = current_distance

# print("Shortest Path:", shortest_path)

