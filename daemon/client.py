from aiohttp import ClientSession
from aiohttp.web import Response


async def fetch(node_url:str, filename:str) -> str:
    async with ClientSession() as session:
        url = ''.join([node_url, filename])
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            else:
                print(response)
    return Response(text='COK')