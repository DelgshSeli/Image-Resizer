from PIL import Image, ImageFilter
import os
import click

def resize_image(input_path, output_path, size):
    with Image.open(input_path) as img:
        img_resized = img.resize((size, size), Image.LANCZOS)
        img_resized.save(output_path)

def create_output_folder(output_folder):
    os.makedirs(output_folder, exist_ok=True)

def get_script_directory():
    return os.path.dirname(os.path.abspath(__file__))

def get_default_output_folder():
    return os.path.join(get_script_directory(), "output")

@click.command()
@click.argument('input_logo', type=click.Path(exists=True))
@click.option('--output_folder', '-o', default=None, help='Output folder path')
@click.option('--sizes', '-s', default='16,32,48,128', help='Comma-separated list of sizes')
def main(input_logo, output_folder, sizes):
    """
    Resize images to specified sizes.

    INPUT_LOGO is the path to the input logo image.

    Example 1: python main.py -o "c:/Users/YourUserName/Downloads/"

    Example 2: python main.py "c:/Users/YourUserName/Downloads/example.jpg" -s 64,128,256 
    
    Example 3: python main.py "c:/Users/YourUserName/Downloads/example.jpg" -s 64,128,256  -o "c:/Users/YourUserName/Downloads/example.jpg"

    """
    sizes = [int(size) for size in sizes.split(',')]
    
    if output_folder is None:
        output_folder = get_default_output_folder()

    create_output_folder(output_folder)

    for size in sizes:
        output_path = os.path.join(output_folder, f"icon{size}.png")
        resize_image(input_logo, output_path, size)
        click.secho(f"Resized image saved to: {output_path}", fg='green')

if __name__ == "__main__":
    main()
