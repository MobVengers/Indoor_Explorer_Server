from models.accessPoint import AccessPoint

async def get_access_points_by_id(project_id):
    try:
        # access_points = await AccessPoint.find({"projectId": project_id}).exec()
        access_points = AccessPoint.objects()
        return access_points
    except Exception as err:
        print(err)

async def add_multiple_access_points(access_point_array, project_id):
    access_points_to_add = [
        {"projectId": project_id, **access_point} for access_point in access_point_array
    ]
    await AccessPoint.insert_many(access_points_to_add)