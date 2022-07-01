a=10
def somethink():
    a=15
    print ('In local',a)
somethink()

print('Global',a)


##################################################################
######################################################################

a=10
def somethink():
    global a # while using **Global**  here global and local values are became as similar;

    a=15
    print ('\nIn local',a)
somethink()

print('Global',a)


#####################################################################
################################################################################


a = 10
b=56
def somethink():

    a = 15
    x=globals()['b']
    print('\nGlobal values inside of local:',x)
    print('In local', a)


somethink()

print('Global', a)