import os
import click

from .application import generate_application
from .example import generate_example
from .board import generate_board
from .driver import generate_driver
from .pkg import generate_pkg
from .test import generate_test
from . import __version__


@click.group()
@click.version_option(version=__version__)
def riotgen():
    pass


@riotgen.command(help="Bootstrap a RIOT application")
@click.option("-d", "--output_dir", type=click.Path(exists=True), default=os.getcwd())
@click.option("-i", "--interactive", is_flag=True, help="Use interactive mode")
@click.option(
    "-c",
    "--config",
    type=click.File(mode="r"),
    help="Configuration file for application",
)
@click.option(
    "-r", "--riotbase", type=click.Path(exists=True), default=os.getenv("RIOTBASE")
)
def application(output_dir, interactive, config, riotbase):
    generate_application(output_dir, interactive, config, riotbase)


@riotgen.command(help="Bootstrap a RIOT board support")
@click.option("-i", "--interactive", is_flag=True, help="Use interactive mode")
@click.option(
    "-c", "--config", type=click.File(mode="r"), help="Configuration file for board"
)
@click.option(
    "-r", "--riotbase", type=click.Path(exists=True), default=os.getenv("RIOTBASE")
)
def board(interactive, config, riotbase):
    generate_board(interactive, config, riotbase)


@riotgen.command(help="Bootstrap a RIOT driver module")
@click.option("-i", "--interactive", is_flag=True, help="Use interactive mode")
@click.option(
    "-c",
    "--config",
    type=click.File(mode="r"),
    help="Configuration file for the driver module",
)
@click.option(
    "-r", "--riotbase", type=click.Path(exists=True), default=os.getenv("RIOTBASE")
)
def driver(interactive, config, riotbase):
    generate_driver(interactive, config, riotbase)


@riotgen.command(help="Bootstrap a RIOT example application")
@click.option("-i", "--interactive", is_flag=True, help="Use interactive mode")
@click.option(
    "-c",
    "--config",
    type=click.File(mode="r"),
    help="Configuration file for example application",
)
@click.option(
    "-r", "--riotbase", type=click.Path(exists=True), default=os.getenv("RIOTBASE")
)
def example(interactive, config, riotbase):
    generate_example(interactive, config, riotbase)


@riotgen.command(help="Bootstrap a RIOT external package")
@click.option("-i", "--interactive", is_flag=True, help="Use interactive mode")
@click.option(
    "-c", "--config", type=click.File(mode="r"), help="Configuration file for package"
)
@click.option(
    "-r", "--riotbase", type=click.Path(exists=True), default=os.getenv("RIOTBASE")
)
def pkg(interactive, config, riotbase):
    generate_pkg(interactive, config, riotbase)


@riotgen.command(help="Bootstrap a RIOT test application")
@click.option("-i", "--interactive", is_flag=True, help="Use interactive mode")
@click.option(
    "-c",
    "--config",
    type=click.File(mode="r"),
    help="Configuration file for test application",
)
@click.option(
    "-r", "--riotbase", type=click.Path(exists=True), default=os.getenv("RIOTBASE")
)
def test(interactive, config, riotbase):
    generate_test(interactive, config, riotbase)
