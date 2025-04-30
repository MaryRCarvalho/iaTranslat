from deep_translator import GoogleTranslator, MyMemoryTranslator

def chatbot():
    print("Olá! Sou um charbot de tradução. Digite 'sair' para encerrar.")
    while True:
        texto = input ("\nDigite o texto para traduzir: ")
        if texto.lower() == "sair":
            break
        idioma_destino = input ("Para qual idioma você quer traduzir? Por exemplo: en, es, fr, de ")
        idioma_destino_myMemory = input ("Para qual idioma você quer traduzir? Por exemplo: en-CA, en-US, en-UK, es-ES, ca-ES, cav-ES, fr-FR, fr-CA, nl-NL ")
        try:
            traducao = GoogleTranslator(source='auto', target=idioma_destino).translate(texto)
            print(f"Tradução: {traducao}")
            traducaoMyMemory = MyMemoryTranslator(source='pt-BR', target=idioma_destino_myMemory).translate(texto)
            print(f"Tradução: {traducaoMyMemory}")
        except Exception as e:
            print(f"Erro na tradução: {e}")
chatbot()