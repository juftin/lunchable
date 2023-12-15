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
