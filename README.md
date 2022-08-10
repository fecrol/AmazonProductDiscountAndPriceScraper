# Amazon Product Discount & Price Scraper (APDPS)

Web scraper built with Python 3 and Selenium 4 to keep track of discount and price changes on an Amazon product page. Intended to be used with Windows Task Scheduler to run daily and save data to a CSV file, and a Microsoft Power Automate flow to send an email report when there is a price difference between the price registered on script run and the price registered the previous day.

## Setup - Windows

Make sure you have Python 3 installed (My exact Python version at the time of writing this was Python 3.10.4)

###### Steps to copy the directory using Git:
- Navigate to the directory where you wish to save the project.
- Copy the path to the directory
- Open the command line
- Input: ```cd (press Shift+Insert to paste copied directory path)``` and hit Enter
- Input: ```git clone https://github.com/fecrol/AmazonProductDiscountAndPriceScraper.git``` and hit Enter

###### Steps to set up a Python virtual environment and install the needed dependecies:
- Open the directory which containes the project code.
- Copy the path to the directory
- Open the command line
- Input: ```cd (press Shift+Insert to paste copied directory path)``` and hit Enter
- Next input: ```py -3 -m venv venv``` and hit Enter
- Next input: ```venv\Scripts\activate``` and hit Enter (This will activate the Python virtual environment)
- Next input: ```pip install -r requirements.txt``` to install all the rquired dependecies in the virtual environment

###### Steps to create a batch file to run the program:
- Open the directory which contains the project code.
- Copy the directory path
- Open Notepad
- And replicate this:
```project_code_directory_path\venv\Scripts\activate.bat && python project_code_directory_path\scraper.py "{'url': '[INSERT url to specific amazon product page]', 'csv-filename': 'price_data.csv', 'csv-file-path': '[INSERT path to directory where you wish to save csv file]'}" && project_code_directory_path\venv\Scripts\deactivate.bat```
- Save the file as your_filename.bat in a directory of your choosing.
- Your batch file should look something like this:
<img width="1064" alt="batch_file" src="https://user-images.githubusercontent.com/38907699/183686677-ad8a9bdf-d39f-428f-ae1b-67ff2d31adeb.PNG">

###### Key points regarding the batch file:
- Make sure you don't accidentaly remove any single or double quotations from here: ```"{'url': '[INSERT url to specific amazon product page]', 'csv-filename': 'price_data.csv'}"```
- The URL you provide needs to be for Amazon page of a specific product.
- Example of a an Amazon page of a specific product:
![Screenshot (11)](https://user-images.githubusercontent.com/38907699/183686007-70368ffd-d0c9-47ac-b6a3-61493d55b3d8.png)

After the completion of all the above instructions, the program should be runnable.

###### Steps to run the program:
- Navigate to the directory containing the batch file
- Double click the batch file to run the program

If the program fails, please doube check you have installed all the dependecies, your batch file is correct, and that you have provided a valid URL to an Amazon product page.
