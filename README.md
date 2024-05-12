<div align="center">

# python-poetry

Docker images with python and poetry

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/shini4i/docker-python-poetry/update_readme.yml?branch=main&style=plastic)
![Supported Python Versions](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue?style=plastic)
![GitHub](https://img.shields.io/github/license/shini4i/python-poetry?style=plastic)

</div>

## Project Description

This project aims to provide pre-built docker images with python and poetry.

The naming convention is as follows:
```
ghcr.io/shini4i/python-poetry:<python_version>-<poetry_version>
```
Python version is the version without a patch number, e.g., `3.12`, and the poetry version is the version with a patch number, e.g., `1.8.2`.

> Additionally, if there is a necessity to use a specific python version, it is possible to use a tag with the patch number, e.g., `3.12.3-1.8.2`.

## Supported versions

Currently, the following python versions are supported: `3.10` `3.11` `3.12`

### Available images
<!-- table_start -->
| Python Version |              Latest built image             |        Updated time       |
|:--------------:|:-------------------------------------------:|:-------------------------:|
|      3.12      |  ghcr.io/shini4i/python-poetry:3.12.3-1.8.3 | 2024-05-12 16:48:21 +0000 |
|      3.11      |  ghcr.io/shini4i/python-poetry:3.11.4-1.8.3 | 2024-05-12 16:48:21 +0000 |
|      3.10      | ghcr.io/shini4i/python-poetry:3.10.12-1.8.3 | 2024-05-12 16:48:21 +0000 |
<!-- table_end -->
