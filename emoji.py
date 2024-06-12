def emoji_converter(words):
    emojis = {
    ":)": "😃",
    ":(": "😔"
    }
    words = message.split(' ')
    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '
    return output

message = input("How are you feeling today? > ")
print(emoji_converter(message))

