# Import necessary libraries
import os

from show_tree import print_tree

# import show_tree

# print_tree = show_tree.print_tree 



# Define function to test
def test_print_tree():
    # Define test directory with files and subdirectories
    test_dir = "./test_dir/"
    os.makedirs(test_dir, exist_ok=True)
    open(test_dir + "file1.txt", "w").close()
    open(test_dir + "file2.txt", "w").close()
    os.makedirs(test_dir + "subdir1/", exist_ok=True)
    os.makedirs(test_dir + "subdir2/", exist_ok=True)
    open(test_dir + "subdir1/file3.txt", "w").close()

    # Test with default parameters
    print_tree(test_dir)

    # Test with filesonly=True
    print_tree(test_dir, filesonly=True)

    # Test with dirsonly=True
    print_tree(test_dir, dirsonly=True)


# Call the test function
test_print_tree()
