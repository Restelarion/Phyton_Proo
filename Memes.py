meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "Una cara riendose"
            "F": "Para pagar respeto"
            "Random": "algo aleatorio"
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print (word,": ",meme_dict[word])
    # ¿Qué debemos hacer si se encuentra la palabra?
else:
    print("Palabra no encontrada")
    # ¿Qué hacer si no se encuentra la palabra?
