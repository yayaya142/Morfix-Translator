
# Morfix-Translator<br />

## About this program.<br />
This program is used to translate words from English to Hebrew using the website Morfix.<br />
With this program, you can easily insert words from a kindle book into the Quizlet app.<br />




**How to use**<br />
You have two options you can use translate from excel or directly from HTML file.<br />
<br />
<br />

Guide to using translate from excel:<br />
<br />
To use this program create a .xlsx file.<br />
Write one word in English in each line. (only in A)<br />
Run the program and Select the file.<br />
Enjoy!

**screenshots 'translate from excel'**<br />
<br />
**words in English**<br />
![words](https://user-images.githubusercontent.com/82652251/137897373-7ae51219-e12f-4e10-9569-d815a2fe2486.png)
<br />
**Pop up window**<br />
![xlsx](https://user-images.githubusercontent.com/82652251/137897826-1e869df4-3d3b-4e85-b0c4-f4c81e822ab3.png)
<br />
**The program ran**<br />
![program run](https://user-images.githubusercontent.com/82652251/139835492-e2553011-7233-4853-9e85-c72ae40e52aa.png)
<br />
**The menu looks like this**<br />
![after run](https://user-images.githubusercontent.com/82652251/139835551-d7cb42e4-5ae1-4008-acd8-8419f577d7ad.png)
<br />
**After the program ran**<br />
![After the program ran](https://user-images.githubusercontent.com/82652251/137892760-1aae74d5-e826-4079-b2c9-61308d34b821.png)
<br />
<br />
<br />
<br />
Guide to using translate from HTML file:<br />
<br />
<br />
you need to export an HTML file from the kindle app.<br />
open the program and select your file.<br />
the program will automatically create a new excel file with 2 Collom.<br />
Collom A > English words.<br />
Collom B > translated words in Hebrew.<br />
Enjoy!<br />



**screenshots 'translate from HTML'**<br />
<br />
**words in English**<br />
![words](https://user-images.githubusercontent.com/82652251/140636075-cfc5ee8b-63dc-4075-8951-e5a575f8ef8d.png)
<br />
**Pop up window**<br />
![pop up](https://user-images.githubusercontent.com/82652251/140636194-2252d4b3-cd2a-41fe-acc7-2e541c8c8988.png)
<br />
**The program ran**<br />
![run](https://user-images.githubusercontent.com/82652251/140636087-545e41ba-2049-450c-8913-ca54c67316a3.png)
<br />
**The menu looks like this**<br />
![menu](https://user-images.githubusercontent.com/82652251/140636090-449a52e6-e9d4-4fa9-b6b2-81d308aae81e.png)
<br />
**After the program ran**<br />
![words](https://user-images.githubusercontent.com/82652251/140636109-b14ff91a-45b9-4684-b679-839c6d5491eb.png)

<br />








**Updates history**:<br />
<br />
**v.1.00**<br />
  morfix open 25 file, with loop.<br />
  open with .txt file<br />
  
 **v.1.01**<br />
    1) It is now possible to use an excel file<br />
    2) There is a start selection of the translation (the end is set automatically when the maximum is 25 words per translation)<br />
 
 **v.1.02**<br />
    1) Add Support for automatic translation<br />
    2) The translation is saved in an excel file<br />
 
**v.1.03**<br />
    1) Window open at the beginning to select a file location<br />
    2) Functions were added to the file Morfix_translator_func.py<br />
    
 **v.1.04**<br />
    1) Fixed the bug that was made by marks like " ' , . @ space and more<br />
    2) Now marks like  " ' , . @ automatically removed from excel files.<br />
    3) Now when the script run it shows word number and how many words there are.<br />
    4) Add bugs count that the users see at the end of the run.<br />
    5) Add errors message when:<br />
         * The excel sheet is open.<br />
         * when Collom A has an empty row.<br />
    6) Add if main == name to the main file.<br />
    7) Functions were added to the file Morfix_translator_func.py.<br />

 **v.1.05**<br />
  1) Now you have two options to use translate from excel or directly from HTML file.<br />
  2) Functions were added to the file Morfix_translator_func.py.<br />
