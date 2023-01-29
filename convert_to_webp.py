from pathlib import Path
from PIL import Image
import os.path
from termcolor import colored

total_saved_size = 0

def sizeof_fmt(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"

def convert_to_webp_if_need(source):
    global total_saved_size
    destination = source.with_suffix(".webp")

    if not os.path.isfile(destination):
        image = Image.open(source)
        size_before = os.path.getsize(source)
        image.save(destination, format="webp", method=6, lossless=True)
        size_after = os.path.getsize(destination)
        diff = size_before - size_after
        color = "green" if diff > 0 else "red"
        print("Convert to WEBP: " + str(destination) + " " + colored(sizeof_fmt(diff), color))
        total_saved_size = total_saved_size + diff
    return destination


def main():
    global total_saved_size
    paths = Path(".").glob("**/*.png")
    for path in paths:
        convert_to_webp_if_need(path)
    # paths = Path(".").glob("**/*.jpg")
    # for path in paths:
    #     convert_to_webp_if_need(path)
    color = "green" if total_saved_size > 0 else "red"
    print(colored("Total saved size is "+sizeof_fmt(total_saved_size), color))

main()
