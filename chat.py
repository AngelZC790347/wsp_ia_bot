import openai as ai
from pathlib import Path
import os
import config


def generate_tmp_chat_file(personal_desc: str, name_usr: str):
    path = Path("chats/" + name_usr + ".txt")
    if not path.is_file():
        context = f"Someone named {name_usr} in a conference tell you this: \n{name_usr}: "
        with open(path, "a") as f:
            f.write(context)
    else:
        with open(path, "r") as f:
            context = f.read()
    return context


def generate_response(message: str, name_usr):
    content = generate_tmp_chat_file(config.ia_personality, name_usr)
    content += message + '\n'
    response = ai.ChatCompletion.create(
        api_key=os.getenv('OPENAI_API_KEY'),
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": config.ia_personality},
            {"role": "user", "content": content}
        ]
    )["choices"][0]["message"]["content"]
    with open(Path(name_usr + ".txt"), 'a') as f:
        f.write(message.replace(f"{config.ia_name}: ", ""))
        f.write(f"\n{config.ia_name}: " + response + f"\n\n{name_usr}:")
    return response
