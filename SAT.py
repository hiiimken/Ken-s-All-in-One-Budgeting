# importing our GUI modules
from tkinter import *




###############################################################################################
# FUNCTIONS
###############################################################################################


### function for the button press
def fncButtonPress():
    ### Initialising variables
    strMonthlySalary = iptEnterMonthlySalary.get()
    flt50PercentResult = 0.00
    flt30PercentResult = 0.00
    flt20PercentResult = 0.00
    enterIndustry=''
    varAwardsResultGotten = varAwardsResult.get()
    varCityofResidenceResultGotten = varCityofResidence.get()

    # Checks if stuff is entered in the text box for Monthly Salary
    if strMonthlySalary != '': # if statement that checks if stuff is entered
        cnvMonthlySalary = float(strMonthlySalary) # converts it into a float value
        flt50PercentResult, flt30PercentResult, flt20PercentResult = fncBudget(cnvMonthlySalary) # uses the function to convert it into the 50/30/20
    else: # else
        return -1 # returns nothing

    ############## GUI Changing
    ### text for the text box 50% result
    txt50PercentResult = Label(frm50PercentResult, text=str('{0:.2f}'.format(flt50PercentResult)), bg='#fff', fg='#330000', font='helvetica 8') # makes a text box with the following characteristics
    txt50PercentResult.place(relx=0.5, rely=0.5, anchor=CENTER) # where the text box is placed

    ### text for 30% result
    txt30PercentResult = Label(frm30PercentResult, text=str('{0:.2f}'.format(flt30PercentResult)), bg='#fff', fg='#330000', font='helvetica 8') # makes a text box with the following characteristics
    txt30PercentResult.place(relx=0.5, rely=0.5, anchor=CENTER)# where it is placed

    ### text for 20% Result
    txt20PercentResult = Label(frm20PercentResult, text=str('{0:.2f}'.format(flt20PercentResult)), bg='#fff', fg='#330000', font='helvetica 8') # makes a text box with the following characteristics
    txt20PercentResult.place(relx=0.5, rely=0.5, anchor=CENTER) # where it is placed


    ### Industry Comparison
    if float(strMonthlySalary) >= float(dctAwards[varAwardsResultGotten]):  # if the value entered is equals to or higher than the industry standard
        txtAwardsResult = Label(frmAwardsResult, text=str('{0:.2f}'.format(float(dctAwards[varAwardsResultGotten]))), bg='#fff', fg='green', font='helvetica 8')
        txtAwardsResult.place(relx=0.5, rely=0.5, anchor=CENTER) # print the result green
    else: # if not
        txtAwardsResult = Label(frmAwardsResult, text=str('{0:.2f}'.format(float(dctAwards[varAwardsResultGotten]))), bg='#fff', fg='red', font='helvetica 8')
        txtAwardsResult.place(relx=0.5, rely=0.5, anchor=CENTER) # print the result red

    ### City of Residence Comparison
    if (float(strMonthlySalary) * 0.5) >= float(dctCityofResidence[varCityofResidenceResultGotten]): # if the value entered is equals to or higher than the cost of living
        txtCostofLivingResult = Label(frmCostofLivingResult, text=str('{0:.2f}'.format(dctCityofResidence[varCityofResidenceResultGotten])), bg='#fff', fg='green', font='helvetica 8') # print it green
        txtCostofLivingResult.place(relx=0.5, rely=0.5, anchor=CENTER) # where the text box is placed
    else: # if not
        txtCostofLivingResult = Label(frmCostofLivingResult, text=str('{0:.2f}'.format(dctCityofResidence[varCityofResidenceResultGotten])), bg='#fff', fg='red', font='helvetica 8') # print it red
        txtCostofLivingResult.place(relx=0.5, rely=0.5, anchor=CENTER) # where the text box is placed 

    ### function for clearing the results
    def fncClear():
        txt50PercentResult.destroy() # destroys the text box for the 50 Percent Result from the budgeting fuction
        txt30PercentResult.destroy() # destroys the text box for the 30 percent Result from the budgeting function
        txt20PercentResult.destroy() # destroys the text box for the 20 percent result from the budgeting function
        txtAwardsResult.destroy() # destroys the green/red text box for the result of the comparison to industry standards
        txtCostofLivingResult.destroy() # destroys the green/red text box for the result of the comparison to the cost of living

    ### Button for clearing
    btnClear = Button(wdwMainWindow, text='Clear', bg='#fff', fg='#330000', command=fncClear) # creates a button with the command fncClear() to clear the result
    btnClear.place(x=20, y=430, width=960, height=51) # where the text box is placed

### function for splitting into 50/30/20
def fncBudget(fltMonthlySalary):
    flt50Percent = fltMonthlySalary * 0.5 # gets 50 percent from fltMonthlySalary
    flt30Percent = fltMonthlySalary * 0.3 # gets 30 percent from fltMonthlySalary
    flt20Percent = fltMonthlySalary * 0.2 # gets 20 percent from fltMonthlySalary
    return flt50Percent, flt30Percent, flt20Percent # returns the result 50 percent, 30 percent and 20 percent




###############################################################################################
# GUI STUFF - MAIN WINDOW
###############################################################################################



### main window
wdwMainWindow = Tk() # sets the window up
wdwMainWindow.title("Ken's All-in-One Suite") # sets the tile for the window as Ken's All in One Suite
wdwMainWindow.geometry('1000x500') # size of the window
wdwMainWindow.resizable(0,0) # makes the window not resizable
wdwMainWindow.configure(background='#fafaf7') # makes the background colour very light gray

### text box heading
txtReport = Label(wdwMainWindow, text='Budgeting Suite', bg='#fafaf7', fg='#330000', font='Bahnschrift 36') # characteristics of the text box Budgeting Report
txtReport.place(relx=0.31, y=0) # where the text box is placed

### frame for the text box enter monthly salary
frmEnterMonthlySalary = Frame(wdwMainWindow, width=291, height=31, bg='#fff') # characteristics of the frame for the Enter Monthly Salary text box
frmEnterMonthlySalary.configure(highlightbackground="#bdbdb5", highlightcolor="#bdbdb5", highlightthickness=0.5, bd= 0) # characteristics for the border 
frmEnterMonthlySalary.place(x=30, y=140) # where it is placed

### text box enter monthly salary
txtEnterMonthlySalary = Label(frmEnterMonthlySalary, text='Enter Monthly Salary', bg='#fff', fg='#330000', font='helvetica 8 bold') # characteristics of the text box Enter Monthly Salary
txtEnterMonthlySalary.place(relx=0.5, rely=0.5, anchor=CENTER) # where it is placed (all relative)

### input for enter monthly salary
iptEnterMonthlySalary = Entry(wdwMainWindow, bg='#fff', fg='#330000', font='helvetica 8') # characteristics of the input box where user enters their monthly salary
iptEnterMonthlySalary.place(x=30, y=190, width=291, height=31) # where it is placed and some characteristics

### frame for text box enter industry
frmEnterIndustry = Frame(wdwMainWindow, width=131, height=31, bg='#fff') # characteristics of the frame for the text box Enter Industry
frmEnterIndustry.configure(highlightbackground="#bdbdb5", highlightcolor="#bdbdb5", highlightthickness=0.5, bd= 0) # characteristics for the border
frmEnterIndustry.place(x=30, y=240) # where it is placed

### text box enter industry
txtEnterIndustry = Label(frmEnterIndustry, text='Enter Industry', bg='#fff', fg='#330000', font='helvetica 8 bold') # characteristics of the text box Enter Industry
txtEnterIndustry.place(relx=0.5, rely=0.5, anchor=CENTER) # where it is placed (all relative)

### frame for the text box city of residence
frmCityofResidence = Frame(wdwMainWindow, width=131, height=31, bg='#fff') # characteristics of the frame for the text box city of Residence
frmCityofResidence.configure(highlightbackground="#bdbdb5", highlightcolor="#bdbdb5", highlightthickness=0.5, bd= 0) # characteristics for the border
frmCityofResidence.place(x=30, y=290) # where it is placed

### text box city of residence
txtCityofResidence = Label(frmCityofResidence, text='City of Residence', bg='#fff', fg='#330000', font='helvetica 8 bold') # characteristics of the text box city of Residence
txtCityofResidence.place(relx=0.5, rely=0.5, anchor=CENTER) # where it is placed

### frame for the text box awards
frmAwards = Frame(wdwMainWindow, bg='#fff', width=281, height=31) # characteristics of the frame for the text box Awards
frmAwards.configure(highlightbackground="#bdbdb5", highlightcolor="#bdbdb5", highlightthickness=0.5, bd= 0) # characteristics for the border
frmAwards.place(x=360, y=140) # where it is placed

### text box for the awards
txtAwards = Label(frmAwards, text='Awards', bg='#fff', fg='#330000', font='helvetica 8 bold') # characteristics for the text box for the Awards
txtAwards.place(relx=0.5, rely=0.5, anchor=CENTER) # where it is placed

### frame for the award result
frmAwardsResult = Frame(wdwMainWindow, bg='#fff', width=281, height=31) # characteristics for the frame for the text box Award Result
frmAwardsResult.configure(highlightbackground="#bdbdb5", highlightcolor="#bdbdb5", highlightthickness=0.5, bd= 0) # characteristic of the border
frmAwardsResult.place(x=360, y=190) # where it is placed


### frame for cost of living
frmCostofLiving = Frame(wdwMainWindow, bg='#fff', width=281, height=31) # characteristic for the frame for the cost of living
frmCostofLiving.configure(highlightbackground="#bdbdb5", highlightcolor="#bdbdb5", highlightthickness=0.5, bd= 0) # characteristic of the border
frmCostofLiving.place(x=360, y=240) # where it is placed

### text for cost of living
txtCostofLiving = Label(frmCostofLiving, text='Cost of Living', bg='#fff', fg='#330000', font='helvetica 8 bold') # characteristics of the text
txtCostofLiving.place(relx=0.5, rely=0.5, anchor=CENTER) # where it is placed

### frame for cost of living result
frmCostofLivingResult = Frame(wdwMainWindow, bg='#fff', width=281, height=31) # characteristics of the frame
frmCostofLivingResult.configure(highlightbackground="#bdbdb5", highlightcolor="#bdbdb5", highlightthickness=0.5, bd= 0) # characteristics of the border
frmCostofLivingResult.place(x=360, y=290) # where it is placed

### frame for the text box budget
frmBudget = Frame(wdwMainWindow, bg='#fff', width=281, height=31) # characteristics of the frame
frmBudget.configure(highlightbackground="#bdbdb5", highlightcolor="#bdbdb5", highlightthickness=0.5, bd= 0) # characteristics of the border
frmBudget.place(x=680, y=140) # where it is placed

### text for budget
txtBudget = Label(frmBudget, text='Budget', bg='#fff', fg='#330000', font='helvetica 8 bold') # characteristics of the text
txtBudget.place(relx=0.5, rely=0.5, anchor=CENTER) # where it is placed

### frame for the text box 50%
frm50Percent = Frame(wdwMainWindow, bg='#fff', width=61, height=31) # characteristics of the frame
frm50Percent.configure(highlightbackground="#bdbdb5", highlightcolor="#bdbdb5", highlightthickness=0.5, bd= 0) # characteristics of the border
frm50Percent.place(x=680, y=190) # where it is placed

### text for 50%
txt50Percent = Label(frm50Percent, text='50%', bg='#fff', fg='#330000', font='helvetica 8 bold') # characteristics of the text
txt50Percent.place(relx=0.5, rely=0.5, anchor=CENTER) # where it is placed

### frame for the text box 50% result
frm50PercentResult = Frame(wdwMainWindow, bg='#fff', width=211, height=31) # characteristics of the frame
frm50PercentResult.configure(highlightbackground="#bdbdb5", highlightcolor="#bdbdb5", highlightthickness=0.5, bd= 0) # characteristics of the border
frm50PercentResult.place(x=750, y=190) # where it is placed

### frame for the text box 30%
frm30Percent = Frame(wdwMainWindow, bg='#fff', width=61, height=31) # characteristics of the frame
frm30Percent.configure(highlightbackground="#bdbdb5", highlightcolor="#bdbdb5", highlightthickness=0.5, bd= 0) # characteristics of the border
frm30Percent.place(x=680, y=240) # where it is placed

### text for 30%
txt30Percent = Label(frm30Percent, text='30%', bg='#fff', fg='#330000', font='helvetica 8 bold') # characteristics of the text
txt30Percent.place(relx=0.5, rely=0.5, anchor=CENTER) # where it is placed

### frame for the text box 30% result
frm30PercentResult = Frame(wdwMainWindow, bg='#fff', width=211, height=31) # characteristics of the frame
frm30PercentResult.configure(highlightbackground="#bdbdb5", highlightcolor="#bdbdb5", highlightthickness=0.5, bd= 0) # characteristics of the border
frm30PercentResult.place(x=750, y= 240) # where it is placed


### frame for the text box 20%
frm20Percent = Frame(wdwMainWindow,bg='#fff', width=61, height=31) # characteristics of the frame
frm20Percent.configure(highlightbackground="#bdbdb5", highlightcolor="#bdbdb5", highlightthickness=0.5, bd= 0) # characteristics of the border
frm20Percent.place(x=680, y=290) # where it is placed

### text for 20%
txt20Percent = Label(frm20Percent, text='20%', bg='#fff', fg='#330000', font='helvetica 8 bold') # characteristics of the text
txt20Percent.place(relx=0.5, rely=0.5, anchor=CENTER) # where it is placed

### frame for the text box 20% result
frm20PercentResult = Frame(wdwMainWindow, bg='#fff', width=211, height=31) # characteristics of the frame
frm20PercentResult.configure(highlightbackground="#bdbdb5", highlightcolor="#bdbdb5", highlightthickness=0.5, bd= 0) # characteristics of the frame
frm20PercentResult.place(x=750, y=290) # where it is placed


###############################################################################################
# MAIN
###############################################################################################

### button to generate report
btnGenerateReport = Button(wdwMainWindow, text='Generate Report', bg='#fff', fg='#330000', command=fncButtonPress) # characteristics of the button
btnGenerateReport.place(x=20, y=360, width=960, height=51) # where it is placed



######################### ENTER INDUSTRY 
## Dictionary for enter industry
dctAwards = {} # initialising the dictionary

flsAwards = open('JobAwards.txt') # open the file called JobAwards.txt and put it into flsAwards
for line in flsAwards: # reads it line to line
    x = line.split(',') # splits the values separated by a comma and puts it into x 
    a=x[0] # puts the first value into a
    b=x[1] # puts the second value into b
    c=len(b)-1 # first step into removing the /n from b
    b=b[0:c] # second step into removing the /n from b
    b=b.replace('"', '') # replacing " with blank in b
    b=b.replace("'", '') # replacing ' with blank in b
    a=a.replace('"', '') # replacing " with blank in a
    a=a.replace("'", '') # replacing ' with blank in b
    dctAwards[a] = float(b) # puts the line into the dictionary as "a:b" with b as a floating point
flsAwards.close() # closes the file
## option menu for enter industry
varAwardsResult = StringVar(wdwMainWindow) # makes it into a TkInter variable
varDefaultVariableAwards = 'Aged Care' # putting the first value into the variable varDefaultVariableAwards
optEnterIndustry = OptionMenu(wdwMainWindow, varAwardsResult, *dctAwards) # creates an option menu in the Main Window, with the variable and the dictionary dctAwards
varAwardsResult.set(varDefaultVariableAwards) # sets the default variable as Aged Care
optEnterIndustry.configure(bg='#fff', fg='#330000', font='helvetica 8') # characteristics of the option menu
optEnterIndustry.place(x=180, y=240, width=141, height=31) # where it is placed



######################### City OF RESIDENCE
## Dictionary for City of residence
dctCityofResidence = {} # initialising the dictionary
flsCityofResidence = open('AustralianCities.txt') # open the file called AustralianStaates.txt and put it into flsCityofResidence
for line in flsCityofResidence: # reads the file line to line
    x = line.split(',') # splits the values separated by a comma and puts it into x
    a=x[0] # puts the first value into the variable a
    b=x[1] # puts the second value into the variable b
    c=len(b)-1 # first step into removing the /n from b
    b=b[0:c] # second step into removing the /n from b
    dctCityofResidence[a] = float(b) # puts the line into the dictionary as "a:b" with b as a floating point
flsCityofResidence.close() # closes the file


##combo box for city of residence
varCityofResidence = StringVar(wdwMainWindow) # makes a tkInterVariable called varCityofResidence
varDefaultVariableCityofResidence = 'Adelaide'  # puts the first value of the dictionary into a variable called varDefaultVariableCityofResidence
optCityofResidence = OptionMenu(wdwMainWindow, varCityofResidence, *dctCityofResidence) # creates an option menu in the main window with the variable and the dictionary dctCityofResidence
varCityofResidence.set(varDefaultVariableCityofResidence) # sets the variable to the first variable 'Adelaide'
optCityofResidence.configure(bg='#fff', fg='#330000', font='helvetica 8') # characteristics of the options menu
optCityofResidence.place(x=180, y=290, width=141, height=31) # where it is placed





wdwMainWindow.mainloop()

