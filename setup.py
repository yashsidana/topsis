from setuptools import setup, find_packages

setup(
    name="Topsis-Yash-102303973",
    version="1.0.0",
    author="Yash",
    author_email="your-email@gmail.com",
    description="A Python package for TOPSIS implementation",
    packages=find_packages(),
    install_requires=["pandas", "numpy"],
    entry_points={
        "console_scripts": [
            "topsis=topsis.topsis:main"
        ]
    },
)
