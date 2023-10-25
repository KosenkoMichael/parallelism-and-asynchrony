import concurrent.futures
import os
from time import sleep


def search_keyword_in_file(keyword: str, filepath: str) -> bool:
    """
    opening a file and checking case insensitively
    """
    with open(filepath, 'r') as file:
        for line in file:
            if keyword.lower() in line.lower():
                return True
    return False


def path_app(path: str) -> list:
    """
    will return the path to all files in path/...
    """
    file_pathes = []

    file_names = os.listdir(path)
    for file_name in file_names:
        file_pathes.append(os.path.join(path, file_name))
    return file_pathes


def main() -> None:
    keyword = input("input keyword >>>")
    path = input("input folderpath >>>")
    file_pathes = path_app(path)

    results = []
    for file_path in file_pathes:
        future = concurrent.futures.ProcessPoolExecutor().submit(
            search_keyword_in_file, keyword, file_path)
        results.append(future)
    for future, path in zip(results, file_pathes):
        if future.result():
            print(f"Keyword '{keyword}' found in file: {path}")
    sleep(10)


if __name__ == '__main__':
    main()
