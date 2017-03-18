import advanced_python_regex as faculty
import csv

def writetocsv():
    with open('emails.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        emails = faculty.getlistof('email')
        for email in emails:
            writer.writerow(email)