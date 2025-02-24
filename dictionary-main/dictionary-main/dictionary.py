meme_dictionary = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "ROFL bir şakaya karşılıktır, LOL gibidir"
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if kelime in meme_dictionary.keys():
    print(meme_dictionary[word])
else:
    print("Bu kelime sözlüğümüzde yok!")
