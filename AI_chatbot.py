import os
import openai
import sys

# Command Line arguments:
key=sys.argv[1]
name= sys.argv[2]

# Loading my API key from environment variable:
openai.api_key = os.getenv(key)

messages=[{"role": "system", "content": "You are a helpful assistant"}]

while True:
    message=input(f"{name.title()}: ")
    try:                
        if message == "bye":# Write done to exit from chatbot:
            print(f"Bye! Thank You, {name.title()}! See you next time!")          
            print("Token Used:", chatbot['usage']['total_tokens'])
            break
        else:
            # Chat message from user
            messages.append({"role": "user", "content": message})
            # Conversation messages 
            chatbot=openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)  
            # Reply message from AI      
            response=chatbot['choices'][0]['message']['content']
            messages.append({"role": "assistant", "content": response})
            print(f"AI: {response}")
    except EOFError:
        print(f"Bye! Thank You, {name.title()}! See you next time!")          
        print("Token Used:", chatbot['usage']['total_tokens'])
        break
