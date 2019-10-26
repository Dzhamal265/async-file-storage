from aiohttp.web import RouteTableDef, Response, HTTPNotFound
from os.path import join
from typing import List
import asyncio

from .client import fetch

routes = RouteTableDef()

async def read_file(request_file: str) -> str:
    file_content = ''
    with open(request_file) as file:
        file_content = file.read()
    return file_content

async def write_file(request_file: str, data: str) -> None:
    with open(request_file, 'w') as file:
        file.write(data)

async def prepare_nodes(filename: str, nodes: List) -> List:
    prepared_nodes = []
    for node in nodes:
        task = asyncio.create_task(fetch(node['url'], filename))
        prepared_nodes.append(task)
    return prepared_nodes    

@routes.get('/{filename}')
async def get_file(request: 'Request') -> Response:
    filename = request.match_info['filename']
    request_file = join(
        request.app['file_distribution_directory'],
        filename
    )
    
    nodes = request.app['nodes']

    try:
        file = await read_file(request_file)
        return Response(text=f'{file}')
    except FileNotFoundError:
        if not nodes:
            return Response(status=404)
        tasks = await prepare_nodes(filename, nodes)
        for task in tasks:
            finished_task = await task
            if request.app['save_file']:
                await write_file(request_file, finished_task)
    return Response(text=f'OK')