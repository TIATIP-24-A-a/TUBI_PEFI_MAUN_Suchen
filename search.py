def searchText(text, searchText):

    occurrences = 0
    currentIndex = 0
    while currentIndex < len(text):
        if text[currentIndex] == searchText:
            occurrences += 1

        currentIndex += 1

    return occurrences