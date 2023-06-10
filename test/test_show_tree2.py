import logging
import os

import pytest

# logging.basicConfig(
#     filename="example.log",
#     filemode="w",
#     format="%(asctime)s %(levelname)s:%(message)s",
#     encoding="utf-8",
#     level=logging.DEBUG,
# )
# logging.debug("This message should go to the log file")
# logging.info("So should this")
# logging.warning("And this, too")
# logging.error("And non-ASCII stuff, too, like Øresund and Malmö")


# Define fixture to create test directory
@pytest.fixture(scope="module")
def test_dir():
    test_dir = "./test_dir/"
    logger = logging.getLogger(__name__)
    logger.debug("Going to create test directory: %s" % test_dir)
    os.makedirs(test_dir, exist_ok=True)
    open(test_dir + "file1.txt", "w").close()
    open(test_dir + "file2.txt", "w").close()
    os.makedirs(test_dir + "subdir1/", exist_ok=True)
    os.makedirs(test_dir + "subdir2/", exist_ok=True)
    open(test_dir + "subdir1/file3.txt", "w").close()
    yield test_dir
    # os.removedirs(test_dir)
    os.remove(test_dir + "file1.txt")
    os.remove(test_dir + "file2.txt")
    os.remove(test_dir + "subdir1/file3.txt")
    os.removedirs(test_dir + "subdir1/")
    os.removedirs(test_dir + "subdir2/")
    if os.path.exists(test_dir):
        logger.debug("Going to remove test directory: %s" % test_dir)
        os.removedirs(test_dir)
    else:
        logger.debug("Test directory does not exist: %s" % test_dir)


# Define test function for default parameters
def test_print_tree_default(test_dir, capsys):
    # Import function to test
    from show_tree import print_tree

    # Test with default parameters
    print_tree(test_dir)
    captured = capsys.readouterr()
    logger = logging.getLogger(__name__)
    logger.debug(f'{captured.out=}')
    expected_output = "├ \n├──/\n|   ├──file1.txt\n|   ├──file2.txt\n|   ├──subdir1/\n|   ├──subdir2/\n├──subdir1/\n|   ├──file3.txt\n├──subdir2/\n"
    logger.debug(f'{expected_output=}')
    assert captured.out == expected_output

    # Add log message
    logger.debug("Ran test_print_tree_default")


# Define test function for filesonly=True
def test_print_tree_filesonly(test_dir, capsys):
    # Import function to test
    from show_tree import print_tree

    # Test with filesonly=True
    print_tree(test_dir, filesonly=True)
    captured = capsys.readouterr()
    logger = logging.getLogger(__name__)
    logger.debug(f'{captured.out=}') 
    expected_output = '├ \n├──/\n|   ├──file1.txt\n|   ├──file2.txt\n'
    logger.debug(f'{expected_output=}')
    assert captured.out == expected_output

    # Add log message
    logger.debug("Ran test_print_tree_filesonly")


# Define test function for dirsonly=True
def test_print_tree_dirsonly(test_dir, capsys):
    # Import function to test
    from show_tree import print_tree

    # Test with dirsonly=True
    print_tree(test_dir, dirsonly=True)
    captured = capsys.readouterr()
    logger = logging.getLogger(__name__)
    logger.debug(f'{captured.out=}') 
    expected_output = '├ \n├──/\n|   ├──subdir1/\n|   ├──subdir2/\n├──subdir1/\n├──subdir2/\n'
    logger.debug(f'{expected_output=}') 
    assert captured.out == expected_output

    # Add log message
    logger.debug("Ran test_print_tree_dirsonly")
