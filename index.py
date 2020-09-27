# Import pyfiglet module
import pyfiglet

# Import Click for creating beautiful command line interfaces. You may
# choose to check https://click.palletsprojects.com/en/7.x/ for more details
import click

# Import data scrambler
from scrambler import DataScrambler

# Show introductory text
intro_text = pyfiglet.figlet_format('Text Obfuscator')
print(intro_text)


@click.command()
@click.option('--depth', default='shallow', help='Run obfuscation using deep or shallow rules. Default is shallow.')
@click.option('--text', prompt='Enter the text you want to obfuscate', help='The text to obfuscate')
@click.option('--rule', default='EN', help='The language pack to use. Default is "EN" i.e. English')
@click.option('--verbose', default=0, help='See details of obfuscation')
def main(text: str, depth: str, rule: str, verbose):
    if depth == 'deep':
        message = "Using deep obfuscation. Operation may be slower.."
    elif depth == 'shallow':
        message = "Using shallow obfuscation.."
    else:
        raise Exception("Sorry. Only 'shallow' or 'deep' allowed as obfuscation depth.")

    # Show obfuscation details as defined by user
    if verbose:
        click.echo(message)
        click.echo("Using rules defined in {pack} Language Pack..".format(pack=rule))

    scramble = DataScrambler()
    scramble.depth = depth
    result = scramble.obfuscate(text)
    click.echo(result)


if __name__ == '__main__':
    main()
