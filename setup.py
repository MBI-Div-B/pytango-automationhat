from setuptools import setup, find_packages

setup(
    name="tangods_automationhat",
    version="0.0.1",
    description="tango device to control raspberry automationhat from pimoroni",
    author="Daniel Schick",
    author_email="schick@mbi-berlin.de",
    python_requires=">=3.6",
    entry_points={"console_scripts": ["AutomationHAT = tangods_automationhat:main"]},
    license="MIT",
    packages=["tangods_automationhat"],
    install_requires=[
        "pytango",
        "automationhat",
    ],
    url="https://github.com/MBI-DIiv-B/pytango-automationhat",
    keywords=[
        "tango device",
        "tango",
        "pytango",
        "automation hat",
    ],
)
