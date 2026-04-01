def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    keyword = keyword.lower()
    key_len = len(keyword)
    key_index = 0
    
    for ch in plaintext:
        if ch.isalpha():
            shift = ord(keyword[key_index % key_len]) - ord('a')
            
            if ch.isupper():
                new_pos = (ord(ch) - ord('A') + shift) % 26
                ciphertext += chr(ord('A') + new_pos)
            else:
                new_pos = (ord(ch) - ord('a') + shift) % 26
                ciphertext += chr(ord('a') + new_pos)
            
            key_index += 1
        else:
            ciphertext += ch
    
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
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
