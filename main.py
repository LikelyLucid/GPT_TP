import TouchPortalAPI as TP
import openai

gpt3_limited_list = ["text-curie-001", "text-babbage-001", "text-ada-001"]
gpt_chat_list = ["gpt-3.5-turbo"]
TPClient = TP.Client("LIKELYLUCID_GPT_TP")


@TPClient.on(TP.TYPES.onConnect)
def onStart(data):
    print("Connected!", data)
    openai.api_key = data["settings"][0]["OpenAI API Key"]
    print(openai.api_key)


@TPClient.on(TP.TYPES.onAction)
def onAction(data):
    print(data)
    if data["actionId"] == "gpt_generate":
        # get the value from the action data
        Instruction = TPClient.getActionDataValue(data.get("data"), "GPT_Instruct")
        print(Instruction)
        data_entry = TPClient.getActionDataValue(data.get("data"), "GPT_Data")
        print(data_entry)
        model = TPClient.getActionDataValue(data.get("data"), "GPT_MODEL")
        print(model)
        temperature = float(TPClient.getActionDataValue(data.get("data"), "GPT_Temperature"))
        print(temperature)
        max_tokens = int(
            float(TPClient.getActionDataValue(data.get("data"), "GPT_MaxTokens"))
        )
        print(max_tokens)
        if model in gpt3_limited_list and max_tokens > 2049:
            max_tokens = 2049
        # TPClient.stateUpdate("gpt_output", f"{Instruction} {data_entry} {model} {temperature} {max_tokens}")
        if model in gpt_chat_list:
            openai.ChatCompletion.create(
                model = model,
                messages = ["role": "user", "content": f"{Instruction} {data_entry}"],
            )
        else:
            response = openai.Completion.create(
                model = model,
                prompt = f"{Instruction} {data_entry}",
                temperature = temperature,
                max_tokens = max_tokens,
            )
        TPClient.stateUpdate("gpt_output", response)

# Shutdown handler, called when Touch Portal wants to stop your plugin.
@TPClient.on(TP.TYPES.onShutdown)  # or 'closePlugin'
def onShutdown(data):
    print("Got Shutdown Message! Shutting Down the Plugin!")
    TPClient.disconnect()


TPClient.connect()
