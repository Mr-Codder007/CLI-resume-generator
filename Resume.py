'''
Resume Basic Structure:-
1. Name
2. Address
3. Phone number
4. Email
5. prefered Languages
6. Educational Qualification
7. Skills
8. Other Skills

'''
import os
from datetime import datetime

def description():
    text=[]
    print("Write *END when You Want to Stop ")
    while True:
        line=input()
        if line == "*END":
            print("\n Thank You......\n")
            break
        text.append(line)
    return("\n".join(text))

header="======RESUME======"

folder_name='Resume'
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
# os.chdir(folder_name) used for changing directory

file_name=input("Enter Your File Name:").strip()
if os.path.exists(file_name):
    print("File Already Exist")
    choice=input("Enter 'Y' for Overwrite or 'N' for new file (Y/N): ").strip().lower()
    if choice != 'y':
        file_name=input("Re-Enter Your File Name:").strip()

#Personal Info 
name=input("Enter Your Name: ").strip().title()
address_input=input("Enter Your Address: ").strip()
number_input=input("Enter Your Phone Number: ").strip()
email_input=input("Enter Your Email Address: ").strip()
education=input("Enter Your Educational Qualification: ").strip()
if education== '':
    print("\tYou Forgot to enter\n")
    education=input("Please Enter It Now: ").strip()
print("Enter Your Skills:")
skills=input().strip().split(",")

#Job Section
job=input("Do you have any job Experince?(Y/N): ").strip().lower()
# job_title=''
# job_duration=''
# job_description=''
# company_name=''
job_details=''
if job== 'y':
    option=int (input("Enter How Many Job Details You Want to Add: "))
    # job_details=''
    for i in range (option):
        count=f"Job no. {i+1}"
        print(f"Give The Details About {count}")
        job_title=input("Enter Your Job Title: ").strip().title()
        company_name=input("Enter The Company Name: ").strip().title()
        job_duration=input("Enter Job Duration: ")
        job_description=input("Enter Y/N If You Want to Add Description:").strip().lower()
        if job_description == 'y':
            job_description= description()
        else:
            job_description='None'
        information=f"""
        Job no {i+1}

        Job Titel: {job_title}

        Company Name: {company_name}

        Job Duration: {job_duration}

        Job Description: {job_description}
        """
        job_details+=information
elif job not in ['y','n']:
    print("Invalid input......")
    job=input("Enter Again (Y/N)")

#Project Section
project=input("Enter Y/N If You Want to add projects: ").strip().lower()
# project_name=''
# project_description=''
project_details=''
if project == 'y':
    count=int (input("Enter The Number of Poject You Want to Add: "))
    for i in range(count):
        print(f"Project no. {i+1}")

        project_name=input("Enter The Project Name: ").strip().title()
        project_description=description()
        information=f"""
        Project no. {i+1}

        Project Name: {project_name}

        Project Description: {project_description}
        """
        project_details+=information

elif project != "y" or project != "n":
    print("Invalid input......")
    project=input("Enter Again (Y/N)")

#Creation and Storing the user data
file_path= os.path.join(folder_name,f"{file_name}.txt")
with open(file_path, "w") as f:
    # if(name=='' or address_input=='' or number_input=='' or email_input==''): this is for basic level
    
    if not all([name,address_input,number_input,email_input]): #much clean and smart method
        print("You have not give all the input")
        exit()

    f.write(header.center(80) + '\n\n')

    f.write(f"Name: {name}\n")
    f.write(f"Address: {address_input}\n")
    f.write(f"Phone no. {number_input}\n")
    f.write(f"Email: {email_input}\n")
    f.write(f"Educational Qualification: {education}\n")
    f.write("Skills:\n")
    for skill in skills :
        f.write(f'--{skill}\n')
    if job == 'y':
        f.write(job_details)
        # f.write(f'Job Title: {job_title}\n')
        # f.write(f"Comapany Name: {company_name}\n")
        # f.write(f"Job Duration: {job_duration}\n")
        # f.write(f"Job Description: {job_description}\n")
    if project == 'y':
        f.write(project_details)
        # f.write(f"Project Name: {project_name}\n")
        # f.write(f"Project Description: \n\t{project_description}\n")
    timestamp=f"Updated on: {datetime.now().strftime('%d-%m-%Y, %H:%M:%S')}"
    f.write("\n"+timestamp.rjust(80))

print("\n\tInformation Successfully Collected.")