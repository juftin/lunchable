"""
Test cases for the __main__ module.
"""

import pytest
from click.testing import CliRunner


@pytest.fixture
def runner() -> CliRunner:
    """
    Fixture for invoking command-line interfaces.
    """
    return CliRunner()


@pytest.mark.filterwarnings("ignore:datetime.datetime.utcfromtimestamp")
def test_main_succeeds(runner: CliRunner) -> None:
    """
    It exits with a status code of zero.
    """
    from lunchable._cli import cli

    result = runner.invoke(cli)
    assert result.exit_code == 0


def test_registered_plugins(runner: CliRunner) -> None:
    """
    Assert that all registered plugins are available.
    """
    from lunchable._cli import cli

    builtin_plugins = ["primelunch", "splitlunch", "pushlunch"]

    for plugin in builtin_plugins:
        result = runner.invoke(cli, ["plugins", plugin, "--help"])
        assert result.exit_code == 0
