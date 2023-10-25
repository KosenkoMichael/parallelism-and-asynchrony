import concurrent.futures
import sys
import os


def search_keyword_in_file(keyword: str, filepath: str) -> bool:
    """
    открытие файла и проверка без учета регистра
    """
    with open(filepath, 'r') as file:
        for line in file:
            if keyword.lower() in line.lower():
                return True
    return False


def path_app(path: str) -> list:
    """
    вернет пути к всем файлам лежищим в path/...
    """
    file_pathes = []

    file_names = os.listdir(path)
    for file_name in file_names:
        file_pathes.append(os.path.join(path, file_name))
    return file_pathes


def main() -> None:
    """
    пример вызова функции: python par_asyn.py "i'm here" "data"
    """
    if len(sys.argv) != 3:
        print("Usage: python par_asyn.py <keyword> <folder_path>")
        sys.exit(1)

    keyword = sys.argv[1]
    path = sys.argv[2]
    file_pathes = path_app(path)

    results = []
    for file_path in file_pathes:
        future = concurrent.futures.ProcessPoolExecutor().submit(
            search_keyword_in_file, keyword, file_path)
        results.append(future)
    for future, path in zip(results, file_pathes):
        if future.result():
            print(f"Keyword '{keyword}' found in file: {path}")


if __name__ == '__main__':
    main()
