"""Run a real draft-generation test using the local Ollama model."""

from tonetune.generator import generate_draft

draft = generate_draft(
    user_input="Ask my teammate for a project update.",
    communication_type="work message",
    tone="friendly",
)

print("\nGenerated draft:\n")
print(draft)
