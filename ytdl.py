import os
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
data = yt({'quiet': True, 'dump_single_json': True}).extract_info(link, download=False)
HOME = os.getenv("HOME")


def create_output_files(data: dict):
    video_formats: list[dict] = []
    audio_formats: list[dict] = []
    for i in data["formats"]:
        if i["video_ext"] != "none":
            video_formats.append(i)
        if i["audio_ext"] != "none":
            audio_formats.append(i)

    n = 0
    video_output = f"""echo -e \"Sr.N. {yellow}Resolution{e}, {orange}Video Data{e}, {magenta}Audio Data{e}, {yellow}File Size & Protocol{e}\"\nsleep 0.3\n"""
    video_format_id = ""
    for i in video_formats:
        n = n+1
        video_output += f"""echo -e \"{n}. {yellow}{i['height']}p{f' ({i["fps"]} fps)' if 'fps' in i.keys() and i['fps']>50 else ''}{e}, {orange}{i['vbr']} kbit/s, {i['vcodec']}{e}{f", {magenta}{i['acodec']}{e}" if i['acodec'] != 'none' else ''}, {yellow}{str(round(int(i['filesize'])/1024/1024, 2))+' MB' if i['filesize'] else 'N/A'}, {i['protocol']}{e}\"\nsleep 0.3\n"""
        video_format_id += f"({i['format_id']})\n"

    n = 0
    audio_output = f"""echo -e \"Sr.N. {yellow}Bitrate{e}, {orange}Sampling Rate{e}, {magenta}Codec{e}, {yellow}File Size & Protocol{e}\"\nsleep 0.3\n"""
    audio_format_id = ""
    for i in audio_formats:
        n = n+1
        audio_output += f"""echo -e \"{n}. {yellow}{i['abr']} kbit/s{e}, {orange}{i['asr']} Hz{e}, {magenta}{i['acodec']}{e}, {yellow}{str(round(int(i['filesize'])/1024/1024, 2))+' MB' if i['filesize'] else 'N/A'}, {i['protocol']}{e}\"\nsleep 0.3\n"""
        audio_format_id += f"({i['format_id']})\n"
    
    try:
        subtitles_list = data['subtitles'].keys()
        subtitle_output = f"""echo -e \"{yellow}List of available subtitles{e}\"\nsleep 0.3\n"""
        for i in list(subtitles_list):
            subtitle_output += f"""echo -e \"{cyan}{i}{e}{' '*(12 - len(i))}{data['subtitles'][i][0]['name']}\"\nsleep0.3\n"""
        with open(HOME+"/print_sub_data", "x") as file:
            file.write(subtitle_output)
    except KeyError:
        pass

    with open(HOME+"/print_vid_data", "x") as file:
        file.write(video_output)
    with open(HOME+"/vid_formats", "x") as file:
        file.write(video_format_id)

    with open(HOME+"/print_aud_data", "x") as file:
        file.write(audio_output)
    with open(HOME+"/aud_formats", "x") as file:
        file.write(audio_format_id)


create_output_files(data)