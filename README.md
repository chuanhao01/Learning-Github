# Personal Finance Tracker

## Description
This is a personal finance tracker I made using python and Google's APIs. The program creates a Tkinter window where you can input your daily transactions into the program and it will be saved on Google Sheets. The window also allows the user to retrieve data from the Google Sheet, analyse the data and then present the data to the user. 
> Note: A more detailed documentation and description is on the wiki

## Getting Started
So far, this program is a personal project, and the set up to change the gauth to other accounts has not been made yet. The guide may be up at a later date. 

### Prerequisites
These libraries should be pre-installed for this program to work:
```
tkinter
SciPy(or numpy and pandas)
gspread
oauth2client
```
This program also requires the set-up of a Google service account, and Google's drive and sheet API on the Google developer's console.
### Installing
To intsall the libraries if they are not already installed, we can use python in-built pip library
```
pip install scipy
pip install tkinter
pip install --upgrade google-api-python-client
```
PS: The libraries can also be downloaded off their respective websites as a package.(Not reccomended)

## Built With
- Tkinter -To build the GUI 
- pandas -To anylse the data from Google Sheets
- gspread -To get and push data from and to Google Sheets
- oauth2client -To authenticate Google's APIs

## Future Imporvements/To Do
- [ ] Using matplotlib to visualise the results
- [ ] Adding a user guide
- [ ] Adding a method to remove data from the Google Sheets in the GUI
- [ ] Make it compatible for multiple years
- [ ] Finish Wiki
