import re
import linecache
import os.path

path = "C:/cygwin64/home/Ge"

original = os.path.join(path, "CTemails" +".txt")         

reg_complete_name = os.path.join(path, "message" +".txt")         
extra_complete_name = os.path.join(path, "message_and_info" +".txt")   

temp = os.path.join(path, "temp" +".txt")         


o = open(original, "r")      

r = open(reg_complete_name, "w")
e = open(extra_complete_name, "w")

t = open(temp, "w+")

gotoextra = False
got_major = False
hit_digit = False
pass_now = False
message_written = False
name = "blank"
e_count = 0
r_count = 0

major_list = ['Architectural Technology', 'Communication Design', 'Nursing', 'Computer Engineering Technology', 'Certified Mid-Wifery', 'Hospitality Management', 'Chemistry', 'Entertainment Technology', 'Liberal Arts & Sciences', 'Dental Hygiene', 'Professional and Technical Writing', 'Human Services', 'Biomedical Informatics', 'Restorative Dentistry', 'Mechanical Engineering Technology', 'Mathematics','Construction Management and Civil Engineering Technology', 'Computer Systems Technology', 'Bioinformatics', 'Microbiology', 'Computer Engineering Technology', 'Computer Systems Technology','Electrical and Telecommunications Engineering Technology','Biology', 'Radiologic Technology & Medical Imaging', 'Law and Paralegal Studies', 'Health Services Administration', 'Business']


# parse scraped data by it's text
for o_line in o:
	t.write(str(o_line)) 

	if "https" not in o_line:
		pass

	else:
		t.seek(0)
		for t_line in t:
			if len(t_line) > 60:
				gotoextra = True

		if gotoextra:
			t.seek(0)

			message_written = False
			for t_line in t:

				if re.match(r'[0-9]{1,4}.*\n.*', t_line) != None:
					hit_digit = True

				else:
					if hit_digit == True:
						name = t_line
						hit_digit = False
						continue

					if t_line.strip() in major_list:
						major = t_line.strip()
						print "got major: "
						print major
						got_major = True

					if message_written:
						e.write(t_line)
						if "https" in t_line:
							e.write("\n")

					else:			

						# write email message		
						if got_major and name != "blank":
							e.write("Hey ")
							e.write(name.split(' ', 1)[0].capitalize().strip())
							e.write(", ")
							e.write("\n")
							e.write("\n")
							e.write("How ya doin? ")
							e.write("Hope it's cool I got your info from Openlab. I made this app for school that mad students here have already started using ")
							e.write("(especially ")
							e.write(major)
							e.write(" students for some reason!) ")
							e.write("and maybe you wanna get in on it too...")
							e.write("\n")
							e.write("\n")
							e.write("It's called Wherewolf Social Mapping and it lets you and everyone else talk and see what's up at school or wherever in realtime. Check it out in the appstore LINK LINK")
							e.write("\n")
							e.write("\n")
							e.write("Thanks!")
							e.write("\n")
							e.write("Greg")							
							e.write("\n")
							e.write("\n")
							e.write(str(e_count))
							e.write("\n")
							e.write("----------------------------------------------------------------------------------------")
							e.write("\n")
							got_major = False

						# if student's name is not available
						elif name != "blank":
							e.write(str(e_count))
							e.write("\n")
							e.write("Hey ")
							e.write(name.split(' ', 1)[0].capitalize().strip())
							e.write(", ")
							e.write("\n")
							e.write("\n")
							e.write("How ya doin? ")
							e.write("Hope it's cool I got your info from Openlab. I made this app for school that mad students here have already started using ")
							e.write("and maybe you wanna get in on it too...")
							e.write("\n")
							e.write("\n")
							e.write("It's called Wherewolf Social Mapping and it lets you and everyone else talk and see what's up at school or wherever in realtime. Check it out in the appstore LINK LINK")
							e.write("\n")
							e.write("\n")
							e.write("Thanks!")
							e.write("\n")
							e.write("Greg")							
							e.write("\n")
							e.write("\n")
							e.write(str(e_count))
							e.write("\n")
							e.write("----------------------------------------------------------------------------------------")		
							e.write("\n")

						e_count = e_count + 1
						message_written = True	
		else:
			t.seek(0)
			for t_line in t:
				r.write(t_line)

		t.seek(0)
		t.truncate()

		gotoextra = False
		
o.close()
r.close()
e.close()
t.close()