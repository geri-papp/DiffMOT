import setuptools
from pathlib import Path


def get_package_dir():
    pkg_dir = {
        "diffmot.dataset": "dataset",
        "diffmot.models": "models",
        "diffmot.tracker": "tracker",
        "diffmot.tracking_utils": "tracking_utils",
    }
    return pkg_dir


def get_install_requirements(path: Path):
    reqs = {}

    with open(path, "r", encoding="utf-8") as f:
        lines = [x.strip() for x in f.read().splitlines()]

    for req in [x for x in lines if not x.startswith("#")]:
        name = req
        for delim in ["==", ">=", "<="]:
            if delim in req:
                name, _ = req.split(delim)
                break

        reqs[name] = req

    return reqs


def get_long_description():
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
    return long_description


setuptools.setup(
    name="diffmot",
    version="0.1",
    package_dir=get_package_dir(),
    packages=setuptools.find_packages(),
    python_requires=">=3.9",
    install_requires=list(get_install_requirements(Path(__file__).parent / "requirements.txt").values()),
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
)
