from smolagents import(
    load_tool,
    CodeAgent,
    InferenceClientModel,
    GradioUI
)

image_generation_tool = load_tool("m-ric/text-to-image", trust_remote_code=True)
model = InferenceClientModel("m-ric/text-to-image", trust_remote_code=True)
agent = CodeAgent(tools=[image_generation_tool], model=model)

GradioUI(agent).launch()