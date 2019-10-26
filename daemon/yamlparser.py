from yaml import load, dump
from typing import Dict, List
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
from sys import exit
from os.path import abspath


class Config:
    def __init__(self, port: int, file_distribution_directory: str, save_file: bool, nodes: List=[]):
        self._port = port
        self._file_distribution_directory = file_distribution_directory
        self._save_file = save_file
        self._nodes = nodes
    
    def get_port(self) -> int:
        return self._port
    
    def get_file_distribution_directory(self) -> str:
        return abspath(self._file_distribution_directory)
    
    def get_save_file(self) -> bool:
        return self._save_file
    
    def get_nodes(self) -> List:
        return self._nodes

    def __str__(self):
        str_representation = f'<Config(port={self._port}, file_distribution_directory={self._file_distribution_directory}, save_file={self._save_file}, nodes={self._nodes})>'
        return str_representation 


def parse_config_file(config_file: str) -> Config:
    try:
        with open(config_file, 'r') as config_file:
            config = load(config_file, Loader=Loader)
    except FileNotFoundError:
        print(f'File {config_file} not found.')
        exit(1)
    else:
        return Config(**config)
