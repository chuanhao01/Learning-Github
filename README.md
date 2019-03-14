# Personal Finacnce Tracker

## Description
This is a personal finace tracker I made using python and Google Drive and Sheet API. Tkinter was used to create a Graphical User Interface(GUI) to make taking user inputs and displaying information easier. Pandas was used to analyse the data taken from Google Sheets easier. 

## Usage

### User Input
This program when run, is able to take daily transactions through the GUI, and push the data to the Google Sheets. This data from the user is checked to catch exceptions and will not push data that is of invalid type. For example, the amount can only be a number and not a string. 

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

