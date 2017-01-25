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


print_courses()