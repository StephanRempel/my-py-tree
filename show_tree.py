import os
import sys


def print_tree(startpath, filesonly=False, dirsonly=False):
    '''Print a tree of the directory structure starting at startpath.
    
    If filesonly is True, only print the files.
    If dirsonly is True, only print the directories.
    The default is to print both files and directories.
    The output is indented to show the nesting of the directory structure.'''
    print(f"├ {os.path.basename(startpath)}")
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, "").count(os.sep)
        indent = "|   " * level
        print(f"{indent}├──{os.path.basename(root)}/")
        if filesonly:
            dirs.clear()  # Suppress the output of subdirectories
        elif dirsonly:
            files.clear()  # Suppress the output of files
        for file in files:
            subindent = "|   " * (level + 1)
            print(f"{subindent}├──{file}")
        for dir in dirs:
            subindent = "|   " * (level + 1)
            print(f"{subindent}├──{dir}/")


if __name__ == "__main__":
    theDir = r"..\.."
    if len(sys.argv) > 1:
        theDir = sys.argv[1]
    print('print_tree(theDir, dirsonly=True)')
    print_tree(theDir, dirsonly=True)
    print("-" * 60)
    print('print_tree(theDir, filesonly=True)')
    print_tree(theDir, filesonly=True)
    print("-" * 60)
    print('print_tree(theDir)')
    print_tree(theDir)
