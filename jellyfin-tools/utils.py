import os


def is_video(filename: str):
    video_shuffix = [".mp4", ".avi", ".rmvb", ".wmv", ".mov", ".mkv", ".flv", ".ts", ".webm", ".iso", ".mpg", ".m4v"]
    for shuffix in video_shuffix:
        if filename.endswith(shuffix):
            return True
    return False


def file_size(filepath: str):
    fsize = os.path.getsize(filepath)
    fsize_gb = fsize / float(1024*1024)
    return round(fsize_gb, 2)
