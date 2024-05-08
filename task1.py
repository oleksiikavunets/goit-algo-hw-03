import shutil
from argparse import ArgumentParser
from pathlib import Path

parser = ArgumentParser()

parser.add_argument('-s', '--src', type=Path)
parser.add_argument('-d', '--dst', type=Path, default='dist', required=False)
args = parser.parse_args()


def cp(cp_from, cp_to):
    try:
        shutil.copy2(cp_from, cp_to)
    except PermissionError:
        cp_from.chmod(444)
        shutil.copy2(cp_from, cp_to)


def cp_files(cp_from: Path, cp_to: Path) -> None:
    for child in cp_from.iterdir():
        if child.is_dir():
            cp_files(child, cp_to)

        else:
            suffix = child.suffix
            dst = cp_to / suffix
            dst.mkdir(exist_ok=True)
            cp(child, dst)


if __name__ == "__main__":
    source = args.src
    destination = args.dst

    destination.mkdir(exist_ok=True)

    cp_files(source, destination)
