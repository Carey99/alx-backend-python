#!/usr/bin/env python3
"""
    Familirize with the utils.access_nested_map function
    play with it in the python console
    write the first unit test for utils.access_nested_map
    create a TestAccessNestedMap class that
    inherits from unittest.TestCase
    implement the TestAccessNestedMap.test_access_nested_map method
    to test that the method returns the expected output
    decorate the method with @parameterized.expand to test the function
    for the following inputs:
        - nested_map={"a": 1}, path=("a",)
        - nested_map={"a": {"b": 2}}, path=("a",)
        - nested_map={"a": {"b": 2}}, path=("a", "b")
    for each input, test with assertEqual that the output is the expected one
    the body of the test method should not be larger than 2 lines
"""
import unittest
from parameterized import parameterized
from .utils import access_nested_map as anm


class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap class """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ test_access_nested_map method """
        @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
            ({"a": {"b": {"c": 3}}}, ("a", "b", "c"), 3),
            ({"a": {"b": {"c": {"d": 4}}}}, ("a", "b", "c", "d"), 4)
        ])
        def test_access_nested_map(self, nested_map, path, expected):
            """ test_access_nested_map method """
            self.assertEqual(anm(nested_map, path), expected)
