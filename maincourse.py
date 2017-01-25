from lol import More


courses = []
def print_courses():


for lol in courses:
    print('{0}',
          print(),
          '{1}',
          print(),
          '{2}',
          print(),
          '{3}',
          print(),
          '{4}',
          print(),
          '{5}',
          print(),
          '{6}',
          print(),
          '{7}.'.format(lol.coursename, lol.qualification, lol.description, lol.whystudy, lol.requirements, lol.opportunities, lol.testimonials))
    print()


def new_course():
    def create_person():
        ''' User can input their own details '''
        print()
        new_coursename= input("What is your first name? ")
        print()
        new_surname = input("What is your surname? ")
        print()
        new_dob = input("What is your date of birth? Please enter in the form MMM DD YYYY ")
        print()
        new_phone = input("Please enter an 11 digit number:")
        print()
        new_p0 = Main(new_coursename, new_qualification, new_description, new_whystudy, new_requirements, new_opportunities, new_testimonials)
        people.append(new_p0)
        return new_p0
