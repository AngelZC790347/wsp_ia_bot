import openai as ai
from pathlib import Path
OPENAI_API_KEY = "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"


tokens = 0


def generate_tmp_chat_file(personal_desc: str, nombre: str):
    path = Path(nombre + ".txt")
    if not path.is_file():
        context = f"Alguien random llamado {nombre} en una conferencia te dice lo siguiente: \n{nombre}: "
        with open(path, "a") as f:
            f.write(context)
    else:
        with open(path, "r") as f:
            context = f.read()
    return context


def generate_response(message: str, nombre):
    nombre_ia = "Andrea Jimenez"
    description = f"""Eres {nombre_ia} una estudiante de administracion """
    content = generate_tmp_chat_file(description, nombre)
    content += message + '\n'
    response = ai.ChatCompletion.create(
        api_key=OPENAI_API_KEY,
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": description},
            {"role": "user", "content": content}
        ]
    )["choices"][0]["message"]["content"]
    with open(Path(nombre + ".txt"), 'a') as f:
        f.write(message.replace(f"{nombre_ia}: ", ""))
        f.write(f"\n{nombre_ia}: " + response + f"\n\n{nombre}:")
    return response
