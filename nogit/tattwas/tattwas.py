from requests import get
from bs4 import BeautifulSoup
from urllib3 import disable_warnings
def add_tattwa_cycle(time:list):
    hour = int(time[0])
    min = int(time[1]) + 24
    if min >=60:
        hour += 1
        min = min - 60
    return {"initial":time,"endtime":[hour,min]}
disable_warnings()
GOOGLE_SUNRISE_URL = "https://www.datosmundial.com/america/mexico/puesta-del-sol.php"
page =get(GOOGLE_SUNRISE_URL,verify=False)
soup = BeautifulSoup(page.content,"html.parser")
mydivs = soup.find_all("table", {"class": "std100 hover"})
for td in mydivs[0]:
    time = td.text
    if "Ciudad de México" in time:
        time = time.split("am")[0].split("ico")[1].strip().split(":")
        time = [int(time[0]),int(time[1])]
        break
times =  {"endtime":time}
while times['endtime'][0]  <= 23:
    times = add_tattwa_cycle(times["endtime"])
    print(f"Akash is from {times['initial'][0]}:{times['initial'][1]} to {times['endtime'][0]}:{times['endtime'][1]}")
    times = add_tattwa_cycle(times["endtime"])
    print(f"Vayu is from {times['initial'][0]}:{times['initial'][1]} to {times['endtime'][0]}:{times['endtime'][1]}")
    times = add_tattwa_cycle(times["endtime"])
    print(f"Texas is from {times['initial'][0]}:{times['initial'][1]} to {times['endtime'][0]}:{times['endtime'][1]}")
    times = add_tattwa_cycle(times["endtime"])
    print(f"                 Prithvi is from {times['initial'][0]}:{times['initial'][1]} to {times['endtime'][0]}:{times['endtime'][1]}")
    times = add_tattwa_cycle(times["endtime"])
    print(f"Apas is from {times['initial'][0]}:{times['initial'][1]} to {times['endtime'][0]}:{times['endtime'][1]}")  
 
