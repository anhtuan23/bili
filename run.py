import subprocess
import sys
from urllib.parse import urlsplit, urlunsplit

import chime


def main():
    link = sys.argv[1]
    assert link is not None

    # Download method: 3.video 6.subtitles only 7.cover image only 8.audio only
    download_mode = "8" if (len(sys.argv) >= 3 and sys.argv[2] == "-a") else "3"

    if sys.platform.startswith("linux"):
        output_folder = "/media/kaestrl/Passport/Timo"
    elif sys.platform.startswith("darwin"):
        output_folder = "/Volumes/Passport/Timo"
    else:
        print("Error: Unknown. Exiting ...")
        return

    # remove all query parameters
    link = urlunsplit(urlsplit(link)._replace(query="", fragment=""))

    print(link)

    # subprocess.run(["source", "./env/bin/activate"])

    # subprocess.run(["env/bin/python", "start.py", "-h"])

    subprocess.run(
        f".venv/bin/python start.py -i {link} -d {download_mode} -p a --ym --yac --yad --yr --yf --mc hev --nar -o {output_folder} --vf mp4",
        shell=True,
    )

    # subprocess.run(
    #     [
    #         "env/bin/python",
    #         "start.py",
    #         f"-i {link}",
    #         "-d 3",  # Download method: 3.video 6.subtitles only 7.cover image only 8.audio only
    #         "-p <number>",  # The number of videos/parts you want to download. Use "a" to select all videos/parts.
    #         "--ym",  # Enable download with maximum quality
    #         "--yac",  # Enable "Continue Download" function.
    #         "--yad",  # Enable Enable delete useless files after merge is complete.
    #         "--yr",  # Enable download again automatically after the download failed.
    #         "--yf",  # Use ffmpeg
    #         "-mc hev",  # Prefer hev encoding
    #         "--nar",  # Download without aria2c
    #         "-F", # Only display video/audio quality and exit when downloading videos. (This is not affected by silent mode.)
    #         "-s",  # Enable Silent Mode.
    #         f"-o {output_folder}",
    #         "-vf mp4",  # The video format output from ffmpeg
    #     ]
    # )

    chime.success()


if __name__ == "__main__":
    main()
