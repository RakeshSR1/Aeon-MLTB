import os
import re

def upload_to_gdrive(file_path):
    output = os.popen(f"./gdrive upload \"{file_path}\" --share").read()
    match = re.search(r'Id:\s*(\S+)', output)
    if match:
        file_id = match.group(1)
        return f"https://drive.google.com/file/d/{file_id}/view"
    return None
