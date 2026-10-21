"""
Manual integration test for ToneTune's draft-generation pipeline.

Uses the actual local Ollama model to generate a draft from sample user input.
Unlike the automated unit tests, this script verifies that prompt construction,
model communication, and draft generation work together in a real environment.
"""

from tonetune.generator import generate_draft

draft = generate_draft(
    user_input="Ask my teammate for a project update.",
    communication_type="work message",
    tone="friendly",
)

print("\nGenerated draft:\n")
print(draft)
