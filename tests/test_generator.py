"""Tests for ToneTune draft generation."""

from unittest.mock import Mock, patch
import pytest
from ollama import ResponseError
from tonetune.generator import generate_draft


def test_generate_draft_success():
    """Verify that generate_draft returns the model's generated text."""
    mock_response = Mock()
    mock_response.message.content = "Hi, could you share a project update?"

    with patch("tonetune.generator.build_prompts") as mock_prompts:
        mock_prompts.return_value = ("System instructions", "Draft request")

        with patch("tonetune.generator.ollama.chat", return_value=mock_response):
            result = generate_draft("Ask for a project update.")

    assert result == "Hi, could you share a project update?"


def test_generate_draft_handles_model_error():
    """Verify that Ollama model errors are raised as RuntimeError."""
    with patch("tonetune.generator.build_prompts", return_value=("System", "User")):
        with patch(
            "tonetune.generator.ollama.chat",
            side_effect=ResponseError("Model not found", status_code=404),
        ):
            with pytest.raises(RuntimeError, match="Ollama model error"):
                generate_draft("Write a message.")


def test_generate_draft_handles_unexpected_error():
    """Verify that unexpected Ollama failures are raised as RuntimeError."""
    with patch("tonetune.generator.build_prompts", return_value=("System", "User")):
        with patch(
            "tonetune.generator.ollama.chat",
            side_effect=ConnectionError("Connection refused"),
        ):
            with pytest.raises(RuntimeError, match="Failed to generate draft"):
                generate_draft("Write a message.")
