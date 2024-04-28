from models.accessPoint import *

async def get_access_points_by_id(project_id):
    try:
        access_points = AccessPoint.objects(projectid = project_id)
        access_point_list = list(access_points)
        return access_point_list
    
    except Exception as err:
        print(err)


async def add_multiple_access_points(access_point_array, project_id):
    try:
        access_points = [
            AccessPoint(projectid=project_id, ssid=signal.ssid, bssid=signal.bssid)
            for signal in access_point_array
        ] 
        AccessPoint.objects.insert(access_points)
        print("## new access points saved")
    except Exception as err:
        print(err)
