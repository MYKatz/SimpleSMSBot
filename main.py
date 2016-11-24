from twilio.rest import TwilioRestClient
import inspect
import functions
import time

accountSID = ''
authToken = ''
tnum = ''
errormsg = "Error Message"

twilioClient = TwilioRestClient(accountSID, authToken)
command = []
lastsid = ""

def bot(sms):
    if sms.body[0] != "!":
        return False
    else:
        full = sms.body + " "
        full = full.rstrip()
        global command
        command = full.split()
        command[0] = command[0].replace("!","")
        b = ""
        try:
            params = len(inspect.getfullargspec(functions.fdict[command[0]]).args)
            for i in range(0,params):
                command.append(" ")
        except:
            return False
        try:
            executed = 'functions.'+command[0]+"("
            for i in range(0,params):
                if i != params-1:
                    executed+='str('+ 'command[' +str(i+1) + ']),'
                else:
                    executed+='str('+ 'command[' +str(i+1) + '])'
            executed += ")"
            if command[0] in functions.fdict:
                print(command[0])
                return(executed)
            else:
                return False
        except:
            return False

while True:
    messages = twilioClient.messages.list(to=tnum)
    inp = messages[0]
    if inp.sid == lastsid:
        time.sleep(5)
        ##The message has already been wo8rked on.  Reset loop.
    else:
        oput = bot(inp)
        if oput != False:
            exec('b='+oput)
        else:
            b = errormsg
        message = twilioClient.messages.create(body=b, from_=tnum, to=inp.from_)
        lastsid = inp.sid    
