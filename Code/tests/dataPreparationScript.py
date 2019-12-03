import mailbox
import json
import os

def getcharsets(msg):
    charsets = set({})
    for c in msg.get_charsets():
        if c is not None:
            charsets.update([c])
    return charsets

#Gmail
mboxFileName = 'mailArchive.mbox'
mboxFilePath = 'C:\\Projects\\Thesis\Code\\tests\\mailArchive.mbox'
mboxFileSmallPath = 'C:\\Projects\\Thesis\Code\\tests\\mailArchiveSmall.mbox'
outputPath = 'C:\\Projects\\Thesis\Code\\tests\\'
outputFileName = 'mailDump_{0}.json'
sizes = [100, 500, 1000, 2000, 4000]
mboxInstance = mailbox.mbox(mboxFilePath)

def googleData(mboxPath, s, outF, outPath):
    """
    mboxPath - path to the mbox file\n
    s        - sizes of files you want to output\n
    outF     - output file name ( has to have {0} for the file size)
    """
    mboxInstance = mailbox.mbox(mboxPath)
    outputData = {}
    outputData['messages'] = []
    i = 0
    for mail in mboxInstance:
        print(i)
        i+=1
        body = ''
        if mail.is_multipart():
            for part in mail.walk():
                if part.is_multipart():
                    for subpart in part.walk():
                        if subpart.get_content_type() == 'text/plain':
                            body += str(subpart.get_payload(decode=True))
                elif part.get_content_type() == 'text/plain':
                    body += str(part.get_payload(decode=True))
        elif mail.get_content_type() == 'text/plain':
            body += str(mail.get_payload(decode=True))

        for charset in getcharsets(mail):
            try:
                body=body.decode(charset)
            except:
                pass

        #print(mail['subject'], '\n', mail['from'], '\n', mail['to'], '\n', body)
        outputData['messages'].append({"id":i, "content":str(mail['subject']) + "\n"+ str(mail['from']) + "\n" + str(mail['to']) + "\n" + str(body)})

        if i in s:
            f = open(outPath + outF.format(str(i)), 'x')
            json.dump(outputData, f)
            f.close()

    f = open(outputPath + outF.format(str(i)), 'x')
    json.dump(outputData, f)
    f.close()

#Facebook
facebookInbox = 'C:\\Projects\\facebook-maksymbrzeczek\\messages\\inbox'

def facebookData(inboxPath, outPath, outFileName, max):
    """
    
    """
    outputData = {}
    fileName = 'message_1.json'
    i = 0
    for x in os.listdir(inboxPath):
        dir = os.path.join(inboxPath, x)
        if os.path.isdir(dir):
            messageFile = os.path.join(dir, fileName)
            if os.path.isfile(messageFile):
                with open(messageFile, 'r') as f:
                    data = json.load(f)
                    for mes in data['messages']:
                        i+=1
                        try:
                            print(i, mes['content'])
                        except:
                            pass
                        if i == max:
                            return
                        

facebookData(facebookInbox, '', '', 20000)