with open('input.txt', 'r', encoding='utf8') as f:
    text = f.read()
    print("Lengde av datasett i antall karakterer:", len(text))

    #Ser på første 1000 karakterer først
    print(text[:1000])

    #Lag liste av unike karakterer i teksten
    chars = sorted(list(set(text)))
    vocab_size = len(chars) #Antall av hver bokstav
    print(''.join(chars))
    print(vocab_size)

    #Mappe fra bokstaver til indeks og omvendt
    stoi = {ch:i for i, ch in enumerate(chars)} #stoi = string to index
    itos = {i:ch for i, ch in enumerate(chars)} #itos = index to string
    encode = lambda s: [stoi[c] for c in s] #Tekst til liste av indekser
    decode = lambda l: ''.join([itos[i] for i in l]) #Liste

    print('encode: ', encode('Selma kan kooodeee'))
    print('decode: ', decode([24, 27, 24])) #LOL

    #lage tokenized versjon av hele teksten
    import torch
    data = torch.tensor(encode(text), dtype=torch.long)
    print(data.shape, data.dtype)
    print(data[:1000]) #første 1000 bokstaver som indekser

    #Trening og valideringsdeler av datasettet
    n = int(0.9*len(data))
    train_data = data[:n] #alt foran n som er 90%
    val_data = data[n:] #alt etter n som er siste 10%
    print(train_data.shape, val_data.shape)
