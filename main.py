message_chiffré = input ('Entrez le texte à déchiffrer :')

liste = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for x in range (len(liste)):
    liste.append (liste[x])



def chiffrage_lettre(lettre, liste, clef):
    for i in range (len(liste)):
        if lettre == '':
            return ''
        elif liste [i] ==lettre:
            return str (liste[i+clef])
    return '?'

for clef in range (1,26):
    message_déchiffré = str()
    for lettre in message_chiffré:
        message_déchiffré += chiffrage_lettre (lettre,liste,clef)
    print (message_déchiffré)

a = (input)


