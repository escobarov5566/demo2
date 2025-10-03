from platform import system

from langchain_gigachat import GigaChat
from langchain_core.messages import HumanMessage, SystemMessage
from pyexpat.errors import messages

key = 'MDE5OWEzNzgtZTQyMC03ZGU3LTliZmMtN2Y0YjY3MGQ5Zjg1OjU2MzFkOWFjLWM1NzktNDZiYi1iMWQ3LThkNjRjYzI3ZjBiNA=='


llm = GigaChat(credentials=key, verify_ssl_certs = False)
while True:
    system_prompt = SystemMessage(content="ты диспетчер географической службы, тебе будут приходить названия стран, ты должен отвечать на эти запросы только названием столицы той страный которую указали. Если в запросе указа не страна то так и сообщи.")
    user_input = input("запрос")
    user_prompt = HumanMessage(content=user_input)
    messages = [system_prompt, user_prompt]
    response = llm.invoke(messages)
    print(response.content)
