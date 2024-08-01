# chatGPTinXmppProfanity

Python Plugin for the Terminal Xmpp Client Profanity.
If loaded in Profanity and Profanify is connected to a Xmpp Account - anyone who writes this account a message like:

"chat Who is Friedrich Schiller ?"

or:

"Chat Who is Friedrich Schiller ?""


Then this plugin sends everything behind "Chat" to ChatGPT 4o over the openAI API. You need a valid API Key for using this API. For example define an environment variable before you start Profanity.
In Linux it would be:  "export OPENAI_API_KEY=sk-...." 

The answer of ChatGPT will be send to the XMPP contact that sends the message. Like:

"Antwort vom plugin: Friedrich Schiller was born at 10. November 1759 ....."

To load this plugin in your Profanity XMPP Terminal Chat Client: Please copy the chat04.py file of this repo in your user directory, start profanity and type:

/plugins install ~/chat04.py

### sources:
This plugin was inspired by Rainer Stropeks scooling  about openAI API from the german heise-academy during Juli 2024. In this scooling he provided his code from the Microsoft AI day:
https://github.com/rstropek/microsoft-ai-day/tree/main/labs/015-basics-python
