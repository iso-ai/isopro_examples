# Adversarial Simulation API Reference

## AdversarialSimulator

The main class for running adversarial simulations is 
```python
class AdversarialSimulator(environment: AdversarialEnvironment)
```

### Methods

- `run_simulation(input_data: List[str], num_steps: int) -> List[Dict]`
Runs the adversarial simulation.

- `class AdversarialEnvironment(agent_wrapper: AI_Agent, num_adversarial_agents: int, attack_types: List[str], attack_targets: List[str])`
Represents the environment for adversarial simulations.
Methods

- `step(state: Dict) -> Dict`
Performs one step in the adversarial environment.

