"""Console script for real-world-path-viz."""
import click

from world_path_viz import __version__


@click.command()
@click.argument("src", help="Source location/coordinates", type=str)
@click.argument("dest", help="Destination location/coordinates", type=str)
@click.option("--algo", "-a", help="Algorithm to use", type=str, default="astar")
@click.option("--output", "-o", help="Output file", type=str, default="output.gif")
@click.version_option(__version__)
def main(src: str, dest: str, algo: str, output: str) -> int:
    """Console script for real-world-path-viz."""
    click.echo("Replace this message by putting your code into world_path_viz.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    main()  # pragma: no cover
