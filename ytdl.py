import sys
from yt_dlp import YoutubeDL as yt

red="\e[31m"
green="\e[32m"
yellow="\e[33m"
orange="\e[34m"
magenta="\e[35m"
cyan="\e[36m"
e="\e[0m"
b="\e[1m"
i="\e[3m"

link = sys.argv[1]
data = yt({'quiet': True}).extract_info(link, download=False)


def get_resolutions(data: dict) -> list[list]:
    resolutions: list[list[str]] = []
    common_resolutions: dict = {}
    for i in data["formats"]:
        if i["video_ext"] != "none":
            resolutions.append([i["resolution"], i["vbr"]])
    for res, br in resolutions:
        try:
            common_resolutions[res].append(int(br))
        except KeyError:
            common_resolutions[res] = [int(br)]
    res_with_max_br: list[list] = []
    for i in common_resolutions.keys():
        max_br: int = max(common_resolutions[i])
        res_with_max_br.append([i, max_br])
    return res_with_max_br


def create_output_files(res_with_max_br: list[list]):
    formats: list[list] = []
    for res, bitrate in res_with_max_br:
        for i in data["formats"]:
            if i["video_ext"] != "none" and res in i["resolution"] and int(i["vbr"]) == bitrate:
                formats.append([res, bitrate, i])
    n = 0
    format_id = ""
    out = f"""echo -e \"Sr.N. {yellow}Resolution{e}, {orange}Video Data{e}, {magenta}Audio Data{e}\""""
    for i in formats:
        out += "\n"
        n = n+1
        out += f"""echo -e \"{n}. {yellow}{i[2]['height']}p{e}, {orange}{i[1]} kbit/s, {i[2]['vcodec']}{e}{f", {magenta}{i[2]['acodec']}{e}" if i[2]['acodec'] != 'none' else ''}\"\nsleep 0.3"""
        format_id += i[2]['format_id']+"\n"
    with open("print", "x") as file:
        file.write(out)
    with open("formats", "x") as file:
        file.write(format_id)


resulutions = get_resolutions(data)
create_output_files(resulutions)
