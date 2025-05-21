def phrase(name, lastname, adjective):
    return f"Hola {name} {lastname}, eres un {adjective}"


result_phrase = phrase(adjective="fiera", name="Jaime", lastname="Carrasco")
print(result_phrase)


def chapter(name, number, adjective="Buenísimo"):
    return f"""El próximo capítulo se llamara:
{name}, es el numero {number} y será {adjective}"""


result_chapter = chapter(name="Bajo el subsuelo", number=20)
print(result_chapter)
