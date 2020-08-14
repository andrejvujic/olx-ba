"""
	!!! UNOFFICIAL !!!
	OLX.ba Python API
	by Andrej Vujić

	Copyright © 2020 Andrej Vujić. All rights reserved.

	Anderj Vujić is not in any way affiliated with OLX.ba (OLX)
	nor their team.
"""

# Required imports:
from bs4 import BeautifulSoup # https://pypi.org/project/beautifulsoup4/
import requests # https://pypi.org/project/requests/
import subprocess # 

class Creator():
	# Class information
	def __init__(self):
		pass

	name = "Andrej"
	surname = "Vujić"
	full_name = "Andrej Vujić"

	email = "vujicandrej366@gmail.com"
	github = "https://github.com/andrejvujic/"
	instagram = "https://www.instagram.com/andrejvujic/"
	twitter = "https://twitter.com/AndrejVujic/"

class Project():
	# Project information
	def __init__(self):
		pass

	name = "olx_ba" # Package name

	date_created = "--> This project was started on 19/07/2020"
	language = "--> Language: English"
	programming_language = "--> Developed in: Python3 (100%)"
	dependencies = ("--> This project requires beautifulsoup4 and requests to run.\n"
		f"--> Run the following function for help: {name}.dependencies_help()")

	github = "https://github.com/andrejvujic/olx-api/"
	pypi = "<insert link here>"

	olx_link = "https://www.olx.ba/"

	installed_version = "0.1"
	release_dates = {"0.1": "14/08/20"}

def installed_version():
	# Project installed version
	return f"--> OLX.ba Python API {Project.installed_version}"

def latest_version():
	# Project latest version
	return Project.latest_version

def set_latest_version():
	# Set Project latest version
	Project.latest_version = get_package_version(Project.pypi)

def version_check():
	# Check for latest version
	if Project.installed_version != Project.latest_version:
		print(f"--> WARNING: You don't have the latest version ({Project.latest_version}) of this package.\n")

def info():
	# Project info
	return (f"--> Version: {Project.installed_version}\n"
	f"--> Creator: {Creator.full_name}\n"
	f"--> Project GitHub: {Project.github}\n"
	f"--> Creator GitHub: {Creator.github}\n"
	f"--> Creator E-Mail: {Creator.email}\n")

def info_dict():
	# Return project info as Python dictionary
	return {"version": Project.installed_version, "creator": Creator.full_name,
	"project_github": Project.github, "creator_github": Creator.github, "email": Creator.email}

def dependencies():
	# Return dependencies as Python dictionary
	dependencies = {"pip": {"version": get_package_version("https://pypi.org/project/pip/"), "link": "https://pypi.org/project/pip/"},
		"beautifulsoup4": {"version": get_package_version("https://pypi.org/project/beautifulsoup4/"), "link": "https://pypi.org/project/beautifulsoup4/"},
		"requests": {"version": get_package_version("https://pypi.org/project/requests/"), "link": "https://pypi.org/project/requests/"}}
	return dependencies

def dependencies_help():
	# Help for installing dependencies
	beautifulsoup_command = get_package_command("https://pypi.org/project/beautifulsoup4/")
	requests_command = get_package_command("https://pypi.org/project/requests/")
	pip_command = get_package_command("https://pypi.org/project/pip/")

	print("--> This project requires beautifulsoup4, and pip requests to run.\n"
		"--> To install these packages you will need pip (Python package installer)\n\n"

		"--> To install beautifulsoup4 type:\n"
		f">>> {beautifulsoup_command}\n"
		f"--> For more info visit: https://pypi.org/project/beautifulsoup4/\n\n"

		"--> To install requests type:\n"
		f">>> {requests_command}\n"
		f"--> For more info visit: https://pypi.org/project/requests/\n\n"

		"--> To install pip type:\n"
		f">>> {pip_command}\n"
		f"--> For more info visit: https://pypi.org/project/requests/\n")

		"--> You can also run the following code:\n"
		">>> import olx_ba as olx\n"
		">>> olx.install_dependencies()\n"

def install_dependencies():
	required = dependencies()
	for key in required.keys():
		print(f"--> Installing {key}...")
		get_package(key)
		print("\n")

def get_package(package):
	subprocess.call(['pip', 'install', package])
	# --> Prevents subprocess output: stdout = subprocess.PIPE

def get_package_version(url):
	# Get package version from PyPi (pypi.org)
	try:
		soup = get_soup(url)
		if soup:
			package_version = soup.find("h1", class_ = "package-header__name")
			package_version = package_version.text
			return package_version.split()[1].strip()

		else:
			return None

	except:
		return None
		
def get_package_command(url):
	# Get package pip command from PyPi (pypi.org)
	try:
		soup = get_soup(url)
		if soup:
			package_command = soup.find("span", id = "pip-command")
			package_command = package_command.text
			return package_command.strip()

		else:
			return None

	except:
		return None

def get_soup(url):
	# Get soup object from url
	response = requests.get(url)
	if response.status_code != 404:
		return BeautifulSoup(response.text, "lxml")

	else:
		return None

def get_session_soup(session, url):
	# Get soup object for session from url
	response = session.get(url)
	if response.status_code != 404:
		return BeautifulSoup(response.text, "lxml")

	else:
		return None

def get_cookies(session, url):
	# Get cookies for post request
	response = session.get(url)
	cookies = response.cookies
	return cookies

def get_headers():
	# Get headers for post request
	headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
	"X-Requested-With": "XMLHttpRequest",
	}
	return headers

def api_info():
	# API info
	print("Unofficial OLX.ba API\n"
		f"Version: {Project.installed_version}\n"
		f"Released on {Project.release_dates[Project.installed_version]}\n\n"
		"The developer of this API is not in any way affiliated with OLX.ba\n\n"
		"Copyright © 2020 Andrej Vujić. All rights reserved.\n")

def warning_message():
	# Warning message
	print("WARNING!\n"
		  "The creator of this unofficial API is not responsible\n"
		  "for any trouble you may get into by using this API.\n\n"
		  "UPOZORENJE!\n"
		  "Kreator ovog API-a nije odgovoran za potencijalne probleme\n"
		  "u koje mozete uci koristenjem ovog API-a.\n")

def to_number(string):
	# Convert price from string type to float type
	if string.upper() == "POKLON":
		return 0

	elif string.upper() == "PO DOGOVORU":
		return 0

	elif string.count("KM") == 1:
		string = string.strip()
		string = string.replace("KM", "").replace(".", "").replace(",", ".")
		string = float(string)
		return string

	elif string.count("KM") == 2:
		string = string[string.index("KM") + 2:]
		string = string.replace("KM", "").replace(".", "").replace(",", ".")
		string = string.strip()
		string = float(string)
		return string

	else:
		return None

def to_status(response):
	# Convert OLX.ba requests response to status only
	response = response.text
	response = response[1:response.index(",")]
	return response

def format_letters(text):
	# Convert keyboard codes to letters
	text = str(text)
	text = text.replace(r"\u", "u")

	key_codes = {"010c": "Č", "010d": "č", "0106": "Ć", "0107": "ć", "017d": "Ž", "017e": "ž", 
	"0110": "Đ", "0111": "đ", "0160": "Š", "0161": "š", "01c4": "Ǆ",}

	for key in key_codes.keys():
		if  f"u{key}" in text:
			text = text.replace(f"u{key}", key_codes[key])

	return text

class Url():
	# Urls
	def __init__(self):
		pass

	def __setattr__(self, name, value):
		print(f"--> You can't assign value {value} to {name}")

	homepage = "https://www.olx.ba/"
	login = "https://www.olx.ba/auth/login"

	send_message = "https://www.olx.ba/ajax/posaljiPoruku/"
	delete_message = "https://www.olx.ba/poruke/brisiPoruku/"
	mark_view_message = "https://www.olx.ba/poruke/oznacineprocitaneporuke"

	ad = "https://www.olx.ba/artikal/"
	ad_order = "https://www.olx.ba/artikal/zavrsi_dostavu/"
	ad_description = "https://www.olx.ba/artikal/detaljni_opis?id="
	ad_follow = "https://www.olx.ba/ajax/spasiArtikal?id="
	ad_public_message = "https://www.olx.ba/ajax/artikal/novoPitanje?art="

	block = "https://www.olx.ba/ajax/blokirajKorisnika/"
	follow = "https://www.olx.ba/ajax/pratiKorisnika/"
	olxcredit = "https://www.olx.ba/ajax/posaljiPikredit/"

	user_profile = "https://www.olx.ba/profil/"
	user_trust = "/povjerenje"
	user_active_ads = "/aktivni"
	user_sold_ads = "/zavrseni"
	user_messages = "https://www.olx.ba/poruke/"
	user_phonenumber = "https://www.olx.ba/ajax/brojTelefona/"
	user_information = "https://www.olx.ba/postavke"

	search = "https://www.olx.ba/pretraga?trazilica="

class OLX():
	# OLX class containing information about the logged in user
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.session = self.login()

		self.__dict__["MESSAGE_LIMIT"] = 10
		self.__dict__["messages_sent"] = 0

	def __setattr__(self, name, value):
		constants = ["MESSAGE_LIMIT"]

		if name in constants:
			print(f"--> Can't assign value {value} to {name}.")
			return

		elif name == "messages_sent":
			if value > self.messages_sent:
				self.__dict__[name] = value
			else:
				print(f"--> Can't assign value {value} to {name}.")
			return

		else:
			self.__dict__[name] = value
			return

	def get_csrf_token(self):
		csrf_token = self.soup.find("input", attrs = {"name": "csrf_token"})
		csrf_token = csrf_token.get("value")
		return csrf_token

	def get_login_PAYLOAD(self, csrf_token):
		PAYLOAD = {
		"username": self.username,
		"password": self.password,
		"csrf_token": csrf_token,
		"zapamtime": "off"
		}
		return PAYLOAD

	def login(self):
		soup = get_soup(Url.homepage)
		self.soup = soup

		csrf_token = self.get_csrf_token()
		PAYLOAD = self.get_login_PAYLOAD(csrf_token)

		session = requests.Session()
		response = session.get(Url.homepage)
		response = session.post(Url.login, data = PAYLOAD)
		return session

	def update_soup(self):
		soup = get_session_soup(self.session, Url.homepage)

		self.soup = soup
		return self.soup

	def get_information(self):
		# Get user information (for OLX delivery)
		soup = get_session_soup(self.session, Url.user_information)

		attribute_names = ["first_name", "last_name", "zip", "address", "phone_number", "email"]
		input_names = ["ime", "prezime", "zip", "adresa", "tel", "email"]

		try:
			dropdowns = []
			options = soup.findAll("option")
			for option in options:
				if "selected" in str(option):
					dropdowns.append(option.text.strip())

			self.city = dropdowns[1]

		except:
			self.information_guidelines(0)

		for index in range(len(attribute_names)):
			attribute = soup.find("input", attrs = {"name": input_names[index]})
			if attribute:
				attribute = attribute.get("value")
				if len(attribute) > 1:
					setattr(self, attribute_names[index], attribute)

				else:
					self.information_guidelines(0)
					
			else:
				self.information_guidelines(0)

		return

	def set_information(self, my_data):
		# Set user information (for OLX delivery)
		attribute_names = ["first_name", "last_name", "zip", "address", "phone_number", "email", "city"]
		for name in attribute_names:
			if name not in my_data.keys():
				self.information_guidelines(1)

		for key in my_data.keys():
			setattr(self, key, my_data[key])

	def information_guidelines(self, error_index):
		# Explain errors while setting information (for OLX delivery)
		if error_index == 0:
			print("\n--> Oops...Looks like your information isn't entered into OLX.\n"
				f"--> You can fill it out at {Url.user_information} or by adding the following\n"
				"code to your script:\n\n\n"
				"me = olx.OLX(your_username, your_password) # Create OLX object\n\n"
				"my_data = {'first_name': <your_firstname>, 'last_name': <your_lastname>,\n"
							"'address': <your_address>, 'city': <your_city>,\n"
							"'zip': <your_zip>, 'phone_number': <your_phonenumber>,\n"
							"'email': <your_email>}\n\n"
							"me.set_information(my_data) # Set OLX information\n\n")
		
		elif error_index == 1:
			print("\n--> Invalid information provided as <my_data> in set_information().\n"
				"--> Provided data must be a Python dictionary object with the following keys\n"
				"and corresponding values:\n\n"
				"'first_name', 'last_name', 'zip', 'address', 'phone_number', 'email'.\n\n")

		quit()

	def get_ad_number(self):
		# Get total number of Ads on OLX
		ad_number = self.soup.find("h1", class_ = "ch1")
		ad_number = ad_number.findAll("strong")
		ad_number = ad_number[0].text

		self.ad_number = ad_number
		return self.ad_number

	def get_category_number(self):
		# Get total number of Categories on OLX
		category_number = self.soup.find("h1", class_ = "ch1")
		category_number = category_number.findAll("strong")
		category_number = category_number[1].text

		self.category_number = category_number
		return self.category_number
	
	def get_olxcredit_number(self):
		# Get number of OLXcredit
		soup = self.update_soup()
		
		olxcredit_number = soup.find("ul", class_ = "nav profil")
		olxcredit_number = olxcredit_number.findAll("li")
		olxcredit_number = olxcredit_number[3].find("a")
		olxcredit_number = olxcredit_number.text.strip()

		self.olxcredit = olxcredit_number
		return self.olxcredit

	def get_unread_messages(self):
		# Get number of unread (private) messages
		soup = self.update_soup()

		unread_messages = soup.find("span", class_ = "notifikacija", id = "brojporuka")
		if unread_messages:
			unread_messages = unread_messages.text

		self.number_unread_messages = unread_messages

		unread_messages = []
		page = 0

		while True:
			page += 1
			soup = get_session_soup(self.session, Url.user_messages + f"?stranica={page}")

			user_messages = soup.findAll("li", class_ = lambda x: x and "novaporuka" in x)
			if user_messages:
				for index, message in enumerate(user_messages, start = 1):
					message_number = index + ((page - 1) * 20)

					message_title = message.find("p", class_ = "naslov")
					message_title = message_title.text.strip()

					message_id = message.get("data-id-poruka")

					unread_messages.append({"number": message_number, "title": message_title,
						"id": message_id, "link": Url.user_messages + f"k-{message_id}"})

			else:
				break

		if len(unread_messages) != 0:
			self.unread_messages = unread_messages

		else:
			self.unread_messages = None

		return self.unread_messages

	def get_all_messages(self):
		# Get all users messages
		all_messages = []
		page = 0

		while True:
			page += 1
			soup = get_session_soup(self.session, Url.user_messages + f"?stranica={page}")

			user_messages = soup.findAll("li", id = lambda x: x and "poruka" in x)
			if user_messages:
				for index, message in enumerate(user_messages, start = 1):
					message_number = index + ((page - 1) * 20)

					message_title = message.find("p", class_ = "naslov")
					message_title = message_title.text.strip()

					message_id = message.get("data-id-poruka")

					all_messages.append({"number": message_number, "title": message_title,
						"id": message_id, "link": Url.user_messages + f"k-{message_id}"})

			else:
				break

		if len(all_messages) != 0:
			self.all_messages = all_messages
			self.number_all_messages = len(all_messages)

		else:
			self.all_messages = None
			self.number_all_messages = 0

		return self.all_messages

	def mark_as_read(self, message_id):
		# Mark message as read/unread
		PAYLOAD = {
		"brisiporuke[]": message_id
		}

		response = self.session.post(Url.mark_view_message, data = PAYLOAD)
		return format_letters(response.text)

	def delete_message(self, message_id):
		# Delete message
		PAYLOAD = {
		"brisiporuke[]": message_id
		}

		response = self.session.post(Url.delete_message, data = PAYLOAD)
		return format_letters(response.text)


class Search():
	# Search class to interact with OLX.ba Search
	def __init__(self, host, search_term, category = 0, pages = 1, sort_by = "datum"):
		self.host = host
		self.session_username = host.username
		self.session_password = host.password
		self.session = host.session

		self.search_term = search_term
		self.category = category
		self.pages = pages

		self.results = self.get_search_results()

	def get_search_results(self):
		results_list = []

		for page in range(self.pages):
			self.soup = get_session_soup(self.session, f"{Url.search}{self.search_term}&stranica={page + 1}&kategorija={self.category}")

			if self.has_results():
				results = self.soup.find("div", id = "rezultatipretrage")
				results = results.findAll("div", class_ = lambda x: x and "listitem" in x)

				for result in results:
					result_link = result.find("div", class_ = "naslov")
					try:
						result_link = result_link.find("a")
						if result_link:
							result_link = result_link.get("href")
							results_list.append(result_link)

					except:
						pass

			else:
				continue

		return results_list

	def has_results(self):
		results = self.soup.find("div", id = "rezultatipretrage")
		results = results.findAll("div", class_ = lambda x: x and "listitem" in x)
		return True if len(results) > 0 else False

class User():
	# User class to interact with other Users and their Ads
	def __init__(self, host, username):
		self.username = username
		self.url = Url.user_profile + username

		self.host = host
		self.session_username = host.username
		self.session_password = host.password
		self.session = host.session

		self.soup = get_session_soup(self.session, self.url)
		self.valid = self.exists()

	def exists(self):
		# Check if User exists
		response = self.session.get(self.url)

		if response.status_code == 404:
			return False
		else:
			return True

	def get_trust(self):
		# Get Users trust percent
		if not self.exists():
			return None

		user_trust = self.soup.find("div", class_ = lambda x: x and "povjerenje_procenat" in x)

		self.trust_message = user_trust.get("title")
		self.trust = user_trust.text.strip()

		if len(self.trust) == 0:
			self.trust = None

		return self.trust

	def get_impressions(self):
		# Get impressions from Users profile
		if not self.exists():
			return None

		soup = get_session_soup(self.session, self.url + Url.user_trust)

		number_different_users = soup.find("ul", class_ ="nav nav-tabs")
		number_different_users = number_different_users.findAll("li")
		number_different_users = number_different_users[3].text
		number_different_users = number_different_users[:number_different_users.index(" ")]
		number_different_users = number_different_users.replace("\n", "").replace("\t", "")

		user_impressions = soup.find("div", id = "profil_main")
		user_impressions = user_impressions.findAll("div", class_ = "op")
		impression_list = []

		for impression in user_impressions:
			impression = impression.find("p", class_ = "", style = lambda x: x and x)
			impression_list.append(impression.text)

		try:
			self.positive = impression_list[0]
			self.neutral = impression_list[1]
			self.negative = impression_list[2]
			self.impressions_different_users = number_different_users

		except:
			self.positive = 0
			self.neutral = 0
			self.negative = 0
			self.impressions_different_users = 0

		self.impressions = {"positive": self.positive, "neutral": self.neutral, "negative": self.negative, "different_users": number_different_users}

		return self.impressions

	def get_impressions_messages(self):
		# Get impression messages from Users profile
		if not self.exists():
			return None

		try:
			impressions = [self.positive, self.neutral, self.negative]
			for index, impression in enumerate(impressions):
				impressions[index] = int(impression)

			max_page = int(sum(impressions) / 20) + 1

		except:
			self.get_impressions()
			return self.get_impressions_messages()

		impressions_messages = []
		for page in range(max_page):
			soup = get_session_soup(self.session, self.url + Url.user_trust + f"?stranica={page + 1}")

			all_messages = soup.findAll("div", class_ = "pitanje_d")
			for index, message in enumerate(all_messages, start = 1):

				message_number = page * 20 + index

				message_type = message.find("div", class_ = "autor_ikona").find("div")
				message_type = message_type.text.strip().replace("\n", "").replace("\t", "")

				message_username = message.find("div", class_ = "username").find("span")
				message_username = message_username.text.strip().replace("\n", "").replace("\t", "")

				message_date = message.find("div", class_ = "pitanje_datum")
				message_date = message_date.text.strip().replace("\n", "").replace("\t", "")

				message_textinfo = message.find("div", class_ = "pitanje_tekst")
				message_textinfo = message_textinfo.text.replace("\n", "")

				message_text = message_textinfo[message_textinfo.index("\t"):].strip().replace("\n", "").replace("\t", "")
				message_ad_title = message_textinfo[:message_textinfo.index("\t")].strip().replace("\n", "").replace("\t", "")

				if "Detalji transakcije su sakriveni" in message_text:
					message_text = message_text.replace("Detalji transakcije su sakriveni", "")
					message_ad_title = "Detalji transakcije su sakriveni"

				message_dict = {"number": message_number, "transaction_type": message_type, "username": message_username, "date": message_date,
					"text": message_text, "ad_title": message_ad_title}
				impressions_messages.append(message_dict)

		if len(impressions_messages) != 0:
			self.impressions_messages = impressions_messages

		else:
			self.impressions_messages = None

		return self.impressions_messages

	def get_information(self):
		# Get Users information
		if not self.exists():
			return None

		user_information = self.soup.findAll("div", class_ = "span2")

		self.avatar = user_information[1].find("div", class_ = "op profil slikaavatarlogo")
		if self.avatar:
			self.avatar = self.avatar.find("img")
			self.avatar = self.avatar.get("src")
		else:
			self.avatar = None

		user_information = user_information[1].findAll("div", class_ = "op profil")
		information_list = []

		for index, information in enumerate(user_information):
			information = information.find("p", style = lambda x: x and x)
			if information:
				information_list.append(information.text.strip())

			else:
				information = user_information[index].find("p", class_ = "n")
				information_list.append(information.text.strip())

		self.last_online = information_list[0]
		self.location = information_list[1]
		self.registration_date = information_list[2]
		self.id = information_list[3]

		self.information = {"username:": self.username, "url": self.url, "last_online": self.last_online, "location": self.location,
		"avatar:": self.avatar, "registration_date": self.registration_date, "id": self.id}
		return self.information

	def get_conversations(self):
		# Get conversations with User
		if not self.exists():
			return None

		try:
			soup = get_session_soup(self.session, Url.user_messages + "u-" + self.id)

		except:
			self.get_information()
			return self.get_conversations()

		user_messages = soup.findAll("li", id = lambda x: x and "poruka" in x)
		messages_list = []

		if user_messages:
			for index, message in enumerate(user_messages, start = 1):
				message_number = index

				message_title = message.find("p", class_ = "naslov")
				message_title = message_title.text.strip()

				message_id = message.get("data-id-poruka")

				messages_list.append({"number": message_number, "title": message_title,
					"id": message_id, "link": Url.user_messages + f"k-{message_id}"})

			self.conversations = messages_list
			return self.conversations

		else:
			self.conversations = None
			return self.conversations

	def get_medals(self):
		# Get Users medals
		if not self.exists():
			return None

		user_medals = self.soup.find("div", id = "medaljesve")
		user_medals = user_medals.findAll("div", class_ = lambda x: x and "medaljaprofil" in x)
		medal_list = []

		for index, medal in enumerate(user_medals):
			medal = medal.get("title")
			if "dostava" in medal:
				self.olx_deliveries = user_medals[index].text

			medal_list.append(medal)

		self.medals = medal_list
		return self.medals

	def get_transaction_medal(self):
		# Get Users transaction medal (for number of transactions)
		if not self.exists():
			return None

		try:
			user_transaction_medal = self.soup.find("div", class_ = lambda x: x and "profil_medalja" in x)
			user_transaction_medal = user_transaction_medal.get("title")
			user_transaction_medal = user_transaction_medal.replace("<br", "").replace("strong", "").replace("<", "").replace(">", "").replace("/", "")

			self.transaction_medal = user_transaction_medal
			return self.transaction_medal

		except:
			self.transaction_medal = None
			return self.transaction_medal

	def get_active_ads(self):
		# Get Users currently active Ads
		if not self.exists():
			return None

		soup = get_session_soup(self.session, self.url + Url.user_active_ads)
		user_active_ads = soup.find("div", class_ = "span8")
		user_active_ads = user_active_ads.find("div", class_ = "desno", id = "desno")
		active_ads = []

		max_page = user_active_ads.find("div", class_ = "disableSelection")
		max_page = max_page.find("h4")
		max_page = max_page.findAll("b")

		if int(max_page[1].text) != 0:
			max_page = int(int(max_page[1].text) / 20) + 1

		else:
			self.active_ads = None
			return self.active_ads
		
		for page in range(max_page):
			soup = get_session_soup(self.session, self.url + Url.user_active_ads + f"?stranica={page + 1}")

			all_ads = soup.findAll("div", class_ = lambda x: x and "listitem" in x)
			for index, ad in enumerate(all_ads, start = 1):

				ad_number = page * 20 + index
				ad_link = ad.find("a")
				ad_link = ad_link.get("href")

				ad_location = ad.find("div", class_ = "lokacijadiv")
				ad_location = ad_location.text.strip()

				ad_title = ad.find("p", class_ = "na")
				ad_title = ad_title.text.strip()

				ad_description = ad.find("div", class_ = "pna")
				ad_description = ad_description.text.strip()

				ad_price = ad.find("div", class_ = "datum")
				ad_price = ad_price.find("span")
				ad_price = ad_price.text.strip()
				ad_price = to_number(ad_price)
				
				ad_date = ad.find("div", class_ = "kada")
				ad_date = ad_date.get("data-cijelidatum")

				ad_state = ad.find("div", class_ = lambda x: x and "stanje" in x)
				ad_state = ad_state.find("span", class_ = "nko")
				if ad_state:
					ad_state = ad_state.text

				else:
					ad_state = ad.find("div", class_ = lambda x: x and "stanje" in x)
					ad_state = ad_state.get("class")
					if ad_state == "stanje k":
						ad_state ="KORIŠTENO"

					else:
						ad_state = "NOVO"

				ad = {"number": ad_number,"link": ad_link, "title": ad_title, "location": ad_location, "description": ad_description,
					"price": ad_price, "date": ad_date, "state": ad_state}
				active_ads.append(ad)

		self.active_ads = active_ads
		return active_ads

	def get_sold_ads(self):
		# Get Ads the User sold in the past
		if not self.exists():
			return None

		soup = get_session_soup(self.session, self.url + Url.user_sold_ads)
		user_sold_ads = soup.find("div", class_ = "goretabs")
		user_sold_ads = user_sold_ads.findAll("li", class_ = "dd disableSelection")
		user_sold_ads = user_sold_ads[2].find("span", class_ = "brojpitanja hide-mobile")
		user_sold_ads = user_sold_ads.text
		sold_ads = []

		if int(user_sold_ads) != 0:
			max_page = int(int(user_sold_ads) / 20) + 1

		else:
			self.sold_ads = 0
			return self.sold_ads

		for page in range(max_page):
			soup = get_session_soup(self.session, self.url + Url.user_sold_ads + f"?stranica={page + 1}")

			all_ads = soup.findAll("div", class_ = lambda x: x and "listitem" in x)
			for index, ad in enumerate(all_ads, start = 1):

				ad_number = page * 20 + index
				ad_link = ad.find("a")
				ad_link = ad_link.get("href")

				ad_title = ad.find("p", class_ = "na")
				ad_title = ad_title.text.strip()

				ad_description = ad.find("div", class_ = "pna")
				ad_description = ad_description.text.strip()

				ad_price = ad.find("div", class_ = "datum")
				ad_price = ad_price.find("span")
				ad_price = ad_price.text.strip()
				ad_price = to_number(ad_price)
				
				ad_date = ad.find("div", class_ = "kada")
				ad_date = ad_date.get("data-cijelidatum")

				ad_state = ad.find("div", class_ = lambda x: x and "stanje" in x)
				ad_state = ad_state.find("span", class_ = "nko")
				if ad_state:
					ad_state = ad_state.text

				else:
					ad_state = ad.find("div", class_ = lambda x: x and "stanje" in x)
					ad_state = ad_state.get("class")
					if ad_state == "stanje k":
						ad_state ="KORIŠTENO"

					else:
						ad_state = "NOVO"

				ad = {"number": ad_number,"link": ad_link, "title": ad_title, "description": ad_description,
					"price": ad_price, "date": ad_date, "state": ad_state}
				sold_ads.append(ad)

		self.sold_ads = sold_ads
		return self.sold_ads

	def get_phonenumber(self):
		# Get users phone number
		# This data can publicly be viewed on OLX.ba
		if not self.exists():
			return None

		soup = get_session_soup(self.session, Url.user_phonenumber + self.username)

		user_phonenumber = soup.find("div", id = "porukamodal-content")
		user_phonenumber = user_phonenumber.find("b")
		if user_phonenumber:
			user_phonenumber = user_phonenumber.text

		self.phonenumber = user_phonenumber
		return self.phonenumber

	def send_message(self, message):
		# Send a message to the User
		if not self.exists():
			return None

		if self.host.messages_sent < self.host.MESSAGE_LIMIT:
			self.host.messages_sent += 1

		else:
			print("--> Message limit reached.")
			return

		try:
			if self.id:
				pass

		except:
			self.get_information()

		print(self.host.messages_sent)
		PAYLOAD = {
		"user_id": self.id,
		"tekst_poruke": message
		}

		response = self.session.post(Url.send_message, data = PAYLOAD)
		return format_letters(response.text)

	def send_olxcredit(self, quantity):
		# Send OLXcredit to the User
		if not self.exists():
			return None

		try:
			if self.id:
				pass

		except:
			self.get_information()

		PAYLOAD = {
		"id": self.id,
		"kolicina": quantity,
		"password": self.session_password,
		"password2": self.session_password
		}

		response = self.session.post(Url.olxcredit, data = PAYLOAD)
		return format_letters(response.text)

	def block(self):
		# Block the User
		if not self.exists():
			return None

		response = self.session.get(Url.block + self.username)
		return format_letters(response.text)

	def follow(self):
		# Follow the User (save the profile)
		if not self.exists():
			return None

		response = self.session.get(Url.follow + self.username)
		return format_letters(response.text)

class Ad():
	# Ad class to interact with Ads
	def __init__(self, host, ad_link):
		self.host = host
		self.session_username = host.username
		self.session_password = host.password

		self.link = ad_link
		self.id = self.get_id()
		self.update_soup()
		self.seller = self.get_seller()

		self.confirm = True
		self.exists = self.exists()

	def update_soup(self):
		# Update Ad soup object
		self.soup = get_soup(self.link)

	def exists(self):
		# Check if Ad exists
		response = self.host.session.get(self.link)

		if response.status_code == 404:
			return False
		else:
			return True

	def get_id(self):
		# Get Ad id
		url = self.link

		url = url[::-1]
		url = url[:url.index("//:sptth")]
		url = url[::-1]
		ad_id = url.split("/")[2]
		return ad_id

	def get_seller(self):
		# Get Ad seller
		if not self.exists:
			return None

		ad_seller = self.soup.find("div", class_ = "vrsta1 vrsta_desno")
		ad_seller = ad_seller.find("div", class_ = "username")
		ad_seller = ad_seller.find("span")
		if ad_seller:
			ad_seller = ad_seller.text.strip()

			self.seller = ad_seller
			return self.seller

		else:
			self.seller = None
			return self.seller

	def get_title(self):
		# Get Ad title
		if not self.exists:
			return None

		ad_title = self.soup.find("span", id = "naslovartikla")
		if ad_title:
			ad_title = ad_title.text.strip()

			self.title = ad_title
			return self.title

		else:
			self.title = None
			return self.title

	def get_price(self):
		# Get Ad price
		if not self.exists:
			return None

		ad_price = self.soup.find("div", class_ = lambda x: x and "cijena" in x)
		if ad_price:
			ad_price = ad_price.findAll("p")[1]
			ad_price = ad_price.text.strip()
			ad_price = to_number(ad_price)

			self.price = ad_price
			return self.price

		else:
			ad_price = self.soup.find("div", class_ = "op pop")
			ad_price = ad_price.find("p")
			if ad_price:
				ad_price = ad_price.text.strip()
				ad_price = to_number(ad_price)

				self.price = ad_price
				return self.price

			else:
				self.price = None
				return self.price

	def get_state(self):
		# Get Ad state (new or used)
		if not self.exists:
			return None

		ad_state = self.soup.find("div", class_ = lambda x: x and "stanje" in x)
		ad_state = ad_state.findAll("p")[1]
		if ad_state:
			ad_state = ad_state.text.strip()

			self.state = ad_state
			return self.state

		else:
			self.state = None
			return self.state

	def get_location(self):
		# Get Ad location (where the item is located)
		if not self.exists:
			return None

		ad_location = self.soup.find("div", class_ = lambda x: x and "lokacija" in x)
		ad_location = ad_location.findAll("p")[1]
		if ad_location:
			ad_location = ad_location.text.strip()

			self.location = ad_location
			return self.location

		else:
			self.location = None
			return self.location

	def get_detailed_information(self):
		# Get Ads detailed information
		if not self.exists:
			return None

		ad_detailed_information = self.soup.findAll("div", class_ = "df")
		detailed_information = {}

		if ad_detailed_information:
			for info in ad_detailed_information:
				title = info.find("div", class_ = lambda x: x and "df1" in x)
				title = title.text.strip().lower().replace(" ", "_")
				title = title.replace(".", "").replace("(", "").replace(")", "")

				value = info.find("div", class_ = lambda x: x and "df2" in x)
				value = value.text.strip()
				value = value if len(value) != 0 else "Da"
			
				detailed_information[title] = value

			detailed_information["zamjena"] = self.get_exchange_status()

			self.detailed_information = detailed_information

		else:
			self.detailed_information = None

		return self.detailed_information

	def get_description(self):
		# Get Ad description
		if not self.exists:
			return None

		ad_description = self.soup.findAll("div", class_ = lambda x: x and "detaljniopis" in x)

		iframe = get_soup(f"{Url.ad_description}{self.get_id()}")
		ad_iframe_description = iframe.find("div", id = "detaljniopis_iframe_sadrzaj")

		if ad_description:
			desc_short = ad_description[0]
			if not ad_iframe_description:
				desc_long = ad_description[1].findChildren(recursive = True)

			else:
				desc_long = ad_iframe_description.findChildren(recursive = True)

			if desc_short:
				ad_short_description = desc_short.text.replace("\n", "").replace("\t", "").strip()

			else:
				ad_short_description = None

			if desc_long:
				title_long = ""
				text = ""

				for child in desc_long:
					text = f"{text} {self.get_child_content(child)}"

				text = text.strip()
				ad_long_description = " ".join(text.split())

			ad_description = {}
			ad_description["short_description"] = ad_short_description
			ad_description["long_description"] = ad_long_description

			self.description = ad_description

		else:
			self.description = None

		return self.description

	def get_child_content(self, element):
		# Get description child element text
		if not self.exists:
			return None

		text = ""
	
		element = str(element)
		element = element.replace("<br/>", " ")
		element = BeautifulSoup(element, "lxml")

		child_text = element.text.replace("\n", " ").replace("\t", "").strip()
		text = f"{text} {child_text}"

		return text

	def get_exchange_status(self):
		# Get exchange status (does the seller want to exchange the item for something else)
		if not self.exists:
			return None

		try:
			ad_exchange = self.soup.find("i", class_ = lambda x: x and "exchange" in x)
			ad_exchange = ad_exchange.parent.parent
			ad_exchange = ad_exchange.find("div", class_ = lambda x: x and "alert" in x)
			ad_exchange = ad_exchange.text

		except:
			# For 
			ad_exchange = self.soup.findAll("div", class_ = "artikal_kat")
			if ad_exchange:
				ad_exchange = ad_exchange[-1].text.strip().replace("\n", "").replace("\t", "")
				ad_exchange = format_letters(ad_exchange)

		self.exchange = ad_exchange
		return self.exchange

	def has_olx_delivery(self):
		# Check if the Ad has OLX delivery
		if not self.exists:
			return None

		ad_order = self.soup.find("div", class_ = lambda x: x and "dostava" in x)
		if ad_order:
			self.olx_delivery = True

		else:
			self.olx_delivery = False

		return self.olx_delivery

	def has_free_delivery(self):
		# Check if the Ad has free delivery
		if not self.exists:
			return None

		if self.has_olx_delivery():
			ad_delivery_free = self.soup.find("div", class_ = lambda x: x and "dostava" in x)
			ad_delivery_fre = ad_delivery_free.find("p")
			if ad_delivery_free:
				self.free_delivery = True

			else:
				self.free_delivery = False

		else:
			self.free_delivery = False

		return self.free_delivery

	def order(self):
		# Order the Ad (the item will be shipped to your address)
		if not self.exists:
			return None

		if self.has_olx_delivery():
			try:
				PAYLOAD = {
				"vrsta_dostave": "2" if self.has_free_delivery() else "12",
				"ime": f"{self.host.first_name} {self.host.last_name}",
				"adresa": self.host.address,
				"grad": self.host.city,
				"zip": self.host.zip,
				"tel": self.host.phone_number,
				"poruka": "",
				"email": self.host.email,
				"artikal_id": self.id,
				"kupac_id": User(self.host, self.session_username).get_information()["id"],
				"prodavac_id": User(self.host, self.seller).get_information()["id"],
				"potrvda": "on"
				}
			
			except:
				self.host.get_information()
				return self.order()

			if self.confirm:
				print(f"--> By performing this action you agree to pay {self.get_price()}KM (+ possible shipping costs) upon delivery.")
				print("--> Are you sure you want to proceed? y/n")

				if input(">>> ").lower() == "n":
					return None

			response = self.host.session.post(Url.ad_order + self.id, cookies = get_cookies(self.host.session, Url.ad_order + self.id),
				data = PAYLOAD, headers = get_headers())
			return format_letters(response.text)

	def send_message(self, message):
		# Send a message to the seller regarding the Ad
		if not self.exists:
			return None

		if self.host.messages_sent < self.host.MESSAGE_LIMIT:
			self.host.messages_sent += 1

		else:
			print("--> Message limit reached.")
			return

		PAYLOAD = {
		"art_id": self.get_id(),
		"tekst_poruke": message
		}

		response = self.host.session.post(Url.send_message, data = PAYLOAD)
		return format_letters(response.text)

	def send_public_message(self, message):
		# Send a public message to the seller regarding the Ad
		if not self.exists:
			return None

		if self.host.messages_sent < self.host.MESSAGE_LIMIT:
			self.host.messages_sent += 1

		else:
			print("--> Message limit reached.")
			return

		PAYLOAD = {
		"pitanje_tekst": message
		}		

		response = self.host.session.post(f"{Url.ad_public_message}{self.get_id()}", data = PAYLOAD)
		return format_letters(response.text)

	def follow(self):
		# Follow the Ad (save the Ad)
		if not self.exists:
			return None

		response = self.host.session.get(f"{Url.ad_follow}{self.get_id()}")
		return format_letters(response.text)

if __name__ == "olx_ba":
	Creator = Creator()
	Project = Project()
	Url = Url()

	set_latest_version()
	warning_message()
	version_check()