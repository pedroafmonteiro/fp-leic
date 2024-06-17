def remove_leading(ip):
    ip = ip.split(".")
    final = []
    for i in ip:
        i = str(int(i))
        final.append(i)
    final = ".".join(final)
    return final