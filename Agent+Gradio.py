from smolagents import(
    load_tool,
    CodeAgent,
    InferenceClientModel,
    GradioUI
)

model_id = "meta-llama/Meta-Llama-3-8B-Instruct"
image_generation_tool = load_tool(
    "huggingface-tools/text-to-image",
    trust_remote_code=True
)
model = InferenceClientModel(model_id = model_id)
agent = CodeAgent(tools=[image_generation_tool], model=model)

GradioUI(agent).launch()