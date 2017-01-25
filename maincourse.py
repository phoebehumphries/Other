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

def main():
    c1 = Art
    courses.append(c1)
    c2 = Biology
    courses.append(c2)
    c3 = Business
    courses.append(c3)




def new_course():
    def create_person():
        ''' User can input their own details '''
        print()
        new_coursename= input("What is your first name? ")
        print()
        new_qual = input("What is your surname? ")
        print()
        new_desc = input("What is your date of birth? Please enter in the form MMM DD YYYY ")
        print()
        new_ws = input("Please enter an 11 digit number:")
        print()
        new_p0 = Main(new_coursename, new_qual, new_desc, new_ws, new_requirements, new_opportunities, new_testimonials)
        people.append(new_p0)
        return new_p0
