print"Let's get started!!!"
spy_name = raw_input("What is your name SPY: ")                      # defining variable.
spy_salutation = raw_input("What should we call you(Mr. or Ms.): ")

if len(spy_name)>0:

spy_name = spy_salutation +""+ spy_name                              # concatenation of name and salutation
print "WELCOME " + spy_name + " Glad to have you back with us!"      # assignment operator parsing happens from r to l.

                                                                     #name = "Mr.Bond"
                                                                     #if len(name)>0:
                                                                         #new_message = "YAY! Name is not empty"
                                                                         #print new_message
