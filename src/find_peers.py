import requests
import curses
import json
import os

# Colors class for terminal colors
class Colors:
	HEADER = '\033[95m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

# Collect user input for API credentials
UID = "u-s4t2ud-4ec846675c48e7bf0bd2d48717ebcb0bf1f4d47746a0fb33e25bcab80f6e22d5"
SECRET = "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"
os.system("clear")

def set_terminal_size(rows, cols):
    curses.setupterm()
    curses.tputwinsize(0, rows, cols)

set_terminal_size(100, 40)

# welcome message part
def welcome_message():

	ascii_art = """
			▄█░ █▀▀█ █▀▀█ ▀▀▀█  █▀▀ ░▀░ █▀▀▄ █▀▀▄  █▀▀█ █▀▀ █▀▀ █▀▀█ █▀▀ 
			░█░ ░░▀▄ ░░▀▄ ░░█░  █▀▀ ▀█▀ █░░█ █░░█  █░░█ █▀▀ █▀▀ █▄▄▀ ▀▀█ 
			▄█▄ █▄▄█ █▄▄█ ░▐▌░  ▀░░ ▀▀▀ ▀░░▀ ▀▀▀░  █▀▀▀ ▀▀▀ ▀▀▀ ▀░▀▀ ▀▀▀ ᴮʸ ᴷᴵᴿᴬ
	"""

	print(Colors.FAIL + ascii_art + Colors.ENDC)
	print(Colors.BOLD + Colors.GREEN + "\t\t\t\t\t  Welcome to 1337 Find Peers" + Colors.ENDC)
	print(Colors.BOLD + Colors.GREEN + "\t\t\t\t\t  --------------------------" + Colors.ENDC)
	print("\n\033[3mThis script will help you find peers for your project.")
	print("------------------------------------------------------\n")
	print(Colors.ENDC + "You can report any issue to me in:")
	print("----------------------------------")
	print(Colors.BLUE + "Github:" + Colors.ENDC + f" https://github.com/kirazizi")
	print(Colors.BLUE + "Discord:" + Colors.ENDC + f" https://discord.com/users/655890569846980608")
	print("\nPlease press Enter to continue.")
	try:
		input()
	except:
		print(Colors.FAIL + "\nYou interrupted the script. Goodbye!\n")
		exit()


welcome_message()
os.system("clear")

# campus selection part
def select_campus():
	print(Colors.BOLD + Colors.GREEN + "Choose your campus:" + Colors.ENDC)
	print("1: Khouribga")
	print("2: Benguerir")
	print("3: Tétouan")
	try:
		campus_code = input("Enter your choice: ")
	except:
		print(Colors.FAIL + "\nYou interrupted the script. Goodbye!\n")
		exit()
	if campus_code == "1":
		return 16
	elif campus_code == "2":
		return 21
	elif campus_code == "3":
		return 55
	else:
		print(Colors.WARNING + "Wrong input. Please select a valid option.")
		return select_campus()

campus_filter = select_campus()
os.system("clear")

# the project selection part
def select_project():
	project_mapping = {
		"1": ["libft", "42cursus-libft"],
		"2": ["get_next_line", "42cursus-get_next_line"],
		"3": ["ft_printf", "42cursus-ft_printf"],
		"4": ["born2beroot", "born2beroot"],
		"5": ["so_long", "so_long"],
		"6": ["fdf", "42cursus-fdf"],
		"7": ["fract-ol", "42cursus-fract-ol"],
		"8": ["minitalk", "minitalk"],
		"9": ["pipex", "pipex"],
		"10": ["push_swap", "42cursus-push_swap"],
		"11": ["minishell", "42cursus-minishell"],
		"12": ["philosophers", "42cursus-philosophers"],
		"13": ["cub3d", "cub3d"],
		"14": ["miniRT", "miniRT"],
		"15": ["netpractice", "netpractice"],
		"16": ["CPP", "CPP"],
		"17": ["webserv", "webserv"],
		"18": ["ft_irc", "ft_irc"],
		"19": ["inception", "inception"],
		"20": ["ft_transcendence", "ft_transcendence"]
	}

	print(Colors.BOLD + Colors.GREEN + "Choose your project:" + Colors.ENDC)
	for key, values in project_mapping.items():
		print(f"{key}: {values[0]}")
	try:
		project_code = input("Enter your choice: ")
	except:
		print(Colors.FAIL + "\nYou interrupted the script. Goodbye!\n")
		exit()
	if project_code in project_mapping:
		return project_mapping[project_code][1]

	print(Colors.WARNING + "Wrong input. Please select a valid option.")
	return select_project()


not_yet = "CPP"

select_project = select_project()
os.system("clear")
if select_project in not_yet:
	print(Colors.FAIL + "Sorry, this project is not supported yet.")
	exit()

# status selection part
def select_status():
	print(Colors.BOLD + Colors.GREEN + "Choose your status:" + Colors.ENDC)
	print("1: waiting_for_correction")
	print("2: in_progress")
	print("3: finished")
	try:
		status_code = input("Enter your choice: ")
	except:
		print(Colors.FAIL + "\nYou interrupted the script. Goodbye!\n")
		exit()
	if status_code == "1":
		return "waiting_for_correction"
	elif status_code == "2":
		return "in_progress"
	elif status_code == "3":
		return "finished"
	else:
		print(Colors.WARNING + "Wrong input. Please select a valid option.")
		return select_status()

compus_status = select_status()
os.system("clear")

# API request part
BASE_API = "https://api.intra.42.fr/"

token_url = f"{BASE_API}oauth/token"
token_data = {
	'grant_type': 'client_credentials',
	'client_id': UID,
	'client_secret': SECRET,
}
token_r = requests.post(token_url, data=token_data)
token = token_r.json().get('access_token')

endpoint = f"/v2/projects/{select_project}/projects_users"

params = {
	'filter[campus]': campus_filter,
	'filter[status]': compus_status
}

headers = {
	'Authorization': f'Bearer {token}',
}
response = requests.get(f"{BASE_API}{endpoint}", headers=headers, params=params)

def filter_projects_by_pool_year(projects_users, target_year="2021"):
	filtered_entries = [
		entry for entry in projects_users 
		if entry.get('user', {}).get('pool_year') == target_year
	]
	return filtered_entries

if response.status_code == 200:
	projects_users = response.json()
	filtered_data = filter_projects_by_pool_year(projects_users)

	print(Colors.GREEN + f"----------- Peers {compus_status} on {select_project} 2021 -----------\n" + Colors.ENDC)
	for entry in filtered_data:
		user_info = entry.get('user', {})
		login = user_info.get('login', 'N/A')
		full_name = user_info.get('usual_full_name', 'N/A')
		intra_link = f"https://profile.intra.42.fr/users/{login}"

		print(Colors.BLUE + f"- Login:" + Colors.ENDC + f" {login}")
		print(Colors.BLUE + f"- Full name:" + Colors.ENDC + f" {full_name}")
		print(Colors.BLUE + f"- Intra Link:" + Colors.ENDC + f" {intra_link}")
		print("---------------------------------------------------------------")

	filtered_data = filter_projects_by_pool_year(projects_users, target_year="2022")
	print(Colors.GREEN + f"----------- Peers {compus_status} on {select_project} 2022 -----------\n" + Colors.ENDC)
	for entry in filtered_data:
		user_info = entry.get('user', {})
		login = user_info.get('login', 'N/A')
		full_name = user_info.get('usual_full_name', 'N/A')
		intra_link = f"https://profile.intra.42.fr/users/{login}"

		print(Colors.BLUE + f"- Login:" + Colors.ENDC + f" {login}")
		print(Colors.BLUE + f"- Full name:" + Colors.ENDC + f" {full_name}")
		print(Colors.BLUE + f"- Intra Link:" + Colors.ENDC + f" {intra_link}")
		print("---------------------------------------------------------------")
	
	filtered_data = filter_projects_by_pool_year(projects_users, target_year="2023")
	print(Colors.GREEN + f"----------- Peers {compus_status} on {select_project} 2023 -----------\n" + Colors.ENDC)
	for entry in filtered_data:
		user_info = entry.get('user', {})
		login = user_info.get('login', 'N/A')
		full_name = user_info.get('usual_full_name', 'N/A')
		intra_link = f"https://profile.intra.42.fr/users/{login}"

		print(Colors.BLUE + f"- Login:" + Colors.ENDC + f" {login}")
		print(Colors.BLUE + f"- Full name:" + Colors.ENDC + f" {full_name}")
		print(Colors.BLUE + f"- Intra Link:" + Colors.ENDC + f" {intra_link}")
		print("---------------------------------------------------------------")
else:
	print(Colors.FAIL + f"Error: Unable to fetch data (Status code: {response.status_code})")
	print(response.text + Colors.ENDC)
