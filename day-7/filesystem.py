class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.size = 0
    
    def add_child(self, child):
        self.children.append(child)
    
    def set_size(self, size):
        self.size = size
    
    def get_size(self):
        return self.size
    
    def get_name(self):
        return self.name

    def __str__(self):
        return self.name + " " + str(self.size) + " " + str(self.children)

class Filesystem:
    def __init__(self):
        self.root = Node("root")
        self.current = self.root
    
    def cd(self, name):
        if name == "..":
            self.current = self.current.parent
        elif name == "/":
            self.current = self.root
        else:
            for child in self.current.children:
                if child.get_name() == name:
                    self.current = child
                    return
            print("Directory not found")
    
    def ls(self):
        for child in self.current.children:
            print(child.get_name())

    def add_dir(self, name):
        new_dir = Node(name)
        new_dir.parent = self.current
        self.current.add_child(new_dir)
    
    def add_file(self, name, size):
        new_file = Node(name)
        new_file.set_size(size)
        self.current.add_child(new_file)

    def get_total_size(self, node):
        total = 0
        for child in node.children:
            if child.children:
                total += self.get_total_size(child)
            else:
                total += child.get_size()
        return total

    def set_size_of_all_dirs(self, node):
        for child in node.children:
            if child.children:
                child.set_size(self.get_total_size(child))
                self.set_size_of_all_dirs(child)
        node.set_size(self.get_total_size(node))

    def set_sizes(self):
        self.set_size_of_all_dirs(self.root)

    def print_all(self, node):
        print(node.get_name(), node.get_size())
        for child in node.children:
            self.print_all(child)


class Parser:
    def __init__(self):
        self.fs = Filesystem()
        self.list_files = False

    def parse(self, line):
        tokens = line.split(" ")
        if self.list_files:
            if tokens[0] == "$":
                self.list_files = False
            elif tokens[0] == "dir":
                self.fs.add_dir(tokens[1])
            else:
                self.fs.add_file(tokens[1], int(tokens[0]))
        if not(self.list_files):
            if tokens[1] == "cd":
                self.fs.cd(tokens[2])
            elif tokens[1] == "ls":
                self.list_files = 1         
    
    

def count_sum(node):
    total = 0
    if node.size <= 100000 and len(node.children) > 0:
        total += node.size
    for child in node.children:
        total += count_sum(child)
    return total


folder_options = []
def find_folder_to_delete(node, requred_size):
    global folder_options
    if node.size > requred_size and len(node.children) > 0:
        folder_options.append(node)
    for child in node.children:
        find_folder_to_delete(child, requred_size)
    

def find_folder_to_delete_main(root):
    global folder_options
    used_size = root.get_size()
    required_size = 30000000
    filesystem_size = 70000000

    available_size = filesystem_size - used_size
    required_size = required_size - available_size
    find_folder_to_delete(root, required_size)
    folder_options.sort(key=lambda x: x.get_size())
    print(folder_options[0].get_name(), folder_options[0].get_size())



def main():
    parser = Parser()

    with open("day-7/input.in", "r") as f:
        for line in f.readlines():
            parser.parse(line.strip())

    parser.fs.set_sizes()
    # parser.fs.print_all(parser.fs.root)
    print(count_sum(parser.fs.root))
    find_folder_to_delete_main(parser.fs.root)

if __name__ == "__main__":
    main()