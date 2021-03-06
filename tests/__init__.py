# tests
# Testing for the confire module
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sun Jul 20 09:42:26 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: __init__.py [] benjamin@bengfort.com $

"""
Testing for the confire module
"""

##########################################################################
## Imports
##########################################################################

import unittest

##########################################################################
## Test Cases
##########################################################################

class InitializationTest(unittest.TestCase):

    def test_initialization(self):
        """
        Tests a simple world fact by asserting that 10*10 is 100.
        """
        self.assertEqual(10*10, 100)

    def test_import(self):
        """
        Can import confire
        """
        try:
            import confire
        except ImportError:
            self.fail("Unable to import the confire module!")
