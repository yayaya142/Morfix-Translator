import openpyxl
from openpyxl import Workbook
import webbrowser
import openpyxl as xl
import Morfix_translator_func as funcs
import os


def main():
    file_path = funcs.file_location_html()
    # file_path = f"F:/Users/shai/Downloads/Living with the Monks - Filtered Items.html"
    words = funcs.Open_html(file_path)
    #create xlsx file
    xlsx_path = file_path.replace(".html", ".xlsx")
    words_xl = Workbook()
    words_xl.save(xlsx_path)
    words_xl = xl.load_workbook(xlsx_path)
    sheets = words_xl["Sheet"]
    #open xlsx
    start_row = 1
    end_row = len(words)
    count_row = start_row - 1
    count_bug = 0
    #add words to ecxel (ROW A)
    for row in range(start_row, end_row + 1):
        cell = sheets[f'a{row}']
        cell.value = words[count_row]
        count_row += 1    
    words_xl.save(xlsx_path)
    count_row = 0
    #add translated words
    words_list = []
    for row in range(start_row, end_row + 1):
        count_row += 1
        cell = sheets[f'a{row}']
        words_list.append(cell.value)
        cell.value = funcs.remove_worng_strings(cell.value)
        os.system('cls')
        print(f"{count_row} from {end_row}")
        translated_word = funcs.morfix_translate(cell.value)
        translated_word_cell = sheets[f"b{row}"]
        translated_word_cell.value = translated_word
        if 'Bug' in translated_word:
            count_bug += 1
    words_xl.save(xlsx_path)
   #Data on what was translated

    print("\nTranslated List Completed")
    print(f"Translated start at: {start_row}")
    print(f"Translated end at: {end_row }")
    print(f"Translated {end_row - start_row + 1 - count_bug} words")
    print(f"{count_bug} words not translated")
    print("Last word is:", words_list[-1])
    input("Press any key to exit")

if __name__ == '__main__':
    main()
