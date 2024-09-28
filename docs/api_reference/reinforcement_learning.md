# Reinforcement Learning API Reference

## LLMRLEnvironment
The Base class for creating reinforcement learning environments with LLM integration is: 

```python
class LLMRLEnvironment(agent_prompt: str, env_prompt: Optional[str] = None)
```

## Methods

- `step(action: Any) -> Tuple[Any, float, bool, bool, Dict]`
Performs one step in the environment.

- `reset() -> Tuple[Any, Dict]`
Resets the environment to its initial state.