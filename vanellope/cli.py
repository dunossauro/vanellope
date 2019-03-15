"""General command lines."""
import click
from vanellope import rotate_blocks, chunks


@click.command()
@click.argument('input', type=click.File('rb'))
@click.argument('output', type=click.File('wb'))
@click.argument('seeds', type=int)
@click.argument('b_size', type=int, default=500)
def cli(input, output, seeds, b_size):
    """Command line interface to open and write file."""
    result = rotate_blocks(
        rotate_blocks(chunks(input.read(), b_size), seeds), seeds
    )

    output.writelines(result)


if __name__ == '__main__':
    cli()
