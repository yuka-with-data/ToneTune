""" Tests for the prompts module."""

from tonetune.prompts import build_prompts, load_template

def test_load_system_template():
    """ Verify that the system prompt template loads successfully. """
    template = load_template("system.txt")

    assert isinstance(template, str)
    assert template.strip()

def test_load_draft_template():
    """ Verify that the draft prompt template loads successfully. """
    template = load_template("draft.txt")

    assert isinstance(template, str)
    assert "{communication_type}" in template
    assert "{tone}" in template
    assert "{user_input}" in template

def test_build_prompts_replaces_placeholders():
    """ Verify that user input and preferences replace template placeholders. """
    user_input = "Ask my teammate for a project update."

    system_prompt, draft_prompt = build_prompts(
        user_input=user_input,
        communication_type="work message",
        tone="friendly"
    )

    assert system_prompt.strip()
    assert "work message" in draft_prompt
    assert "friendly" in draft_prompt
    assert user_input in draft_prompt

    assert "{communication_type}" not in draft_prompt
    assert "{tone}" not in draft_prompt
    assert "{user_input}" not in draft_prompt
