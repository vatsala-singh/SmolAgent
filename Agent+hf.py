from smolagents import CodeAgent, InferenceClientModel, tool, GradioUI
from huggingface_hub import InferenceClient

client = InferenceClient()

@tool
def generate_image(prompt: str) -> str:
    """
    Generate an image from a text prompt.

    Args:
        prompt: The text description of the image to generate.

    Returns:
        Path to the generated image file.
    """

    image = client.text_to_image(
        prompt,
        model="stabilityai/stable-diffusion-xl-base-1.0"
    )

    path = "generated.png"
    image.save(path)

    return path


model = InferenceClientModel(
    model_id="meta-llama/Meta-Llama-3-8B-Instruct"
)

agent = CodeAgent(
    tools=[generate_image],
    model=model
)

GradioUI(agent).launch()