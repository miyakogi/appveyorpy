#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_appveyorpy
----------------------------------

Tests for `appveyorpy` module.
"""

import unittest

import appveyorpy


class TestAppveyorpy(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_something(self):
        self.assertEqual(appveyorpy.add(3, 4), 7)
