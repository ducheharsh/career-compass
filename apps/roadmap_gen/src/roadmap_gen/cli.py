import click
from roadmap_gen.api import run_api

@click.group()
def cli():
    """RoadmapGen CLI tool."""
    pass

@cli.command()
@click.option('--port', default=5000, help='Port to run the API server on')
@click.option('--debug', is_flag=True, help='Run in debug mode')
def api(port, debug):
    """Run the RoadmapGen API server."""
    import os
    os.environ['PORT'] = str(port)
    os.environ['FLASK_DEBUG'] = str(debug).lower()
    run_api()

if __name__ == '__main__':
    cli() 