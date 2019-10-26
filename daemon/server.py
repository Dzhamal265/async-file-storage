from aiohttp.web import Application, run_app
from .handler import routes


def serve(daemon_config: 'Config') -> Application:
    app = Application()
    app['host'] = '127.0.0.1'
    app['port'] = daemon_config.get_port()
    app['file_distribution_directory'] = daemon_config.get_file_distribution_directory()
    app['save_file'] = daemon_config.get_save_file()
    app['nodes'] = daemon_config.get_nodes()
    
    app.add_routes(routes)

    run_app(app, host=app['host'], port=app['port'])