from setuptools import setup, find_packages

__version__ = None
with open("appsflyer/__init__.py") as f:
    exec(f.read())  # nosec

with open("README.md") as f:
    long_description = f.read()

setup(
    name="appsflyer",
    version=__version__,
    description="AppsFlyer S2S events API client",
    author="Frederico Jordan",
    author_email="fredericojordan@gmail.com",
    url="https://github.com/fredericojordan/appsflyer-python/",
    keywords=["appsflyer"],
    install_requires=["requests >= 2.0.0"],
    extras_require={},
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
