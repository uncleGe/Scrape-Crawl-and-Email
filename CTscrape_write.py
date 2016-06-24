# got to p 272.. connection error
import requests
from bs4 import BeautifulSoup
import re
import os.path
# from __future__ import print_function

path = "C:/cygwin64/home/Ge"

email_complete_name = os.path.join(path, "CTemails_0" + ".txt")         
phone_complete_name = os.path.join(path, "CTphone_numbers_0" + ".txt")         

e = open(email_complete_name, "w")
p = open(phone_complete_name, "w")

p_count = 0
e_count = 0


_digits = re.compile('\d')
def contains_digits(d):
    return bool(_digits.search(d))


def dataget(url):
	try:
		r2 = requests.get(url)
	except requests.exceptions.ConnectTimeout:
		print "dataget() error!"

	soup = BeautifulSoup(r2.content, "html.parser")

	name = soup.find("span", {"class": "profile-name"})

	clubs = soup.find("div", {"class": "club-list"})
	club_name = clubs.find_all("span",  {"class": "original-copy hidden"})
	clubs_list = clubs.find_all("p",  {"class": "truncate-on-the-fly hyphenate"})

	data = soup.find_all("div", {"class": "col-sm-17"})

	for item in data:
		if contains_digits(item.text) and item.text.find('@')==-1:
			# write to phone

			global p_count 
			p_count = p_count + 1
			p.write(str(p_count))
			p.write("\n")

			p.write(name.contents[0][:-10].encode('utf-8'))
			p.write("\n")

			for item in data:
				p.write(item.text.strip().encode('utf-8'))
				p.write("\n")
			
			item_number = 1
			index = 0
			for item in clubs_list:
				p.write("Club ")
				p.write(str(item_number))
				p.write("\n")
				p.write(club_name[index].text.encode('utf-8'))
				p.write(item.text.encode('utf-8'))
				item_number = item_number + 1
				index = index + 1
				p.write("\n")

			p.write(url)
			p.write("\n")

			p.write("\n")
			p.write("\n")
			break
		elif item.text.find('@')!=-1:
			# write to emails

			global e_count
			e_count = e_count + 1
			e.write(str(e_count))
			e.write("\n")

			e.write(name.contents[0][:-10].encode('utf-8'))
			e.write("\n")

			for item in data:
				e.write(item.text.strip().encode('utf-8'))
				e.write("\n")

			item_number = 1
			index = 0
			for item in clubs_list:
				e.write("Club ")
				e.write(str(item_number))
				e.write("\n")
				e.write(club_name[index].text.encode('utf-8'))
				e.write(item.text.encode('utf-8'))
				item_number = item_number + 1
				index = index + 1
				e.write("\n")

			e.write(url)
			e.write("\n")

			e.write("\n")
			e.write("\n")
			break



def crawler():
	start_page = 1
	while (start_page < 19):
	# while (start_page < 305):
		print "Page:", start_page
		people_url = "https://openlab.citytech.cuny.edu/people/?school=school_all&department=dept_all&usertype=student&group_sequence=newest&upage=" + str(start_page)
		try:
			r1 = requests.get(people_url)
		except requests.exceptions.ConnectTimeout:
			print "crawler() crap!"

		people_soup = BeautifulSoup(r1.content, "html.parser")

		people_list = people_soup.find_all("h2", {"class": "item-title"})
		# print people_list

		for person in people_list:
			person_url = person.a.get("href")
			dataget(person_url)

		start_page = start_page + 1


crawler()
e.close()
p.close()
print "done!"


# reference
# global vars http://stackoverflow.com/questions/423379/using-global-variables-in-a-function-other-than-the-one-that-created-them



