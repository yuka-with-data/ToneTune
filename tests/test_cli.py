"""Tests for ToneTune's command-line interface."""

from unittest.mock import patch
from tonetune.cli import get_user_input, get_choice, run_tonetune

def test_get_user_input_rejects_empty_input():
    """Verify that empty input is rejected until non-empty text is entered."""
    with patch("builtins.input", side_effect=["", "   ", "Invite my teammate."]):
        result = get_user_input()

    assert result == "Invite my teammate."


def test_get_choice_returns_valid_selection():
    """Verify that a valid menu number returns the corresponding choice."""
    choices = ["Email", "Work message", "Text / short message"]

    with patch("builtins.input", return_value="2"):
        result = get_choice("Choose a type:", choices)

    assert result == "Work message"


def test_get_choice_rejects_invalid_selections():
    """Verify that invalid menu entries are rejected."""
    choices = ["Natural", "Friendly", "Professional"]

    with patch("builtins.input", side_effect=["abc", "0", "4", "2"]):
        result = get_choice("Choose a tone:", choices)

    assert result == "Friendly"


def test_run_tonetune_displays_generated_draft():
    """Verify that the CLI displays the draft returned by generate_draft."""
    with (
        patch("builtins.input", side_effect=["Invite my teammate.", "3", "2"]),
        patch(
            "tonetune.cli.generate_draft",
            return_value="Hey! Join us for the party."
            ) as mock_generate,
        patch("builtins.print") as mock_print,
    ):
        run_tonetune()

    mock_generate.assert_called_once_with(
        user_input="Invite my teammate.",
        communication_type="Text / short message",
        tone="Friendly",
    )
    printed_text = " ".join(
        str(call) for call in mock_print.call_args_list
    )
    assert "Hey! Join us for the party." in printed_text


def test_run_tonetune_handles_generation_error():
    """Verify that the CLI displays a message when draft generation fails."""
    with (
        patch("builtins.input", side_effect=["Write a message.", "1", "1"]),
        patch(
            "tonetune.cli.generate_draft",
            side_effect=RuntimeError("Ollama is not running."),
        ),
        patch("builtins.print") as mock_print,
    ):
        run_tonetune()

    printed_text = " ".join(
        str(call) for call in mock_print.call_args_list
    )
    assert "Unable to generate your draft" in printed_text
    assert "Ollama is not running." in printed_text
