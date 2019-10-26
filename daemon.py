#!/usr/bin/env python
import argparse
from daemon.yamlparser import parse_config_file
from daemon.server import serve


def parse_args():
    parser = argparse.ArgumentParser(description='This is a distributed, asynchronous, network file daemon.')
    parser.add_argument(
        action='store',
        dest='config',
        type=str,
        help='Daemon config file')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    config = parse_config_file(args.config)
    serve(config)