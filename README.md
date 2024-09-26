# IsoPro Examples 

This repository contains example Jupyter notebooks demonstrating the usage of the `isopro` package, a Python library for Intelligent Simulation Orchestration of Large Language Models.

## Overview

The `isopro` package provides tools for various AI-related tasks, including:

- Adversarial testing of language models
- Conversation simulation with different user personas
- Reinforcement learning with LLM integration
- AI orchestration for complex tasks

These example notebooks showcase the capabilities of `isopro` and provide practical demonstrations of its features.

## Prerequisites

Before running these examples, make sure you have the following installed:

- Python 3.7+
- Jupyter Notebook or JupyterLab
- isopro package (`pip install isopro`)

You'll also need API keys for OpenAI and Anthropic services. Set these as environment variables or use a `.env` file.

## Examples

### 1. Adversarial Simulation (`adversarial_example.ipynb`)

This notebook demonstrates how to run adversarial simulations against a language model (Claude) and analyze the results.

Key features:
- Setting up an adversarial environment
- Running simulations with different attack types
- Analyzing and visualizing the impact of adversarial attacks

### 2. Conversation Simulation (`conversation_simulation_example.ipynb`)

This example shows how to simulate conversations between an AI assistant and various user personas.

Key features:
- Initializing a conversation simulator
- Running simulations with predefined personas
- Creating and using custom personas
- Analyzing conversation results

### 3. Reinforcement Learning with CartPole (`run_cartpole_example.ipynb`)

This notebook illustrates how to integrate Large Language Models with reinforcement learning using the CartPole environment.

Key features:
- Creating an LLM-based wrapper for the CartPole environment
- Training a reinforcement learning agent
- Testing the trained agent and collecting performance metrics

### 4. AI Orchestration (`orchestrator_example.ipynb`)

This example demonstrates how to orchestrate multiple AI agents to work together on complex tasks.

Key features:
- Setting up an orchestration environment
- Adding different types of AI agents
- Running simulations in various execution modes
- Evaluating and comparing results from different modes

## Usage

To run these examples:

1. Clone this repository:
   ```
   git clone https://github.com/your-username/isopro_examples.git
   cd isopro_examples
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your API keys as environment variables or in a `.env` file.

4. Launch Jupyter Notebook or JupyterLab:
   ```
   jupyter notebook
   ```

5. Open and run the desired notebook.

## Contributing

We welcome contributions to improve these examples or add new ones! Please feel free to submit pull requests or open issues for any bugs or suggestions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any problems or have questions about these examples, please drop a comment in our isopro beta community chat on discord. 

If you do not have access to this community and would like to join, head over to our [sign up page](https://docs.google.com/forms/d/e/1FAIpQLSdgbBJWwI-MiyeZ0EL0CxmOZ_yFKBr8P-Ac_7x99cw5ViiC0g/viewform) to get added today. 
