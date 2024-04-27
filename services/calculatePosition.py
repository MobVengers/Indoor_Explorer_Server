from utils import calibrationPoints
from utils.accessPoint import *
from utils.calibrationPoints import *
from constants import RSS_NOT_RECEIVED
import math
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse


async def calculate_position(req):
    try:
        project_id = req.projectId
        received_signals = req.received_signals
        access_point_list = await get_access_points_by_id(project_id)
        initially_received_rssi_values = signals_to_map(received_signals)

        received_database_rssi_values = {}
        not_received_count = 0

        for access_point in access_point_list:
            if access_point.bssid not in initially_received_rssi_values:
                not_received_count += 1
                received_database_rssi_values[access_point.bssid] = RSS_NOT_RECEIVED
            else:
                received_database_rssi_values[access_point.bssid] = initially_received_rssi_values[access_point.bssid]

        if not_received_count == len(access_point_list):
            err = "No access point in database matches the received signals"
            return JSONResponse(content={"message": str(err)}, status_code=500)       
        else:
            finger_print = await wknn_algorithm(received_database_rssi_values, project_id)
            print(finger_print)
            JSONResponse(content={"message": "done"}, status_code=200)
            # return {'message': finger_print}

    except Exception as err:
        return JSONResponse(content={"message": str(err)}, status_code=500)       

    
def calculate_weighted_average_k_distance_locations(location_distances):
    try:
        k = 3
        location_weight = 0.0
        sum_weights = 0.0
        weighted_sum_x = 0.0
        weighted_sum_y = 0.0

        floor = "Null"
        x = 0.0
        y = 0.0

        k_min = min(k, len(location_distances))
        floor_voting = {}
        for i in range(k_min):
            if location_distances[i]['distance'] != 0.0:
                location_weight = 1 / location_distances[i]['distance']
            else:
                location_weight = 100

            location_distance_cali_point_pos = location_distances[i]['calibrationPointPosition']

            x = location_distance_cali_point_pos['x']
            y = location_distance_cali_point_pos['y']

            floor_key = location_distance_cali_point_pos['floor']
            if floor_key in floor_voting:
                floor_voting[floor_key] += 1
            else:
                floor_voting[floor_key] = 1

            sum_weights += location_weight
            weighted_sum_x += location_weight * x
            weighted_sum_y += location_weight * y

        weighted_sum_x /= sum_weights
        weighted_sum_y /= sum_weights
        floor = get_floor_by_value(floor_voting)

        position_to_return = {
            'x': weighted_sum_x,
            'y': weighted_sum_y,
            'floor': floor,
        }
        return position_to_return

    except Exception as err:
        print(err)
        return "Null"


async def wknn_algorithm(received_database_rssi_values, project_id):
    calibration_point_list = await get_calibration_points_by_id(project_id)
    location_distance_results = []

    try:
        for calibration_point in calibration_point_list:
            radio_map = calibration_point.radiomap
            current_distance = calculate_euclidean_distance(radio_map, received_database_rssi_values)
            if current_distance == float('-inf'):
                err = "Negative Infinity Distance Error"
                return JSONResponse(content={"message": str(err)}, status_code=500)  

            location_distance_to_add = {
                'calibrationPointId': calibration_point.id,
                'calibrationPointName': calibration_point.name,
                'calibrationPointPosition': calibration_point.position,
                'distance': current_distance
            }
            location_distance_results.append(location_distance_to_add)

        sorted_location_distances = sorted(location_distance_results, key=lambda x: x['distance'])
        calculated_position = calculate_weighted_average_k_distance_locations(sorted_location_distances)

        return calculated_position

    except Exception as err:
        raise err

def signals_to_map(received_signals):
    rssi_value_map = {}
    for signal in received_signals:
        rssi_value_map[signal.bssid] = signal.rssi
    return rssi_value_map

def calculate_euclidean_distance(radio_map, received_rssi_values):
    print(">>", radio_map, received_rssi_values)
    final_distance = 0
    temp_value_one = 0.0
    temp_value_two = 0.0
    temp_distance = 0.0

    # if len(radio_map) != len(received_rssi_values):
    #     print(">>>")
    #     return float('-inf')

    try:
        for bssid, rss in radio_map.items():
            if rss == RSS_NOT_RECEIVED:
                temp_value_one = 0.0
            else:
                temp_value_one = rss

            if received_rssi_values.get(bssid) == RSS_NOT_RECEIVED:
                temp_value_two = 0.0
            else:
                temp_value_two = received_rssi_values[bssid]

            temp_distance = temp_value_one - temp_value_two
            temp_distance **= 2

            final_distance += temp_distance
    except Exception as e:
        return float('-inf')

    return final_distance ** 2

def get_floor_by_value(floor_voting_map):
    floor_with_highest_vote = float('-inf')
    for floor, vote_count in floor_voting_map.items():
        temp_vote_count = -1

        if temp_vote_count == -1 or temp_vote_count < vote_count:
            temp_vote_count = vote_count
            floor_with_highest_vote = floor

    return floor_with_highest_vote

