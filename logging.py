def log_file(str1):
    f=open('log.txt','a')
    f.writelines('\n'+str1)
    f.close()

b='helo'
log_file(b)

