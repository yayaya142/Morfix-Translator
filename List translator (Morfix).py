import webbrowser

loop_var = 'start'
while loop_var != "n":
    file_path = input("""Enter file path and file name
    for example:
    D:\softwere\python 3\AA project\AA my project\.vscode\filename.txt
    """)
    # file_path = r"D:\softwere\python 3\AA project\AA my project\List translator (morfix)\words.txt"
    print(file_path)
    try:
        with open(file_path) as words_txt:
            word_read = words_txt.read()
            word_read = word_read.split("\n")
            if len(word_read) > 25:
                print(
                    "Sorry file is to big \nPlease make sure the file contain less then 25 words. ")
            else:
                for trans_word in word_read:
                    webbrowser.open(f'https://www.morfix.co.il/{trans_word}')
        print("Translate List Completed")
    except:
        print ("Cant find file name.\nPlease try again.")
    loop_var = (input("Do you want to translate another list? \nPress 'y' for Yes or press 'n' for No: ")).lower()
