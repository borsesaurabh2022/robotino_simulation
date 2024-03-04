import os
from glob import glob

from setuptools import find_packages
from setuptools import setup

package_name = "robotino3_navigation"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (os.path.join("share", package_name, "launch"), glob("launch/*.launch.py")),
        (os.path.join("share", package_name, "config"), glob("config/*")),
        (os.path.join("share", package_name, "rviz"), glob("rviz/*")),
        (os.path.join("share", package_name, "map"), glob("map/*")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="srb-jarvis",
    maintainer_email="saurabh.borse@alumni.fh-aachen.de",
    description="TODO: Package description",
    license="TODO: License declaration",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "robotinobase_initial_pose = robotino3_navigation.robotinobase_initial_pose:main",
        ],
    },
)
