#!/usr/bin/python3
""" TestFileStorageDocs classes """

from datetime import datetime
import inspect
import models
from models.engine import file_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
FileSystemStorage = file_storage.FileStorage
test_classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
                "Place": Place, "Review": Review, "State": State, "User": User}


class TestFileSystemStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of FileSystemStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.fs_f = inspect.getmembers(FileSystemStorage, inspect.isfunction)

    def test_pep8_conformance_file_storage(self):
        """Test that models/engine/file_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_file_storage(self):
        """Test tests/test_models/test_file_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_file_storage_module_docstring(self):
        """Test for the file_storage.py module docstring"""
        self.assertIsNot(file_storage.__doc__, None,
                         "file_storage.py needs a docstring")
        self.assertTrue(len(file_storage.__doc__) >= 1,
                        "file_storage.py needs a docstring")

    def test_file_storage_class_docstring(self):
        """Test for the FileSystemStorage class docstring"""
        self.assertIsNot(FileSystemStorage.__doc__, None,
                         "FileSystemStorage class needs a docstring")
        self.assertTrue(len(FileSystemStorage.__doc__) >= 1,
                        "FileSystemStorage class needs a docstring")

    def test_fs_func_docstrings(self):
        """Test for the presence of docstrings in FileSystemStorage methods"""
        for func in self.fs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFileSystemStorage(unittest.TestCase):
    """Test the FileSystemStorage class"""
    @unittest.skipIf(models.switch == 'db', "not testing file storage")
    def test_all_returns_dict(self):
        """Test that all returns the FileSystemStorage.__objects attr"""
        storage = FileSystemStorage()
        new_dict = storage.all()
        self.assertEqual(type(new_dict), dict)
        self.assertIs(new_dict, storage._FileSystemStorage__objects)

    @unittest.skipIf(models.switch == 'db', "not testing file storage")
    def test_new(self):
        """test that new adds an object to the FileSystemStorage.__objects attr"""
        storage = FileSystemStorage()
        save = FileSystemStorage._FileSystemStorage__objects
        FileSystemStorage._FileSystemStorage__objects = {}
        test_dict = {}
        for key, value in test_classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                storage.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, storage._FileSystemStorage__objects)
        FileSystemStorage._FileSystemStorage__objects = save

    @unittest.skipIf(models.switch == 'db', "not testing file storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""
        storage = FileSystemStorage()
        new_dict = {}
        for key, value in test_classes.items():
            instance = value()
            instance_key = instance.__class__.__name__ + "." + instance.id
            new_dict[instance_key] = instance
        save = FileSystemStorage._FileSystemStorage__objects
        FileSystemStorage._FileSystemStorage__objects = new_dict
        storage.save()
        FileSystemStorage._FileSystemStorage__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        string = json.dumps(new_dict)
        with open("file.json", "r") as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))
