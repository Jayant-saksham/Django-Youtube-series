from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def result(request):
    if request.method == 'POST':
        myText = request.POST.get('textbox')
    length = len(myText)
    listOfWords = myText.split()
    words = len(listOfWords)
    symbols = list('''!@#$%^&*()_+{:>?*-`~''')
    countSymbols = 0
    countLowerCase = 0
    countNumbers = 0
    countUpperCase = 0
    for i in myText:
        if i.isupper():
            countUpperCase += 1
        if i in symbols:
            countSymbols += 1
        if i.islower():
            countLowerCase += 1
        if i.isnumeric():
            countNumbers += 1
    data = {
        'length': length,
        'words': words,
        'uppers': countUpperCase,
        'lowers': countLowerCase,
        'numbers': countNumbers, 
        'symbols': countSymbols,
    }

    return render(request, 'result.html', data)