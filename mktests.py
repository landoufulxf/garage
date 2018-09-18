#!/usr/bin/env python3
import ast
from glob import iglob
import os
from os import path as osp

TEST_PATH_PREFIX = "tests"
TEST_FILE_PREFIX = "test"

TEST_FILE_TEMPLATE = """import pickle
import unittest
"""

PICKLE_TEST_TEMPLATE = """
class Test{class_name}(unittest.TestCase):

    def test_pickleable(self):
        obj = {class_name}(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
"""


class ClassVisitor(ast.NodeVisitor):
    def __init__(self):
        super().__init__()
        self.classes = []

    def visit_ClassDef(self, node):
        self.generic_visit(node)
        self.classes += [node.name]


for p in iglob("garage/**/*.py", recursive=True):

    # Skip __init__ and examples
    if ("__init__.py" in p or "config" in p or "examples" in p
            or "launchers" in p):
        continue

    test_path = osp.join(TEST_PATH_PREFIX, osp.dirname(p))
    test_file = osp.join(test_path, "test_{}".format(osp.basename(p)))

    # Make directory
    os.makedirs(osp.join(TEST_PATH_PREFIX, osp.dirname(p)), exist_ok=True)

    # Skip test files which already exist
    if osp.isfile(test_file):
        continue

    with open(p) as f:
        syntax = f.read()
        tree = ast.parse(syntax)
        v = ClassVisitor()
        v.visit(tree)

    # skip files without classes
    if not v.classes:
        continue

    # Build test file
    print(test_file)
    with open(test_file, mode="x") as test_py:
        test_py.write(TEST_FILE_TEMPLATE)

        # Add an import for each class in the module
        module_path = p[:-3].replace("/", ".")
        for c in sorted(v.classes):
            test_py.write("\n")
            test_py.write("from {} import {}".format(module_path, c))

        # Add a templated pickling test for each class
        test_py.write("\n")
        for c in sorted(v.classes):
            test_py.write("\n")
            test_py.write(PICKLE_TEST_TEMPLATE.format(class_name=c))
