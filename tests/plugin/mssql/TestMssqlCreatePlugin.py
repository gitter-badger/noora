#!/usr/bin/env python
import unittest
import os
import noora
import argparse
import json
from noora.plugins.mssql.create.CreatePlugin import CreatePlugin
from noora.system.Properties import Properties
from noora.system.App import App


class TestBase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreatePass(self):
        NOORA_DIR = os.path.dirname(noora.__file__)
        CURRENT_DIR = os.path.abspath('.')

        properties = Properties()
        properties.set_property("noora.dir", NOORA_DIR)
        properties.set_property("current.dir", CURRENT_DIR)
        properties.set_property("plugin.dir", os.path.join(NOORA_DIR, 'plugins'))
        properties.set_property("project.file", "myproject.json")

        app = App()
        f = app.get_config_file(properties)
        f = open(f.get_url())

        data = json.load(f)
        for key in data.keys():
            properties.set_property(key, data[key])

        parser = argparse.ArgumentParser(description="mynoora, a sql deployment tool", add_help=False)
        parser.add_argument("commands", help="display a square of a given number", type=str, nargs='+')
        parser.add_argument('-r', action='store_true', help='show the revision')
        parser.add_argument('-h', type=str, help='host', required=False)
        parser.add_argument('-s', type=str, help='schema', required=False)
        parser.add_argument('-e', type=str, help='environment', required=False)
        parser.add_argument('-a', type=str, help='alias', required=False)

        arguments = parser.parse_args(['create', '-h=elsevierdb4.c07v9zv3jhxs.eu-west-1.rds.amazonaws.com,1433'])

        plugin = CreatePlugin()
        plugin.execute(arguments, properties)


if __name__ == '__main__':
    unittest.main()
