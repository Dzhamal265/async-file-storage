from unittest import TestCase
from daemon.yamlparser import parse_config_file, Config
from typing import List

class ConfigParserTest(TestCase):
    def test_config_parser(self):
        res = parse_config_file('/home/dzhamal/async-file-storage/daemonsconfigs/config.yaml')
        self.assertIsInstance(res, Config)

    def test_config_class(self):
        res = parse_config_file('/home/dzhamal/async-file-storage/daemonsconfigs/config.yaml')
        self.assertIsInstance(res.get_file_distribution_directory(), str)
        self.assertIsInstance(res.get_nodes(), List)
        self.assertIsInstance(res.get_port(), int)
        self.assertIsInstance(res.get_save_file(), bool)


class DaemonTest(TestCase):
    pass