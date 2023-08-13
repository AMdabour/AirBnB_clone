#!/usr/bin/python3
"""test cases for the base_module module"""


import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel





class Test_constructor(unittest.TestCase):

    obj = BaseModel()
    obj.name = "Model Name"
    obj.my_number = 2

    
    def test_consturctor_with_no_kwargs(self):
        self.assertIsInstance(self.obj, BaseModel)
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.created_at, datetime)
        self.assertIsInstance(self.obj.updated_at, datetime)
        self.assertEqual(self.obj.name, "Model Name")
        self.assertEqual(self.obj.my_number, 2)

    def test_kwargs_constructor(self):
            
        data = {
            'id': 'some_id',
            'created_at': '2023-08-13T12:34:56.789',
            'updated_at': '2023-08-13T12:34:56.789',
            'name': 'Test Model'
        }
        obj = BaseModel(**data)

        self.assertIsInstance(self.obj, BaseModel)
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.created_at, datetime)
        self.assertIsInstance(self.obj.updated_at, datetime)

        self.assertEqual(obj.id, 'some_id')
        self.assertEqual(obj.name, 'Test Model')
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertEqual(self.obj.name, "Model Name")
        self.assertEqual(self.obj.my_number, 2)
