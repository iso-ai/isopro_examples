"""
ISOPRO Examples

This package contains example Jupyter notebooks demonstrating various features and use cases of the ISOPRO package.

Available examples:
- custom_environment_example: Demonstrates how to create custom environments using Claude or Hugging Face models.
- conversation_simulation_example: Shows how to use the conversation simulation with a Claude agent for customer service.
- adversarial_simulation_example: Illustrates how to use the adversarial simulation and analyze its results.

To run these examples, open the respective .ipynb files in a Jupyter notebook environment.
"""

# Import any shared utilities or constants used across notebooks here
# For example:
# from .utils import plot_results, load_sample_data

# List available example notebooks
AVAILABLE_EXAMPLES = [
    "custom_environment_example",
    "conversation_simulation_example",
    "adversarial_simulation_example"
]

def list_examples():
    """
    Print a list of available example notebooks.
    """
    print("Available ISOPRO example notebooks:")
    for example in AVAILABLE_EXAMPLES:
        print(f"- {example}")
    print("\nTo run an example, open the corresponding .ipynb file in a Jupyter notebook environment.")

# You can add any other shared functions or variables here that might be useful across multiple notebooks