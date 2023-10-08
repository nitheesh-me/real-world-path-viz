"""Tests for `world_path_viz`.cli module."""
from typing import List

import pytest
from click.testing import CliRunner

import world_path_viz
from world_path_viz import cli


@pytest.mark.parametrize(
    "options,expected",
    [
        ([], "world_path_viz.cli.main"),
        (["--help"], "Usage: main [OPTIONS]"),
        (["--version"], f"main, version { world_path_viz.__version__ }\n"),
    ],
)
def test_command_line_interface(options: List[str], expected: str) -> None:
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, options)
    assert result.exit_code == 0
    assert expected in result.output
