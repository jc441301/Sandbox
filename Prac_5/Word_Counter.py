def main():
    text = input("Enter your text here: ").split()
    words_dic = count_word(text)
    word_list = list_word(text)
    number_of_characters = find_longest(word_list)
    for i in word_list:
        print('{:{}} : {}'.format(i, number_of_characters, words_dic[i]))


def count_word(text):
    words_dic = {}
    for word in text:
        if word in words_dic:
            words_dic[word] += 1
        else:
            words_dic[word] = 1
    return words_dic


def list_word(text):
    word_list = []
    for word in text:
        if word not in word_list:
            word_list.append(word)
    word_list.sort()
    return word_list


def find_longest(word_list):
    number_of_characters = 0
    for word in range(len(word_list)):
        if len(word_list[word]) > number_of_characters:
            number_of_characters = len(word_list[word])
    return number_of_characters


if __name__ == '__main__':
        main()