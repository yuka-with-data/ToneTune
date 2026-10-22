"""
ToneTune draft generation.

Sends constructed prompts to a local Ollama model and returns
the generated communication draft.
"""

import ollama
from ollama import ResponseError
from tonetune.prompts import build_prompts

def generate_draft(
        user_input: str,
        communication_type: str = "general_message",
        tone: str = "natural",
        model: str = "gemma4:e4b",
) -> str:
    """ Generate and return a communication draft using a local Ollama. """

    # Build the system and draft prompts from the user's input and preferences.
    system_prompt, draft_prompt = build_prompts(
        user_input=user_input,
        communication_type=communication_type,
        tone=tone,
    )
    try:
        # Send both prompts to the local Ollama model.
        response = ollama.chat(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": draft_prompt},
            ],
        )

        # Return the generated draft without surrounding whitespace.
        return response.message.content.strip()

    except ResponseError as error:
        # Handle model-related errors
        raise RuntimeError(f"Ollama model error: {error.error}") from error

    except Exception as error:
        # Handle unexpected errors
        raise RuntimeError(
            f"Failed to generate draft. Is Ollama running? Details: {error}"
        ) from error
