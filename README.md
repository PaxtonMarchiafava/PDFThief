# PDFTheif

## Overview + Justification

Often times there are restrictions to pdfs that companies will sell like not allowing you to print them or only having acess to them for a restricted ammount of time. This annoys me. If I buy information that happens to be in a PDF, I would like to:
1. Be able to print the PDF that I bought.
2. Not worry about losing access to it because a liscence expired.
3. And most importantly *open it outside of Adobe Acrobat*. 

I have a digital copy of the Canadian Electrical Code (CEC) that I am [*legally required*](https://sac-ace.ca/resources/electric-sign-codes-and-standards/canadian-electrical-code/) to follow when installing electrical panels for work. This document will no longer open in Acrobat after July 7th, 2025. ![ExpirationDate](/MEDIA/ExpirationDate.png) After that, how am I supposed to know the laws I need to follow? Unfortunately, I am just expected to pay again. 

Thus, I have made this tool that will screen shot every page of the pdf, and put the screenshots in a new completely unrestricted pdf. Free to do whatever the user wants.

## Use

To use it, the program should be run, and Abobe Acrobat should be the fisrt thing to open when alt tabbing. Press run and it should just work. it will automatically alt tab over, resize and go to the first page of the PDF. It can take a long time on long files (CEC is almost 1000 pages) but I havent had it crash yet.

## Downsides
 - No CTRL + F because there is no text
 - No copy paste because there is no text
 - File is aproximately 6 times larger
 - Links no longer work (page numbers and links to outside websites)

## Future of this project
There are still a few bugs I will probably fix at some point but it works for the most part and I have my copy of the CEC so I'm happy. Don't expect any updates, but they will probably come eventually.
