#import beautifulsoup and request here
import requests
import json
from flask import Flask
from flask import render_template
from bs4 import BeautifulSoup



def displayJobDetails():
    print("Display job details")

#function to get job list from url 'https://www.indeed.com/jobs?q={role}&l={location}'
def getJobList(role,location):
    url = 'https://www.indeed.com/jobs?q={role}&l={location}'
    url = url.replace("{role}",role)
    url = url.replace("{location}",location)

    # Complete the missing part of this function here 
    page = requests.get(url) # from https://www.dataquest.io/blog/web-scraping-python-using-beautiful-soup/
    job = BeautifulSoup(page.content, 'html.parser')

    #print("job title: ")
    #print(job.find('h2', class_= 'jobTitle'))
    #print("company name: ")
    #print(job.find('span', class_ = 'companyName'))
    #print("job description: ")
    #print(job.find('div', class_ = 'job-snippet'))
    #print("job salary: ")
    #print(job.find('div', class_ = 'salary-snippet-container'))

    

    jobTitle = job.find('h2', class_= 'jobTitle').text
    companyName = job.find('span', class_ = 'companyName').text
    jobDescription =  job.find('div', class_ = 'job-snippet').text
    jobSalary = job.find('div', class_ = 'salary-snippet-container').text
    
    allJobDetails = ["Title: " + jobTitle, "Company: " + companyName, "Description: " + jobDescription, "Salary: " + jobSalary]
    return allJobDetails



#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    print("Saving data to JSON")
    out = open("jobDetails.json", "w")
    json.dump(jobDetails, out)
    print("Successfuly saved to specified file")

app = Flask(__name__)
@app.route("/")
def displayJobDetails():
    
    #write a code to give call to json file and then render html page
    response = requests.get('https://raw.githubusercontent.com/ijacob20/BeautifulSoup/main/jobDetails.json')
    responseJSON = response.json()
    return render_template('index.html',responseJSON = responseJSON)




#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    print("Enter location you want to search")
    location = input()
    print("Role: " + role + "\nLocation: " + location)
    # Complete the missing part of this function here
    print(getJobList(role, location))
    jobDetails = getJobList(role, location)
    saveDataInJSON(jobDetails)
if __name__ == '__main__':
    main()
