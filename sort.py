import sys
from pathlib import Path

def sort_folder(path: Path, elements = []) -> list:
    for item in path.iterdir():
        if item.is_dir():
            sort_folder(item, elements)
        else:
            elements.append(item)   
    #return elements   

    for i in elements:
        print(i.suffix.lower())     


def main() -> str:
    try:
        path = Path(sys.argv[1])
    except IndexError:
        return "Please, enter path to folder"    

    if not path.exists():
        return "Check folder PATH and try again"

    if not path.is_dir():
        return "You can sort only folders. Specify folder"
    
    print(sort_folder(path))
    
if __name__ == '__main__':
    main()