import webbrowser
import openpyxl as xl
import Morfix_translator_func as funcs


def main():
    file_path = funcs.file_location()

    loop_var = 'start'

    while loop_var != "n":
        words_list = []

        words_xl = xl.load_workbook(file_path)
        sheets = words_xl["Sheet1"]

        start_row = int(
            input("In which line would you like to start the translation: "))
        end_row = sheets.max_row
        count_row = start_row - 1
        count_bug = 0

        for row in range(start_row, end_row + 1):
            count_row += 1
            cell = sheets[f'a{row}']
            words_list.append(cell.value)
            cell.value = funcs.remove_worng_strings(cell.value)
            print(f"{count_row} from {end_row}")
            translated_word = funcs.morfix_translate(cell.value)

            translated_word_cell = sheets[f"b{row}"]
            translated_word_cell.value = translated_word
            if 'Bug' in translated_word:
                count_bug += 1
        try:
            words_xl.save(file_path)
        except PermissionError:
            print("\n\nPermission error\nClose open xlsx files and try again.")
            input("")
            # close program
            return
        
        print("\nTranslated List Completed")
        print(f"Translated start at: {start_row}")
        print(f"Translated end at: {end_row }")
        print(f"Translated {end_row - start_row + 1 - count_bug} words")
        print(f"{count_bug} words not translated")
        print("Last word is:", words_list[-1])
        loop_var = (input(
            "Do you want to translate another list? \nPress 'y' for Yes or press 'n' for No: ")).lower()


if __name__ == '__main__':
     main()
