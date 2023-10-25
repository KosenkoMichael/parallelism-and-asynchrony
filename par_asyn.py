import os
import sys
import concurrent.futures
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


def main() -> None:
    keyword = input("input keyword >>>")
    file_pathes = input("input filepath >>>").split()

    results = []
    for file_path in file_pathes:
        future = concurrent.futures.ProcessPoolExecutor().submit(
            search_keyword_in_file, keyword, file_path)
        results.append(future)
    for future, path in zip(results, file_pathes):
        if future.result():
            print(f"Keyword '{keyword}' found in file: {path}")
    os.system("PAUSE")


if __name__ == '__main__':
    main()
