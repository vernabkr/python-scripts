# show duplicated videos in jellyfin-file-system
from pathlib import Path
from utils import is_video, file_size


def contain_nfo(folder: Path) -> bool:
    return len(list(folder.glob("*.nfo"))) > 0

root_folder = "I:\JAV"
path = Path(root_folder)

for folder in path.glob("**/"):
    if contain_nfo(folder):
        video_list = [file for file in folder.iterdir() if is_video(file.name)]
        if len(video_list) > 1:
            print("="*25)
            for video in video_list:
                print(f"{video} {file_size(str(video))} MB")

            