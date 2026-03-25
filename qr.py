import qrcode
import os
import uuid

BASE_URL = "http://172.16.210.94:8000"

def qr_generate(org_name, base_url):

    img = qrcode.make(f"{BASE_URL}/{org_name}/form")
    
    folder = "static/qr"
    os.makedirs(folder, exist_ok=True)

    random_uuid = uuid.uuid4()

    filepath = f"{folder}/{org_name}{random_uuid}.png"
    img.save(filepath)

    return filepath