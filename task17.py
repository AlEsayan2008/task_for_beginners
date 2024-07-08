def a_finder(text):
    index = text.find("a")
    if index == -1:
        print(text)
    else:
        print(s[:index])
text = "qjbejaswji"
a_finder(text)
