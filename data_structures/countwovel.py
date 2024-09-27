def get_count(sentence):
    count= 0
    for c in sentence:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            count += 1
    return count


print(get_count("caminata total"))