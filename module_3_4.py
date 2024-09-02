# Произвольное число параметров
def single_root_words(root_word, *other_words):
    same_words = []
    lower_others = [item.lower() for item in other_words]
    lower_root = root_word.lower()
    for original_item, lower_item in zip(other_words, lower_others):
        if lower_root in lower_item or lower_item in lower_root:
            same_words.append(original_item)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)