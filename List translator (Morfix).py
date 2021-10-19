from Morfix_translator_func import morfix_translate
import webbrowser
import openpyxl as xl
file_path = input("""Enter file path and file name
    for example: D:\softwere\python 3\AA project\AA my project\.vscode\filename (with no ending)
    """)
# file_path = r"D:\softwere\python 3\AA project\AA my project\List translator (morfix)\words"
file_path = file_path + ".xlsx"
loop_var = 'start'

while loop_var != "n":
    words_list = []

    words_xl = xl.load_workbook(file_path)
    sheets = words_xl["Sheet1"]

    start_row = int(
        input("In which line would you like to start the translation: "))
    end_row = sheets.max_row
    if end_row - start_row > 25:
        end_row = start_row + 24

    for row in range(start_row, end_row + 1):
        cell = sheets[f'a{row}']
        words_list.append(cell.value)
        translated_word = morfix_translate(cell.value)
        translated_word_cell = sheets[f"b{row}"]
        translated_word_cell.value = translated_word
    words_xl.save(file_path)
    print(f"Words list: \n{words_list}")
    print("\nTranslated List Completed")
    print(f"Translated start at: {start_row}")
    print(f"Translated end at: {end_row }")
    print(f"Translated {end_row - start_row + 1} words")
    print("Last word is:", words_list[-1])

    loop_var = (input(
        "Do you want to translate another list? \nPress 'y' for Yes or press 'n' for No: ")).lower()
