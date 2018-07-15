import numpy as np


def find_len_common_part(first_text, second_text):
    common_letter = np.zeros((len(first_text), len(second_text)))
    for i in range(len(first_text)):
        for j in range(len(second_text)):
            if first_text[i] == second_text[j]:
                common_letter[i, j] = common_letter[i - 1, j - 1] + 1
    return common_letter.max()


def find_count_common_letter(first_text, second_text):
    common_letter = np.zeros((len(first_text), len(second_text)))
    for i in range(len(first_text)):
        for j in range(len(second_text)):
            if first_text[i] == second_text[j]:
                common_letter[i, j] = common_letter[i - 1, j - 1] + 1
            else:
                common_letter[i, j] = max(common_letter[i - 1, j],
                                          common_letter[i, j - 1])
    return common_letter.max()



