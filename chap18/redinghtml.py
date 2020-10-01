with open('file2.txt','r') as ht:
    with open('file1.txt','a') as t:
        for line in ht.readlines():
            if '<a herf=' in line:
                pos = line.find('<a href=')
                fq= line.find('\"',pos)
                lq = line.find('\"',fq+1)
                url = line[fq+1:lq]
                t.write(url + '\n')
            else:
                pass


