import requests
import re
import time
import urllib
import queue

def cut_string(input_str, head, tail):
    if isinstance(
            head,
            str) and isinstance(
            tail,
            str) and isinstance(
                input_str,
            str):
        start = input_str.find(head) + len(head)
        end = input_str.find(tail, start)

        rt_str = ""
        for index in range(start, end):
            rt_str += input_str[index]
        return rt_str
    else:
        raise TypeError("Inputs are not string!")


url_m = "https://bbs.meizu.cn/forum.php?mod=viewthread&tid=6591622&extra=&highlight=%E8%87%AA%E8%A1%8C%E8%BD%A6%E6%B6%82%E8%A3%85&page=1000"


def get_img_url(url):
    content = requests.get(url).text
    all_url = re.findall("[a-zA-z]+://[^\s]*", content)
    matched_url = list()

    for url in all_url:
        if "bbsimage.res.meizu.com/forum" in url:
            if url not in matched_url:
                matched_url.append(url)

    return matched_url

old_matches = get_img_url(url_m)
print(old_matches)

while True:
    # 10S delay
    old = time.time()
    while time.time() - old < 30:
        pass

    new_matches = get_img_url(url_m)
    new_img = list()

    if len(new_matches) < len(old_matches):
        # new page
        pass
    else:
        # still in the same page
        if len(new_matches) > len(old_matches):
            # the page has been append some new img
            for u in new_matches:
                if u not in old_matches:
                    new_img.append(u)
        elif len(new_matches) == len(old_matches):
            # no new IMG
            print("No New.")
            pass

    old_matches = new_matches

    if len(new_img):

        for u in new_img:

            u=str(u).replace("\"","")

            def get_file_name(url):
                return re.findall(r"/forum/.*", url)[0][18::]

            r = requests.get(u)
            with open(get_file_name(u), "wb") as code:
                code.write(r.content)
