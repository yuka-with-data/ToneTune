"""
ToneTune prompt management module.

Loads system instructions and draft templates from packaged text files,
then assembles prompts using the user's input, communication type, and tone preferences.
Keeps prompt construction separate from model generation.

 """

from importlib.readers import files
from typing import Dict, List, Optional

def load_template(filename: str) -> str:
    """ Load and return a prompt template from the packaged template directory."""
    template_path = files("tonetune").joinpath("prompt_templates", filename)
    return template_path.read_text(encoding="utf-8")

def build_prompts(
        user_input: str,
        communication_type: str = "general_message",
        tone: str = "natural",
) -> tuple[str, str]:
    """ Build and return the system prompt and completed draft prompt. """

    # Load the system instructions and draft template.
    system_prompt = load_template("system.txt")
    draft_template = load_template("draft.txt")

    # Insert user input and preferences into the draft template.
    draft_prompt = draft_template.format(
        communication_type=communication_type,
        tone=tone,
        user_input=user_input
    )

    # Return prompts separately for the generator to use.
    return system_prompt, draft_prompt
