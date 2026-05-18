import os
import shutil
from generate_page import generate_pages_recursive

def main():
    delete_dir("public")
    copy_from_to("static", "public")
    generate_pages_recursive("content", "template.html", "public")

def copy_from_to(start, to):
    if not os.path.exists(start):
        raise FileNotFoundError(f"Folder doesnt exist: {folder}")
    if not os.path.exists(to):
        os.mkdir(to)
    dirs = os.listdir(start)
    for dir in dirs:
        source = os.path.join(start, dir)
        destination = os.path.join(to, dir)
        print(f"Copying {source} to {destination}")
        if os.path.isfile(source):
            shutil.copy(source, destination)
        else:
            copy_from_to(source, destination)

def delete_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)



main()
