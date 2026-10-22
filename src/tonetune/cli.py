"""
ToneTune command-line interface.

Collects user input and writing preferences, generates a draft using the local Ollama MOdel,
and displays the result in the terminal.
 """

from tonetune.generator import generate_draft

# Define Communication types and tones.
COMMUNICATION_TYPES = [
    "Email",
    "Work message",
    "Text / short message",
    "Open-source discussion",
    "Issue / PR comment",
    "Personal note",
    "Social media post",
    "Feedback / review",
]

# Define the tone options available to users.
TONES = [
    "Natural",
    "Friendly",
    "Professional",
    "Casual",
    "Formal",
    "Concise",
    "Empathetic",
    "Persuasive",
]

""" Prompt user input and display choices. """
def get_user_input() -> str:
    """ Ask the user for their rough thoughts or keywords. """
    while True:
        user_input = input("\nWhat would you like to express?\n").strip()

        # Reject empty input and ask the user to try again.
        if user_input:
            return user_input
        print("Input cannot be empty. Please try again.")

def get_choice(prompt:str, choices: list[str]) -> str:
    """ Display options and validate the selected number. """
    print(f"\n{prompt}")

    # Display each choice with a number starting at 1
    for index, choice in enumerate(choices, start=1):
        print(f"{index}. {choice}")

    while True:
        selection = input("Enter your choice number: ").strip()

        # Accept only a number within the available choices.
        if selection.isdigit():
            choice_index = int(selection)

            if 1 <= choice_index <= len(choices):
                return choices[choice_index - 1]

        print(f"Please enter a number between 1 and {len(choices)}.")

# Generate a draft and display it to the user.
def run_tonetune() -> None:
    """ Collect preferences, generate a draft, and display the results. """

    user_input = get_user_input()
    communication_type = get_choice(
        "Choose a communication type:",
        COMMUNICATION_TYPES,
    )
    tone = get_choice("Choose a tone:", TONES)

    try:
        # Generate a draft using the selected preferences
        draft = generate_draft(
            user_input=user_input,
            communication_type=communication_type,
            tone=tone,
        )

        # Display the generated draft.
        print("\n--- YOUR DRAFT ---")
        print(draft)

    except RuntimeError as error:
        print(f"\nUnable to generate your draft: {error}")

# Run the CLI when this module is executed directly
if __name__ == "__main__":
    print("Welcome to ToneTune!")
    run_tonetune()
