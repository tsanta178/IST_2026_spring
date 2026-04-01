import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    for ch in plaintext:
        if ch.isupper():
            new_pos = (ord(ch) - ord('A') + shift) % 26
            ciphertext += chr(ord('A') + new_pos)
        elif ch.islower():
            new_pos = (ord(ch) - ord('a') + shift) % 26
            ciphertext += chr(ord('a') + new_pos)
        else:
            ciphertext += ch
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    for ch in ciphertext:
        if ch.isupper():
            new_pos = (ord(ch) - ord('A') - shift) % 26
            plaintext += chr(ord('A') + new_pos)
        elif ch.islower():
            new_pos = (ord(ch) - ord('a') - shift) % 26
            plaintext += chr(ord('a') + new_pos)
        else:
            plaintext += ch
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    best_shift = 0
    best_count = 0
    
    for shift in range(26):
        plaintext = ""
        for ch in ciphertext:
            if ch.isupper():
                new_pos = (ord(ch) - ord('A') - shift) % 26
                plaintext += chr(ord('A') + new_pos)
            elif ch.islower():
                new_pos = (ord(ch) - ord('a') - shift) % 26
                plaintext += chr(ord('a') + new_pos)
            else:
                plaintext += ch
        
        words = plaintext.split()
        count = sum(1 for word in words if word in dictionary)
        
        if count > best_count:
            best_count = count
            best_shift = shift
    
    return best_shift
