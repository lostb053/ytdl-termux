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

link = "Pv56oBAfRhY"
data = yt({'quiet': True}).extract_info(link, download=False)


def get_resolutions(data: dict) -> list[list]:
    resolutions: list[list[str]] = []
    common_resolutions: dict = {}
    qualities: list[list[str]] = []
    common_qualities: dict = {}
    for i in data["formats"]:
        if i["video_ext"] != "none":
            resolutions.append([i["resolution"], i["vbr"]])
        if i["audio_ext"] != "none":
            qualities.append([i["asr"], i["abr"]])
    for res, br in resolutions:
        try:
            common_resolutions[res].append(int(br))
        except KeyError:
            common_resolutions[res] = [int(br)]
    for freq, br in qualities:
        try:
            common_qualities[freq].append(int(br))
        except KeyError:
            common_qualities[freq] = [int(br)]
    list_abr: list = []
    res_with_max_br: list[list] = []
    for i in common_resolutions.keys():
        max_br: int = max(common_resolutions[i])
        res_with_max_br.append([i, max_br])
    for i in common_qualities.keys():
        list_abr.append(max(common_qualities[i]))
    return res_with_max_br, max(list_abr)


def create_output_files(res_with_max_br: list[list[list]]):
    formats: list[list] = []
    for i in data["formats"]:
        for res, bitrate in res_with_max_br[0]:
            if i["video_ext"] != "none" and res in i["resolution"] and int(i["vbr"]) == bitrate:
                formats.append([res, bitrate, i])
        if i["audio_ext"] != "none" and int(i["abr"]) == res_with_max_br[1]:
            audio_data: dict = i
    n = 0
    format_id = ""
    out = f"""echo -e \"Sr.N. {yellow}Resolution{e}, {orange}Video Data{e}, {magenta}Audio Data{e}, {yellow}File Size{e}\""""
    audio_format = audio_data["format_id"]
    audio_size = int(audio_data['filesize'])/1024/1024
    for i in formats:
        out += "\n"
        n = n+1
        out += f"""echo -e \"{n}. {yellow}{i[2]['height']}p{e}, {orange}{i[1]} kbit/s, {i[2]['vcodec']}{e}{f", {magenta}{i[2]['acodec']}{e}" if i[2]['acodec'] != 'none' else ''}, {yellow}{str(round(int(i[2]['filesize'])/1024/1024+audio_size), 2)+' MB' if i[2]['filesize'] != 'none' else 'N/A'}{e}\"\nsleep 0.3"""
        format_id += f"({i[2]['format_id']})+({audio_format})\n"
    with open("print", "x") as file:
        file.write(out)
    with open("formats", "x") as file:
        file.write(format_id)


resulutions = get_resolutions(data)
create_output_files(resulutions)
