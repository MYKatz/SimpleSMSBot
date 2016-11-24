# SimpleSMS
Execute Python functions through text messaging using Twilio!

## Features

* Completely free to use
* Easy to configure 
* Customizable

## Getting Started

Getting started should be pretty quick.  It only takes a few minutes to get everything set up.  Make sure that main.py and functions.py are in the same folder.

### Twilio Registration

If you don't already have a twilio account, you're going to need to register one.  Thankfully, they have a trial available that includes all of the features that this bot needs.  A credit card isn't even necessary!  The steps you'll need to take are as follows:

1. Register for the [Twilio Trial] (https://www.twilio.com/try-twilio)
2. Go through the new account process and register your phone number
3. Jot down your **Account SID** and **Auth Token**
4. Go to [Manage Numbers] (https://www.twilio.com/console/phone-numbers/incoming)
5. Click on your twilio number to configure it
6. Scroll down in the configure page and put 'http://twimlets.com/echo?Twiml=%3CResponse%3E%3C%2FResponse%3E' in the "A message comes in" field.

Optional: if you want to use this with more than one number you will need to either pay for a full account or verify more numbers to your account for free.  We'll go with the second option:

1. In the phone numbers page, go to [Verified Caller IDs] (https://www.twilio.com/console/phone-numbers/verified)
2. Press the red "+" sign to add more of your phone numbers
3. Follow through with the steps that twilio presents you with.

### Configuring the program

To get the program up and running you're only going to need to do a few things things:

1. Use pip to install twilio ('pip install twilio')
2. Put your Account SID into the variable accountSID
3. Put your Auth token into the variable authToken
4. Set variable tnum to your twilio number including country code but without spaces or brackets (eample: +18586515050)
5. Optionally you can change errormsg to whatever message you would like to text back if someone uses improper format or a nonexistant command.

Once you're done this run main.py and send a command to your twilio number.  Do this by sending '!' followed by the command you want.  There are two commands pre-programmed into the file: 'test' and 'testparam'.  If you want to execute 'test', for example, you would send "!test" (without quotes) to your twilio number.  Commands like 'testparam' have a certain amount of arguments (1 in this example).  Arguments are easily sent in this format: "!testparam arg1 arg2 arg3".  The program finds out how many arguments each function requires, and only uses that amount.  'testparam' only needs one parameter, so in python the above command would be executed as 'testparam(arg1)'.  Likewise, if a user sends a command that is lacking the required arguments, those will be replaced by a space.  For example, the command '!testparam' would be executed as 'testparam(" ")'.

### Defining Commands

It's very easy to create commands if you can program in python.  Your ability is pretty much your only limit.  All you need to do is define a function in the functions.py file and then add it to 'fdict' in the format '{"functionName":functionName}' (notice one is a string and the other isnt).  You'll see that there are already two functions (described above).  The possibilities are pretty much limitless, the only requirements are that the function compiles (obviously) and it returns a string value.

