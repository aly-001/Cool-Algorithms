def spoilerize(phrase):
    replaced_phrase = ''
    for char in phrase:
        if char.lower() in 'abcdefghijklmnopqrstuvwxyz':
            replaced_phrase += "||" + char + "||"
        else:
            replaced_phrase += char

    return replaced_phrase