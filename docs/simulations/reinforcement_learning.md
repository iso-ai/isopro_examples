
# Reinforcement Learning

The Reinforcement Learning module in isopro integrates Large Language Models with reinforcement learning environments.

## Basic Usage

Here's a simple example of how to use the Reinforcement Learning module:

```python
from isopro.rl.rl_environment import LLMRLEnvironment
from stable_baselines3 import PPO

class YourEnvironment(LLMRLEnvironment):
    def step(self, action):
        # Your environment logic here
        pass

env = YourEnvironment("You are an AI trained to solve this task.")
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=100)
```