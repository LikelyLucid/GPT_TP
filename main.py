import TouchPortalAPI as TP
import openai
gpt3_limited_list = ["text-curie-001", "text-babbage-001", "text-ada-001"]

TPClient = TP.Client("LIKELYLUCID_GPT_TP")


@TPClient.on(TP.TYPES.onConnect)
def onStart(data):
    print("Connected!", data)
    data = {'settings': [{'OpenAI API Key': 'poopybum'}, {'Made by': 'LikelyLucid'}], 'tpVersionString': '3.1.11.0.0', 'pluginVersion': 100, 'tpVersionCode': 301011, 'sdkVersion': 6, 'type': 'info', 'status': 'paired'}
    openai.api_key = data['settings'][0]['OpenAI API Key']


@TPClient.on(TP.TYPES.onAction)
def onAction(data):
    print(data)
    if data['actionId'] == "gpt_generate":
        # get the value from the action data
        Instruction = TPClient.getActionDataValue(data.get('data'), 'GPT_Instruct')
        print(Instruction)
        data_entry = TPClient.getActionDataValue(data.get('data'), 'GPT_Data')
        print(data_entry)
        model = TPClient.getActionDataValue(data.get('data'), 'GPT_MODEL')
        print(model)
        temperature = TPClient.getActionDataValue(data.get('data'), 'GPT_Temperature')
        print(temperature)
        max_tokens = int(float(TPClient.getActionDataValue(data.get('data'), 'GPT_MaxTokens')))
        print(max_tokens)
        if model in gpt3_limited_list and max_tokens > 2049:
            max_tokens = 2049

# Shutdown handler, called when Touch Portal wants to stop your plugin.
@TPClient.on(TP.TYPES.onShutdown) # or 'closePlugin'
def onShutdown(data):
    print("Got Shutdown Message! Shutting Down the Plugin!")
    TPClient.disconnect()


TPClient.connect()