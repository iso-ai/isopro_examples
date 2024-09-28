# Conversation Simulation API Reference

## ConversationSimulator

The main class for running conversation simulations is:

```python
class ConversationSimulator(ai_prompt: str)
```


### Methods

- `run_simulation(persona: str, num_turns: int) -> List[Dict]`
Runs a simulation with a predefined persona.

- r`un_custom_simulation(name: str, characteristics: List[str], message_templates: List[str], num_turns: int) -> List[Dict]`
Runs a simulation with a custom persona.