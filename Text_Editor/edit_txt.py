
class TextEditor:

    @staticmethod
    def parse_string(txt, number_of_characters) -> str:
        message_new_line = ''
        for letter_index in range(len(txt)):

            if letter_index % number_of_characters == 0 and letter_index != 0:
                message_new_line += f'{txt[letter_index]}\n'
            else:
                message_new_line += txt[letter_index]
        return message_new_line

