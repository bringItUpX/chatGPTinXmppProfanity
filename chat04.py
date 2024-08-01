from openai import OpenAI
import prof

# Load environment variables from .env file


# In this sample, we use key-based authentication. This is only done because this sample
# In real world, AVOID key-based
# authentication. ALWAYS prefer Microsoft Entra-based authentication (Managed Identity)!
client = OpenAI()  # todo: you have to provide the openai_api_key somehow. i.e. as environment variable

# System prompt
system_prompt = """
You are an assistant that helps users to find the right answer for the users question.
"""

# Initial assistant message to get the conversation started
assistant_message = "Hi! What question do you have?"
# choose the openAI ChatGPT model version
deploymentModel = "gpt-4o"

def prof_init(version, status, account_name, fulljid):
    prof.cons_show("Plugin chat04.py loaded successfully!")
    prof.log_error("Plugin chat04 loaded successfully!")
    return True


def prof_post_chat_message_display(barejid, resource, message):
    global assistant_message
    prof.log_error(barejid)
    if (message.startswith("chat") or message.startswith("Chat")):
        message = message[4:]
        prof.log_error("send to profanity: send_line ...")
        prof.send_line("/win " + barejid)
        if (len(message) < 2):
            assistant_message = "Hi! Welche Frage hast du?"
            prof.send_line("Antwort vom plugin: " + assistant_message + " (bitte sende eine Leertaste um den Verlauf zu löschen):")
        else:
            response = client.chat.completions.create(model=deploymentModel,
                                              messages=[
                                                  {"role": "system",
                                                      "content": system_prompt},
                                                  {"role": "assistant",
                                                      "content": assistant_message},
                                                  {"role": "user",
                                                      "content": message}
                                              ])
            if (len(response.choices) == 0):
                prof.send_line("Error: leider antwortet ChatGPT nicht auf die Frage.")
            else:
                # Add the response from the API to the list of messages to send to the API
                assistant_message = response.choices[0].message.content
                prof.send_line("Antwort vom plugin: " + assistant_message)
    else:
        prof.log_error("message fängt nicht mit chat an.")
    return
