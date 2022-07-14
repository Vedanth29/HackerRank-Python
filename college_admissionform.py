#Vedanth M

# A simple admission form using class and objects (object oriented programming)
print('''
***** Institute of Engineering and Technology
        APPLICATION FORM DETAILS:
''')

class collegeinfo():
    def printdata(self):
        print(f'Application Number  :{self.appnum}')
        print(f'Admission Number    :{self.addnum}')
        print('***********************************')
        print(f'ISE    :{self.i}')
        print(f'CSE    :{self.c}')
        print(f'ECE    :{self.e}')
        print('***********************************')

class personalinfo():
    def printpersdata(self):
        print('PERSONAL INFORMATION:')
        print(f'Applicant name :{self.appname}')
        print(f'Nationality    :{self.nation}')
        print(f'Religion       :{self.rel}')
        print(f'DateOfBirth    :{self.dob}')
        print(f'Father name    :{self.fname}')
        print(f'Mother name    :{self.mname}')
        print(f'Phone number   :{self.pnum}')
        print(f'Address        :{self.add}')
        print(f'SSLC marks     :{self.ssmark}')
        print(f'PUC marks      :{self.pumark}')
        print('************************************')
        
#applicant1
print('Application1')
college = collegeinfo()
college.appnum = 100000
college.addnum = 26
college.i = 'yes'
college.c = 'no'
college.e = 'no'
college.printdata()

personal = personalinfo()
personal.appname = 'Vedanth'
personal.nation = 'India'
personal.rel = 'Hindu'
personal.dob = 'date of birth'
personal.fname = 'father name'
personal.mname = 'mothername'
personal.pnum = '9*********'
personal.add = 'india'
personal.ssmark = 80
personal.pumark = 70
personal.printpersdata()

#applicant2
print('Applicaton2')

college = collegeinfo()
college.appnum = 2000000
college.addnum = 00
college.i = 'no'
college.c = 'yes'
college.e = 'no'
college.printdata()

personal = personalinfo()
personal.appname = 'ranjan'
personal.nation = 'Russia'
personal.rel = 'Nil'
personal.dob = 'date of birth'
personal.fname = 'father name'
personal.mname = 'mothername'
personal.pnum = '0*********'
personal.add = 'Russia'
personal.ssmark = 100
personal.pumark = 20
personal.printpersdata()
