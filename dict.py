bilinmeyen_kelime_sozlugu = {    
    "LOL": "Kahkaha atmak.",
    "BRB": "Hemen döneceğim.",
    "OMG": "Aman Tanrım!",
    "FYI": "Bilgin olsun.",
    "TTYL": "Sonra konuşalım.",
    "TMI": "Gereğinden fazla bilgi.",
    "BFF": "En iyi arkadaş.",
    "FOMO": "Kaçırma korkusu.",
    "YOLO": "Bir kez yaşarsın.",
    "SMH": "Hayal kırıklığı.",
    "ICYMI": "Kaçırdıysan.",
    "IDK": "Bilmiyorum.",
    "LMAO": "Kahkaha atmak.",
    "RIP": "Rahmetli.",
    "WTF": "Ne oluyor?"
}

kelime = input("Bir kısaltma girin: ").casefold()  # Kullanıcının girdiği kelimeyi küçük harfe çevir

if kelime in bilinmeyen_kelime_sozlugu:
    print(kelime.upper() + ": " + bilinmeyen_kelime_sozlugu[kelime])
else:
    print("Bu kısaltma sözlükte bulunmuyor.")
