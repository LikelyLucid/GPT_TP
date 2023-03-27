import asyncio
from pygpt import PyGPT

async def main():
    chat_gpt = PyGPT('eyJhbGciOiJkaXIiLCJlbmMiOiJBMR0NN....')
    await chat_gpt.connect()
    await chat_gpt.wait_for_ready()
    answer = await chat_gpt.ask('What is the capital of France?')
    print(answer)
    await chat_gpt.disconnect()

if __name__ == '__main__':
    asyncio.run(main())