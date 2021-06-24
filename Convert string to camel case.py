#Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized
# (known as Upper Camel Case, also often referred to as Pascal case).

def to_camel_case(text):
    import re
    words = re.split('-|_',text)
    camel_case = ""
    if words[0].isupper() == False:
        camel_case = words[0]
        for i in range(1,len(words)):
            j = words[i].capitalize()
            camel_case += j
    else:
        for i in words:
            j = i.capitalize()
            camel_case += j

    return camel_case

str = input("Enter String ")
print(to_camel_case(str))