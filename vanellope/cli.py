"""General command lines."""
import click
from .vanellope import rotate_blocks, chunks


@click.command()
@click.option('input_file', '-i', type=click.File('rb'), help='File to glitch')
@click.option(
    'output_file', '-o', type=click.File('wb'), help='Result of glitch'
)
@click.option(
    'times', '-t', type=int, help='Times the operation will be applied'
)
@click.option(
    'block_size',
    '-size',
    '-bs',
    '-s',
    type=int,
    default=500,
    help='Size of the part of the file that will be glitched',
)
def cli(input_file, output_file, times, block_size):
    """Command line interface to open and write file."""
    blocks = chunks(input_file.read(), block_size)

    result = rotate_blocks(blocks, times)

    output_file.writelines(result)


if __name__ == '__main__':
    cli()
