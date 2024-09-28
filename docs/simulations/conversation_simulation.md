# Conversation Simulation

The Conversation Simulation module allows you to simulate conversations between an AI assistant and various user personas.

## Basic Usage

Here's a simple example of how to use the Conversation Simulation module:

```python
from isopro.conversation_simulation.conversation_simulator import ConversationSimulator

simulator = ConversationSimulator(
    ai_prompt="You are an AI assistant. Be helpful and concise."
)

# Run a simulation with a predefined persona
conversation = simulator.run_simulation("upset", num_turns=3)

# Run a simulation with a custom persona
custom_conversation = simulator.run_custom_simulation(
    "Tech Expert",
    ["knowledgeable", "impatient"],
    ["What's the latest in quantum computing?", "Explain neural networks briefly."],
    num_turns=3
)
```