import os


def filter_for_subfolders(folder, filter_str=""):
    subfolders = [ f.path for f in os.scandir(folder) if f.is_dir() and f.name.endswith(filter_str) ]
    return subfolders
