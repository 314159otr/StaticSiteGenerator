import os
from block_markdown import markdown_to_html_node

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    from_file = open(from_path, "r")
    markdown = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    title = extract_title(markdown)
    html_string = markdown_to_html_node(markdown).to_html() 
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_string)
    template = template.replace("href=\"/", f"href=\"{basepath}")
    template = template.replace("src=\"/", f"src=\"{basepath}")

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)
    to_file.close()

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise Exception("There is no title header")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    dirs = os.listdir(dir_path_content)
    for dir in dirs:
        path_source = os.path.join(dir_path_content, dir)
        dir_dest = dir.replace(".md", ".html")
        path_destination = os.path.join(dest_dir_path, dir_dest)
        if os.path.isfile(path_source):
            generate_page(path_source, template_path, path_destination, basepath)
        else:
            generate_pages_recursive(path_source, template_path, path_destination, basepath)
