def mail_merge(names, mail_template):
    names_final_list = []
    final_list = []
    with open(names, 'r') as names:
        names_list = names.readlines()
    with open(mail_template, 'r') as mail:
        template = mail.readlines()
    string_template = ''.join(template)
    for n in names_list:
        names_final_list.append(n.replace('\n', ''))
    for n in names_final_list:
        string = string_template.replace('<name>', n)
        final_list.append(string)
    return final_list