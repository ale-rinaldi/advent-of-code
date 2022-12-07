from typing import Optional, Dict

with open("d7-input.txt") as f:
    data = f.read().splitlines()


class File:
    name: str
    parent: "Directory"
    size: int


class Directory:
    name: str
    parent: Optional["Directory"]
    subdirectories: Dict[str, "Directory"]
    files: Dict[str, File]

    def get_subdirectory(self, name):
        if name in self.subdirectories:
            return self.subdirectories[name]
        subdir = new_directory(name, self)
        self.subdirectories[name] = subdir
        return subdir

    def add_file(self, name, size):
        if name in self.files:
            print(f"WARN file {name} was already defined in this directory, overwriting it")
        new_file = File()
        new_file.name = name
        new_file.size = size
        self.files[name] = new_file

    def size(self):
        size = 0
        for subdir in self.subdirectories.values():
            size += subdir.size()
        for file in self.files.values():
            size += file.size
        return size


def new_directory(name, parent):
    newdir = Directory()
    newdir.name = name
    newdir.parent = parent
    newdir.subdirectories = {}
    newdir.files = {}
    return newdir

root = None
current_directory: Optional[Directory] = None
for line in data:
    parts = line.split(" ")
    if parts[0] == "$" and parts[1] == "cd":
        if parts[2] == "/":
            if root is None:
                root = new_directory("/", None)
            current_directory = root
        if parts[2] == "..":
            current_directory = current_directory.parent
        else:
            current_directory = current_directory.get_subdirectory(parts[2])
    elif parts[0] == "$" and parts[1] == "ls":
        continue
    else:
        if parts[0] == "dir":
            current_directory.get_subdirectory(parts[1])
        else:
            current_directory.add_file(parts[1], int(parts[0]))

total_space = 70000000
free_space = total_space - root.size()
needed_space = 30000000
to_free = needed_space - free_space
folders_with_enough_space = []
def get_subdirs_size(directory: Directory):
    global res
    for subdir in directory.subdirectories.values():
        if subdir.size() > to_free:
            folders_with_enough_space.append(subdir.size())
        get_subdirs_size(subdir)

get_subdirs_size(root)
print(min(folders_with_enough_space))
