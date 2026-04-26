words = "abcdefghijklmnopqrstuvwxyz"


for word in words:
    b_word = bytes(word.upper(), encoding="utf-8")
    print(f"{word.upper()}:", b_word[0])
    
print('----------')

for word in words:
    b_word = bytes(word, encoding="utf-8")
    print(f"{word}:", b_word[0])

print('----------')

for i in range(256):
    print(f"{i}:", bytes([i]))