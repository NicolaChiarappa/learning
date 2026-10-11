# Snippet 4 - predict every printed line.
raw_name = "  ada lovelace "    #assegna a raw_name la stringa che è immutabile
raw_name.strip()    #il risultato viene perso
raw_name.title()    #il risultato viene perso
print(repr(raw_name))   #non so cosa fa la funzione di repr() probabile che stampi "  ada lovelace "
clean_name = raw_name.strip().title()   ## clean_name fa riferimento all'oggetto stringa "Ada Lovelace"
print(repr(clean_name)) #non so cosa fa la funzione di repr() probabile che stampo "Ada Lovelace"
print(repr(raw_name)) #non so cosa fa la funzione di repr() probabile che stampi "  ada lovelace "
