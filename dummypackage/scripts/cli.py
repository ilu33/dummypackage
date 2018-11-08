# Skeleton of a CLI

import click

import dummypackage


@click.command('dummypackage')
@click.argument('count', type=int, metavar='N')
def cli(count):
    """Echo a value `N` number of times"""
    for i in range(count):
        click.echo(dummypackage.has_legs)
