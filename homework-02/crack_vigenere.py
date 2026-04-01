import string

# Lire le fichier chiffré
with open('cipher.txt', 'r', encoding='utf-8') as f:
    ciphertext = f.read()

# Garder seulement les lettres pour l'analyse
letters = [c for c in ciphertext if c.isalpha()]

def index_of_coincidence(text, key_len):
    """Calcule l'indice de coïncidence pour une longueur de clé donnée"""
    n = len(text)
    total_ic = 0
    
    for i in range(key_len):
        group = [text[j] for j in range(i, n, key_len)]
        if len(group) < 2:
            continue
        
        freq = {}
        for c in group:
            freq[c] = freq.get(c, 0) + 1
        
        ic = 0
        m = len(group)
        for count in freq.values():
            ic += count * (count - 1)
        if m > 1:
            ic /= m * (m - 1)
        
        total_ic += ic
    
    return total_ic / key_len if key_len > 0 else 0

# Trouver la meilleure longueur de clé
best_len = 1
best_ic = 0

print("Recherche de la longueur de la clé...")
for length in range(1, 30):
    ic = index_of_coincidence(letters, length)
    print(f"Longueur {length}: IC = {ic:.4f}")
    if ic > best_ic:
        best_ic = ic
        best_len = length

print(f"\nLongueur de clé probable: {best_len}\n")

# Fréquences des lettres en anglais (ordre décroissant)
english_freq = "etaoinshrdlcumwfgypbvkjxqz"

# Trouver la clé
key = ""
for pos in range(best_len):
    # Extraire les lettres à cette position
    group = [letters[i] for i in range(pos, len(letters), best_len)]
    
    best_shift = 0
    best_score = 0
    
    for shift in range(26):
        # Déchiffrer le groupe avec ce shift
        decrypted = []
        for ch in group:
            if ch.isupper():
                new_pos = (ord(ch) - ord('A') - shift) % 26
                decrypted.append(chr(ord('A') + new_pos).lower())
            else:
                new_pos = (ord(ch) - ord('a') - shift) % 26
                decrypted.append(chr(ord('a') + new_pos).lower())
        
        # Calculer un score basé sur la fréquence
        freq = {}
        for d in decrypted:
            freq[d] = freq.get(d, 0) + 1
        
        score = 0
        for idx, letter in enumerate(english_freq):
            if letter in freq:
                score += freq[letter] * (len(english_freq) - idx)
        
        if score > best_score:
            best_score = score
            best_shift = shift
    
    key += chr(ord('a') + best_shift)
    print(f"Position {pos}: shift = {best_shift} -> lettre de clé = {key[-1]}")

print(f"\nClé trouvée: {key}")

# Déchiffrer avec la clé trouvée
def decrypt_vigenere(ciphertext, keyword):
    plaintext = ""
    keyword = keyword.lower()
    key_len = len(keyword)
    key_index = 0
    
    for ch in ciphertext:
        if ch.isalpha():
            shift = ord(keyword[key_index % key_len]) - ord('a')
            if ch.isupper():
                new_pos = (ord(ch) - ord('A') - shift) % 26
                plaintext += chr(ord('A') + new_pos)
            else:
                new_pos = (ord(ch) - ord('a') - shift) % 26
                plaintext += chr(ord('a') + new_pos)
            key_index += 1
        else:
            plaintext += ch
    
    return plaintext

decrypted = decrypt_vigenere(ciphertext, key)

# Sauvegarder le résultat
with open('cracked.txt', 'w', encoding='utf-8') as f:
    f.write(decrypted)

print(f"\nTexte déchiffré sauvegardé dans cracked.txt")
print("\nAperçu des 500 premiers caractères:")
print(decrypted[:500])
