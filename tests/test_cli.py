"""Tests for `world_path_viz`.cli module."""
# import os
from typing import List

import pytest
from click.testing import CliRunner

import world_path_viz
from world_path_viz import cli


@pytest.mark.parametrize(
    "options,expected",
    [
        (["--help"], "Usage: main [OPTIONS]"),
        (["--version"], f"main, version { world_path_viz.__version__ }\n"),
        (
            [
                "40.7128,-74.0060",
                "37.7749,-122.4194",
                "--algo",
                "dijkstra",
                "--output",
                "test.gif",
            ],
            (
                "Processing... request for 40.7128,-74.0060 to 37.7749,-122.4194 "
                "using dijkstra algorithm\n"
            ),
        ),
    ],
)
def test_command_line_interface(options: List[str], expected: str) -> None:
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(
        cli.main,
        options,
    )
    assert result.exit_code == 0
    assert expected in result.output
    # assert os.path.exists("test.gif")
    # os.remove("test.gif")
