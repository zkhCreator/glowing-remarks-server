from openai import Client as client

class ChatService():

    def createThread():
        assistant = client.beta.assistants.create(
            name="Math Tutor",
            instructions="You are a personal math tutor. Write and run code to answer math questions.",
            tools=[{"type": "code_interpreter"}],
            model="gpt-4-1106-preview"
        )
        
        thread = client.beta.threads.create()
        
        

        