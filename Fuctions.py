import re

def get_file_name(url):
    return re.findall(r"/forum/.*", url)[0][18::]