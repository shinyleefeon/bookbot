def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    count = {}
    for l in text:
        lower = l.lower()
        if lower in count:
            count[lower] += 1
        else:
            count[lower] = 1
    return count

def sort_on(item):
    return item["num"]

def sorted_char_count(text):
    count = char_count(text)
    red = []
    for key in count:
        red.append({"char": key, "num": count[key]})
    red.sort(reverse = True, key=sort_on)
    return red


