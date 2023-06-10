# Import necessary libraries
import logging
import os

import pytest

logger = logging.getLogger(__name__)


# Define fixture to create test directory
@pytest.fixture(scope="module")
def test_dir():
    test_dir = "./test_dir/"
    os.makedirs(test_dir, exist_ok=True)
    open(test_dir + "file1.txt", "w").close()
    open(test_dir + "file2.txt", "w").close()
    os.makedirs(test_dir + "subdir1/", exist_ok=True)
    os.makedirs(test_dir + "subdir2/", exist_ok=True)
    open(test_dir + "subdir1/file3.txt", "w").close()
    yield test_dir
    os.removedirs(test_dir)


# Define test function
def test_print_tree(test_dir, capsys):
    # Import function to test
    from show_tree import print_tree

    # Test with default parameters
    print_tree(test_dir)
    captured = capsys.readouterr()
    logger.debug(captured.out)
    expected = """test_dir/\n├── file1.txt
├── file2.txt
├── subdir1/\n│   └── file3.txt
└── subdir2/\n
"""
    logger.debug(expected)
    assert captured.out == expected

    # Test with filesonly=True
    print_tree(test_dir, filesonly=True)
    captured = capsys.readouterr()
    assert (
        captured.out
        == """test_dir/\n├── file1.txt
└── file2.txt

"""
    )

    # Test with dirsonly=True
    print_tree(test_dir, dirsonly=True)
    captured = capsys.readouterr()
    assert (
        captured.out
        == """test_dir/\n├── subdir1/\n└── subdir2/\n
"""
    )
