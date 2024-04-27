from models.calibrationFingerPrint import CalibrationPoint
import uuid

async def get_calibration_points_by_id(project_id):
    try:
        calibration_points = CalibrationPoint.objects(projectid=project_id)
        return calibration_points
    except Exception as err:
        print(err)

async def create_calibration_point(req):
    received_signals = req.received_signals
    try:
        cp_to_add = CalibrationPoint(
            projectId=req.projectId,
            name=f"calibration_point{uuid.uuid4()}",
            position={
                'x': req.pos_x,
                'y': req.pos_y,
            },
            radioMap={}
        )

        for signal in received_signals:
            cp_to_add.radioMap[signal.bssid] = signal.rssi

        # sus
        CalibrationPoint.objects.insert(cp_to_add)
    except Exception as err:
        print(err)

def add_maps():
    print("ADDING")

    try:
        c3 = CalibrationPoint(
            projectId="3",
            name="Calibration Point 7",
            position={'x': "13", 'y': "23", 'floor': "1"},
            radioMap={}
        )

        c3.radioMap['12:344:45336'] = 5
        c3.radioMap['12:344:456'] = 3
        c3.radioMap['12:344:4546'] = 3
        c3.radioMap['12:344:4526'] = 102
        c3.radioMap['12:344:4546'] = 15

        # sus
        # await c3.save()
        print("SUCCESS")
    except Exception as err:
        print("DD", err)