<div align="center">

# python-poetry

Docker images with python and poetry

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/shini4i/docker-python-poetry/update_readme.yml?branch=main&style=plastic)
![Supported Python Versions](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%203.12-blue?style=plastic)
![GitHub](https://img.shields.io/github/license/shini4i/python-poetry?style=plastic)

</div>

## Project Description

This project aims to provide pre-built docker images with python and poetry.

The naming convention is as follows:
```
ghcr.io/shini4i/python-poetry:<python_version>-<poetry_version>
```
Python version is the version without a patch number, e.g., `3.9`, and the poetry version is the version with a patch number, e.g., `1.2.1`.

> Additionally, if there is a necessity to use a specific python version, it is possible to use a tag with the patch number, e.g., `3.9.14-1.2.1`.

## Supported versions

Currently, the following python versions are supported: `3.8` `3.9` `3.10` `3.11` `3.12`

### Available images
<!-- table_start -->
| Python Version |              Latest built image             |        Updated time       |
|:--------------:|:-------------------------------------------:|:-------------------------:|
|      3.9       |  ghcr.io/shini4i/python-poetry:3.9.17-1.8.2 | 2024-03-07 18:29:16 +0000 |
|      3.11      |  ghcr.io/shini4i/python-poetry:3.11.4-1.8.2 | 2024-03-07 18:29:16 +0000 |
|      3.12      |  ghcr.io/shini4i/python-poetry:3.12.2-1.8.2 | 2024-04-12 16:27:28 +0300 |
|      3.8       |  ghcr.io/shini4i/python-poetry:3.8.17-1.8.2 | 2024-03-07 18:29:16 +0000 |
|      3.10      | ghcr.io/shini4i/python-poetry:3.10.12-1.8.2 | 2024-03-07 18:29:16 +0000 |
<!-- table_end -->
