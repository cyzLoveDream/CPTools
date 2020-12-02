A series of Chinese processing tools

There are some features in the package. If you need to use it can be installed directly

extract_chinese(self, text, symbols= "", remove_letter=False)

Extract chinese from raw text. You can choose symbols to replace non-Chinese characters in the corpus


filter_words_in_corups(self, sensitive_list, raw_text_list)

Use AC automata to filter sensitive words


is_chinese(self, uchar)
Determine if a character is Chinese


get_json_data(self, path)

Read json data from a file, where each line is a Dict


save_data_to_npy(self, data, path)

read_data_from_npy(self, path)


