# AI Orchestration

The AI Orchestration module allows you to coordinate multiple AI agents to work on complex tasks.

## Basic Usage

Here's a simple example of how to use the AI Orchestration module:

```python
from isopro.orchestration_simulation import OrchestrationEnv
from isopro.orchestration_simulation.components import YourCustomAgent

env = OrchestrationEnv()
env.add_component(YourCustomAgent("Researcher", "conduct research"))
env.add_component(YourCustomAgent("Writer", "write report"))

results = env.run_simulation(mode='parallel', input_data={'task': 'Create a report on AI trends'})
```