def delete_spaces(string1, string2):
    string_new1 = ''
    string_new2 = ''
    for i in range(len(string1)):
        if string1[i] != ' ':
            string_new1 += string1[i]
    for i in range(len(string2)):
        if string2[i] != ' ':
            string_new2 += string2[i]
    return string_new1 == string_new2


string1 = input("Введите первую строку:\n")
string2 = input("Введите вторую строку:\n")

print(delete_spaces(string1, string2))