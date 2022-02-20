import sys
import subprocess
from urllib.parse import urlsplit, urlunsplit

def main():
    link = sys.argv[1]
    assert link is not None

    output_folder = "/Volumes/Passport/Timo"

    # remove all query parameters
    link = urlunsplit(urlsplit(link)._replace(query="", fragment=""))

    print(link)
    

    # subprocess.run(["source", "./env/bin/activate"])

    # subprocess.run(["env/bin/python", "start.py", "-h"])

    subprocess.run(
        f"env/bin/python start.py -i {link} -d 3 --ym --yac --yr --yf --mc hev --nar -o {output_folder} --vf mp4",
        shell=True,
    )

    # subprocess.run(
    #     [
    #         "env/bin/python",
    #         "start.py",
    #         f"-i {link}",
    #         "-d 3",  # Download method: 3.video
    #         "--ym",  # Enable download with maximum quality
    #         "--yac",  # Enable "Continue Download" function.
    #         "--yr",  # Enable download again automatically after the download failed.
    #         "--yf",  # Use ffmpeg
    #         "-mc hev",  # Prefer hev encoding
    #         "--nar",  # Download without aria2c
    #         f"-o {output_folder}",
    #         "-vf mp4",  # The video format output from ffmpeg
    #     ]
    # )


if __name__ == "__main__":
    main()
