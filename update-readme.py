#!/usr/bin/env python

import os
import subprocess

import semver
from prettytable import MARKDOWN
from prettytable import PrettyTable

repo = "ghcr.io/shini4i/python-poetry"


class Readme:
    def __init__(self):
        self.readme_path = "README.md"
        self.readme_content = self._read_readme()

        self.table_start_marker = "<!-- table_start -->"
        self.table_end_marker = "<!-- table_end -->"

    def _read_readme(self) -> str:
        with open(self.readme_path, "r") as readme_file:
            return readme_file.read()

    @staticmethod
    def _generate_table(versions: dict) -> PrettyTable:
        headers = ["Python Version", "Latest built image", "Updated time"]
        rows = []

        for k, v in versions.items():
            rows.append([k, v.get("version"), v.get("timestamp")])

        table = PrettyTable(headers)
        table.set_style(MARKDOWN)
        table.add_rows(rows)

        return table

    def _replace_table(self, table: PrettyTable):
        print("Generating new table...")

        table_start = (
            self.readme_content.find(self.table_start_marker)
            + len(self.table_start_marker)
            + 1
        )
        table_end = self.readme_content.find(self.table_end_marker)

        if table_start == len(self.table_start_marker):
            raise IndexError("Table start marker not found")

        self.readme_content = (
            f"{self.readme_content[:table_start]}"
            f"{table.get_string()}\n"
            f"{self.readme_content[table_end:]}"
        )

    def update_readme(self, versions: dict):
        table = self._generate_table(versions)

        self._replace_table(table)

        print("Writing new readme...")
        with open(self.readme_path, "w") as readme_file:
            readme_file.write(self.readme_content)


def process_dockerfiles():
    dockerfiles = []

    for root, dirs, files in os.walk("."):
        for file in files:
            if file == "Dockerfile":
                dockerfiles.append(os.path.join(root, file))

    return dockerfiles


def get_dockerfile_details(dockerfile: str) -> tuple:
    mtime = subprocess.check_output(
        [
            "git",
            "--no-pager",
            "log",
            "-1",
            "--format=%ci",
            "--date=iso-strict",
            dockerfile,
        ]
    )
    with open(dockerfile) as f:
        for line in f:
            if line.startswith("FROM"):
                python_version = line.split(":")[1].strip().split("-")[0]
            if line.startswith("ENV POETRY_VERSION"):
                poetry_version = line.split("=")[1].strip()

    return python_version, poetry_version, mtime


def main():
    versions = {}
    dockerfiles = process_dockerfiles()

    for dockerfile in dockerfiles:
        python_version, poetry_version, timestamp = get_dockerfile_details(dockerfile)
        version = semver.VersionInfo.parse(python_version)
        versions[f"{version.major}.{version.minor}"] = {
            "version": f"{repo}:{python_version}-{poetry_version}",
            "timestamp": timestamp.strip().decode("utf-8"),
        }

    readme = Readme()
    readme.update_readme(versions)


if __name__ == "__main__":
    main()
