from models.calibrationPoint_model import CalibrationPoint
import uuid

def get_calibration_points_by_id(project_id):
    try:
        calibration_points = CalibrationPoint.objects(projectId=project_id)
        return calibration_points
    except Exception as err:
        print(err)

def create_calibration_point(req_body):
    received_signals = req_body.received_signals

    try:
        cp_to_add = CalibrationPoint(
            projectId=req_body.projectId,
            name=f"calibration_point{uuid.uuid4()}",
            position={
                'x': req_body.position.x,
                'y': req_body.position.y,
                'floor': req_body.position.floor
            },
            radioMap={}
        )

        for signal in received_signals:
            cp_to_add.radioMap[signal.bssid] = signal.rss

        cp_to_add.save()
        print("Saved Calibration Point")
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

        c3.save()
        print("SUCCESS")
    except Exception as err:
        print("DD", err)