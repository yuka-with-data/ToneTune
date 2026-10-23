# ToneTune

> Turn rough thoughts into clear, natural, ready-to-edit messages.

Have you ever struggled to find the right wards to express exactly what you are thinking?

`ToneTune` helps turn rough thoughts, imcomplete sentences, or keywords into clear, natural draft tailored to different communication types and tones.

Built with Python and Ollama, `ToneTune` is a lightweight, local-first communication drafting assistant that runs a language model on your own machine. You stay in control of the wording and decide what to do with the final draft.

## Features

- Turn rough thoughts into drafts: Start with keywords, fragments, or incomplete sentences.
- Choose communication types: Create emails, work messages, text messages, open-source discussions, issue or PR comments, personal notes, social media posts, and feedback or reviews.
- Adjust the tone: Choose a tone that fits your message and audience.
- Run locally: Use Ollama to generate drafts on your own machine.
- Stay in control: Review and edit the generated draft before using it.


## Quick Start

Once you have completed the installation steps and started Ollama with the required model, run `ToneTune` from the project root:

```bash
# Launch the ToneTune CLI
python -m tonetune.cli
```

Follow the prompts to enter your thoughts, choose a communication type and tone, and review your draft.

## Example

`ToneTune` can turn even a few rough keywords into a usable draft.

User input:

```bash
ask teammates update projects work
```

Communication type: Work message

Tone: Casual

Generated draft:

```bash
Hey team, do you all have a quick moment to update me on where we are with our current projects? Thanks!
```

You don't need to have the right words ready. Start with a few thoughts, choose your communication type and tone, and let `ToneTune` help shape them into a draft you can review and edit.

## Prerequisites

Before installing `ToneTune`, make sure you have:

- Python 3.12 or later
- Ollama installed and running
- the `gemma4:e4b` model downloaded through Ollama

To download the default model, run:

```bash
# Download the default language model.
ollama pull gemma4:e4b
```

`ToneTune` runs the model locally through Ollama, so you don't need an external API key.

The official Ollama documentation:

- [Ollama CLI Reference](https://docs.ollama.com/cli)
- [Ollama Model Library](https://ollama.com/library)

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd tone-tune
```

2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Activate the virtual environment.

On Windows PowerShell:

```bash
.\.venv\Scripts\Activate.ps1
```

4. Install `ToneTune`:

```bash
python -m pip install -e .
```

For development and testing, install the development depenencies instead:

```bash
python -m pip install -e ".[dev]"
```

## Usage

1. Make sure Ollama is running and the `gemma4:e4b` model is available locally.

2. From the project root, launch `ToneTune`:

```bash
python -m tonetune.cli
```

3. Follow the prompts to:

- Enter your thoughts, keywords, or rough fragments.
- Choose a communication type.
- Choose a tone.
- Review your generated draft.
