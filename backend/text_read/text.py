from cgitb import text


f = open('allData.txt')
new = open('new.txt','a')
array=f.readlines()
new.write('Semester,year,subject,code,section,ATotal,BTotal,CTotal,DTotal,FTotal,A-FTotal,GPA,ITotal,STotal,UTotal,QTotal,XTotal,Total,Instuctor,mathCredit,commCredit,scienceCredit,langCredit,artCredit,americanCredit,govermentCredit,socialCredit'+'\n')
for line in array:
    if line[0:25] == "GRADE DISTRIBUTION REPORT" and line[-3:-2]!='e':#plain
        semester = line[30:-7]
        year = line[-6:-1]
        year=year[:-1]
    elif line[0:25] == "GRADE DISTRIBUTION REPORT" and line[-15:-2] == "Undergraduate":#udergrade atached
        semester = line[30:len(line)-21]
        year=line[len(line)-20:-16]
    elif line[0:25] == "GRADE DISTRIBUTION REPORT" and line[-10:-2] == "Graduate" and line[-12:-11]!='&':#Graduate atached
        semester = line[30:len(line)-16]
        year=line[len(line)-15:-11]
    elif line[0:25] == "GRADE DISTRIBUTION REPORT" :#underagrate & graduate
        semester = line[30:len(line)-32]
        year=line[len(line)-31:-27]
    elif line[4:5]=='-' and line[8:9]=='-' and line[0:1] != '-':
        if len(line)>60:
            words=line.split()
            tempLine=""
            for word in words:
                if word[-1] != '%':
                    tempLine=tempLine+','+word
            tempLine=tempLine[1:5]+','+tempLine[6:9]+','+tempLine[10:]
            #fix names
            for i in range(len(tempLine)-1, -1, -1):
                if(tempLine[i]==',' and (tempLine[i-1].isalpha() or tempLine[i-1]=='.' or tempLine[i-1]==',')):
                    if tempLine[i-1]==',':
                        tempLine=tempLine[:i]+tempLine[i+1:]
                    else:
                        tempLine=tempLine[:i]+' '+tempLine[i+1:]
                elif(tempLine[i].isdigit()):#bad case
                    tempLine=tempLine[:i+1]+','+tempLine[i+1:]
                elif(tempLine[i]==',' and tempLine[i-1].isdigit()):
                    break
            #fix gpa miss input
            count=0
            total=""
            for i in range(len(tempLine)):
                if tempLine[i]==',':
                    count+=1
                if count==8 and tempLine[i]=='.':
                    tempLine=tempLine[:i-1]+','+tempLine[i-1:]
                    break
            #print(tempLine)
            new.write(semester+','+year+','+tempLine+','+'FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE'+'\n')
new.close()
f.close()
