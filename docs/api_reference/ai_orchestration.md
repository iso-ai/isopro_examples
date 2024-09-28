# AI Orchestration API Reference

## OrchestrationEnv

The main class for setting up and running AI orchestration simulations is: 

```python
class OrchestrationEnv()
```

## Methods

- `add_component(component: BaseComponent) -> None`
Adds a component (agent) to the orchestration environment.

- `run_simulation(mode: str, input_data: Dict) -> Dict`
Runs the orchestration simulation in the specified mode.