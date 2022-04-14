#import beautifulsoup and request here
import requests
import json
from bs4 import BeautifulSoup



def displayJobDetails():
    print("Display job details")

#function to get job list from url 'https://www.indeed.com/jobs?q={role}&l={location}'
def getJobList(role,location):
    url = 'https://www.indeed.com/jobs?q={role}&l={location}'
    url = url.replace("{role}",role)
    url = url.replace("{location}",location)

    # Complete the missing part of this function here 
    page = requests.get(url)
    job = BeautifulSoup(page.content, 'html.parser')

    #print("job title: ")
    #print(job.find('h2', class_= 'jobTitle'))
    #print("company name: ")
    #print(job.find('span', class_ = 'companyName'))
    #print("job description: ")
    #print(job.find('div', class_ = 'job-snippet'))
    #print("job salary: ")
    #print(job.find('div', class_ = 'salary-snippet-container'))

    jobTitle = job.find('h2', class_= 'jobTitle')
    companyName = job.find('span', class_ = 'companyName')
    jobDescription =  job.find('div', class_ = 'job-snippet')
    jobSalary = job.find('div', class_ = 'salary-snippet-container')
    
    allJobDetails = [jobTitle, companyName, jobDescription, jobSalary]
    print(allJobDetails)



#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    print("Saving data to JSON")

#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    print("Enter location you want to search")
    location = input()
    print("Role: " + role + "\nLocation: " + location)
    # Complete the missing part of this function here
    getJobList(role, location)
if __name__ == '__main__':
    main()
