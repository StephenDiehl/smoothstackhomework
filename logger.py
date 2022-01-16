from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
import os, logging, webbrowser

files = os.listdir('.')
logging.basicConfig(filename='log.log',filemode='w',format='%(asctime)s - %(levelname)s %(message)s',datefmt='%H:%M:%S', encoding='utf-8', level=logging.DEBUG)
months = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06', 'July': '07',
          'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}
years = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']
directories = [item for item in files if '.xlsx' in item]


def workb():
    picked = False
    while not picked:
        for item in enumerate(directories, 1):
            print(item)
        which = input("Please pick which file you would like to get data from using it's corresponding number above: ")
        if which.isdigit():
            if int(which) <= (len(directories)):
                picked = True
            else:
                print('That option was not a choice please try again')
                continue
        else:
            print('That option was not a choice, please try again')

    return directories[int(which)-1][:-5]

def would():
    ask = input("Would you like to me to open the log file for you? (Yes or No)  ")
    leave = False
    try:
        if ask.lower() == "yes" or ask.lower() == "y":
            webbrowser.open('log.log')
            leave = True
        if ask.lower() == "no" or ask.lower() == "n":
            print("Okay have a good day. ")
            leave = True
    except Exception as e:
        print(e)
    finally:
        if leave:
            print("Have a good day")
        else:
            print("Looks like you gave a bad value that wasn't expected, please answer yes or no. :)")
            would()

def main():
    current = workb()
    wb = load_workbook(current + '.xlsx')
    mandd = [item for item in current.split("_")[::-1] if item.capitalize() in months or item in years]
    mand = f'{mandd[0]}-{months[mandd[1].capitalize()]}'
    ws = wb['Summary Rolling MoM']
    row = None
    for item in ws['A']:
        if mand in str(item.value):
            row = item.row
    test = [ro for ro in ws.iter_rows(min_row=row, max_row=row, values_only=True)]
    new_test = [item for item in test[0][1:] if item != None]
    logging.info(f"Month of {mandd[1].capitalize()}, {mandd[0]} ")
    logging.info(f"Calls Offered: {new_test[0]}")
    logging.info(f"Abandon after 30s: {new_test[1]*100}%")
    logging.info(f"FCR : {new_test[2]*100}0%")
    logging.info(f"DSAT : {new_test[3]*100}0%")
    logging.info(f"CSAT : {new_test[4]*100}0%")
    ws = wb["VOC Rolling MoM"]
    z = 0
    found = False
    try:
        for item in ws['1']:
            z += 1
            if mand in str(item.value):
                found = True
                break
            else:
                pass
        if not found:
            z=0
            for item in ws['1']:
                z+= 1
                if str(item.value) in months:
                    found = True
                    break
                else:
                    pass
    except Exception as e:
        logging.warning(e)
    finally:
        if found:
            pass
        else:
            logging.warning('Was unable to find the correct month and year combination. Check file to make sure it matches conventional naming methods.')
            raise FileNotFoundError
    nums = [item.value for item in ws[get_column_letter(z)][1:] if item.value != None and int(item.value) != 0]
    logging.info(f"In Net Promoter Score - Base Size = {nums[0]}")
    if nums[1] > 200:
        logging.info(f"Promoters: {nums[1]}, which is good!")
    else:
        logging.info(f"Promoters: {nums[1]}, which is bad!")
    if nums[2] > 100:
        logging.info(f"Passives: {nums[2]}, which is good!")
    else:
        logging.info(f"Passives: {nums[2]}, which is bad!")
    if nums[3] > 100:
        logging.info(f"Decractors: {nums[3]}, which is good!")
    else:
        logging.info(f"Decractors: {nums[3]}, which is bad!")
    would()

if __name__ == "__main__":
    main()