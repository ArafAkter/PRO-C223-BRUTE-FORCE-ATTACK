import PyPDF2 as pd
filename = input('Path to the file: ')
filename=filename.strip()
file = open(filename,'rb')
pdfReader = pd.PdfReader(file)

tried = 0

if not pdfReader.is_encrypted:
    print('The file is not password protected! You can successfully open it!')
else :
    wordlistfile=open('wordlist.txt','r',errors = 'ignore')
    body=wordlistfile.read().lower()
    words = body.split('\n')
    for i in range(len(words)):
        word = words[i]
        print('Trying to decode password by {}'.format(word))
        result=pdfReader.decrypt(word)
        if result == 1:
            print('success the password is '+word)
            break
        elif result == 0:
            tried+=1
            print('tried '+str(tried)) 
            continue


            


