from models.adminKey import *
    
    
def get_admin_keys():
    try:
        hashed_key_obj = AdminKey.objects().first()
        return hashed_key_obj
    except Exception as err:
        print(err)