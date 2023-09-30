#urllib
from os import write
import requests
from bs4 import BeautifulSoup

cookies = {
    '__ddg1_': '7QxzneL01PxAHpUTWPxt',
    '_xsrf': 'afee479ee0262c5853661924da9c55f1',
    'hhuid': 'S69WessL!zyJWWTs7OEz5Q--',
    'display': 'desktop',
    'crypted_hhuid': '6929BFF62FBA62676351A047F64BFCCF8ABD8824989FCDC5DF02F456F1BB61FF',
    'GMT': '3',
    'tmr_lvid': '29d240a7f7747d7eff2a7becf10b6a6c',
    'tmr_lvidTS': '1693248753024',
    '_ga': 'GA1.2.972042572.1693248753',
    '_ym_uid': '1693248754361358126',
    '_ym_d': '1693248754',
    'iap.uid': 'de7802753fb14412808f236fe6ede678',
    'hhul': 'dd54cbcab12dc1df8c915916676b4782676bc65aa5a35c5e951af0a77cbfa74e',
    '_gid': 'GA1.2.1206820436.1695563430',
    'regions': '2',
    '_ym_isad': '2',
    '_ym_visorc': 'w',
    '__zzatgib-w-hh': 'MDA0dC0jViV+FmELHw4/aQsbSl1pCENQGC9LX3VaQCBTZXpcInhdU3oqHxkxaytRDj1gPncqMV4/ZSUaOVURCxIXRF5cVWl1FRpLSiVueCplJS0xViR8SylEW1Z+Lh0VeXQsUg8TVy8NPjteLW8PKhMjZHYhP04hC00+KlwVNk0mbjN3RhsJHlksfEspNRF+fSVMFncpVFIQQRlyQ3V8XW1mJmZLXyB4VVQ0WkwaNHElCw4MXEEzaWVpcC9gIBIlEU1HGEVkW0I2KBVLcU8cenZffSpBbiJoS10hTF5QCSkVe0M8YwxxFU11cjgzGxBhDyMOGFgJDA0yaFF7CT4VHThHKHIzd2UxPm4lZkxfIDVRP0FaW1Q4NmdBEXUmCQg3LGBwVxlRExpceEdXeisiFghvJ1EQFF5FR2llbQwtUlFRS2IPHxo0aQteTA==weCL2w==',
    '__zzatgib-w-hh': 'MDA0dC0jViV+FmELHw4/aQsbSl1pCENQGC9LX3VaQCBTZXpcInhdU3oqHxkxaytRDj1gPncqMV4/ZSUaOVURCxIXRF5cVWl1FRpLSiVueCplJS0xViR8SylEW1Z+Lh0VeXQsUg8TVy8NPjteLW8PKhMjZHYhP04hC00+KlwVNk0mbjN3RhsJHlksfEspNRF+fSVMFncpVFIQQRlyQ3V8XW1mJmZLXyB4VVQ0WkwaNHElCw4MXEEzaWVpcC9gIBIlEU1HGEVkW0I2KBVLcU8cenZffSpBbiJoS10hTF5QCSkVe0M8YwxxFU11cjgzGxBhDyMOGFgJDA0yaFF7CT4VHThHKHIzd2UxPm4lZkxfIDVRP0FaW1Q4NmdBEXUmCQg3LGBwVxlRExpceEdXeisiFghvJ1EQFF5FR2llbQwtUlFRS2IPHxo0aQteTA==weCL2w==',
    'remember': '0',
    'lrp': '""',
    'lrr': '""',
    'hhrole': 'anonymous',
    'hhtoken': 'sT0EbKSy_vAmfcgaK7xUdds8Mua0',
    'redirect_host': 'hh.ru',
    'region_clarified': 'hh.ru',
    'device_magritte_breakpoint': 'm',
    'device_breakpoint': 'm',
    'total_searches': '5',
    'tmr_detect': '0%7C1695944737701',
    'cfidsgib-w-hh': 'GIoQO1wldpnSHfk9zaQ5rS4xPm1Eu9yWvglP4ZDquZpPplmc0UDJI/7Mp/oYpe6BJumZVMV5oHNfPRYnLQ+tGiGXhs3v1dEe4ieK5mU3g2k3z2h0HMZl3dvtoaQcOETMW2b2RlX1pwEFrB4eMURBHhJeh/yVDaT9jQu7M+rd',
    'cfidsgib-w-hh': 'GIoQO1wldpnSHfk9zaQ5rS4xPm1Eu9yWvglP4ZDquZpPplmc0UDJI/7Mp/oYpe6BJumZVMV5oHNfPRYnLQ+tGiGXhs3v1dEe4ieK5mU3g2k3z2h0HMZl3dvtoaQcOETMW2b2RlX1pwEFrB4eMURBHhJeh/yVDaT9jQu7M+rd',
    'cfidsgib-w-hh': 'GIoQO1wldpnSHfk9zaQ5rS4xPm1Eu9yWvglP4ZDquZpPplmc0UDJI/7Mp/oYpe6BJumZVMV5oHNfPRYnLQ+tGiGXhs3v1dEe4ieK5mU3g2k3z2h0HMZl3dvtoaQcOETMW2b2RlX1pwEFrB4eMURBHhJeh/yVDaT9jQu7M+rd',
    'gsscgib-w-hh': 'Zl6L2qXffjpXvFWuQewulnXbKZPrdK3PQ89UWQMYVgtC9lSh8DPudKOCn6oolnqmobtqYtvN+wgUWr20fupEjxP9hjPaNXBhS7/wMZohmA2omhnHMdZHc+5fSat25jXruJV6/OgYsJ0znNqe2ub4KE3uuDn/KXMbrFL+bTmm5Fb8mwNCRCY+RGHL221rs3hCCUeTJGyiQJWGbdM6ypEDoMvT1wxzz3lXjQWW3EPR+A1wd5/3DN9he5lgI6k3ISnMYppTO4q2',
    'gsscgib-w-hh': 'Zl6L2qXffjpXvFWuQewulnXbKZPrdK3PQ89UWQMYVgtC9lSh8DPudKOCn6oolnqmobtqYtvN+wgUWr20fupEjxP9hjPaNXBhS7/wMZohmA2omhnHMdZHc+5fSat25jXruJV6/OgYsJ0znNqe2ub4KE3uuDn/KXMbrFL+bTmm5Fb8mwNCRCY+RGHL221rs3hCCUeTJGyiQJWGbdM6ypEDoMvT1wxzz3lXjQWW3EPR+A1wd5/3DN9he5lgI6k3ISnMYppTO4q2',
    'fgsscgib-w-hh': 'z1G56146344e8b44aae5a58590277c1b3d84e89e',
    'fgsscgib-w-hh': 'z1G56146344e8b44aae5a58590277c1b3d84e89e',
}

headers = {
    'authority': 'spb.hh.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': '__ddg1_=7QxzneL01PxAHpUTWPxt; _xsrf=afee479ee0262c5853661924da9c55f1; hhuid=S69WessL!zyJWWTs7OEz5Q--; display=desktop; crypted_hhuid=6929BFF62FBA62676351A047F64BFCCF8ABD8824989FCDC5DF02F456F1BB61FF; GMT=3; tmr_lvid=29d240a7f7747d7eff2a7becf10b6a6c; tmr_lvidTS=1693248753024; _ga=GA1.2.972042572.1693248753; _ym_uid=1693248754361358126; _ym_d=1693248754; iap.uid=de7802753fb14412808f236fe6ede678; hhul=dd54cbcab12dc1df8c915916676b4782676bc65aa5a35c5e951af0a77cbfa74e; _gid=GA1.2.1206820436.1695563430; regions=2; _ym_isad=2; _ym_visorc=w; __zzatgib-w-hh=MDA0dC0jViV+FmELHw4/aQsbSl1pCENQGC9LX3VaQCBTZXpcInhdU3oqHxkxaytRDj1gPncqMV4/ZSUaOVURCxIXRF5cVWl1FRpLSiVueCplJS0xViR8SylEW1Z+Lh0VeXQsUg8TVy8NPjteLW8PKhMjZHYhP04hC00+KlwVNk0mbjN3RhsJHlksfEspNRF+fSVMFncpVFIQQRlyQ3V8XW1mJmZLXyB4VVQ0WkwaNHElCw4MXEEzaWVpcC9gIBIlEU1HGEVkW0I2KBVLcU8cenZffSpBbiJoS10hTF5QCSkVe0M8YwxxFU11cjgzGxBhDyMOGFgJDA0yaFF7CT4VHThHKHIzd2UxPm4lZkxfIDVRP0FaW1Q4NmdBEXUmCQg3LGBwVxlRExpceEdXeisiFghvJ1EQFF5FR2llbQwtUlFRS2IPHxo0aQteTA==weCL2w==; __zzatgib-w-hh=MDA0dC0jViV+FmELHw4/aQsbSl1pCENQGC9LX3VaQCBTZXpcInhdU3oqHxkxaytRDj1gPncqMV4/ZSUaOVURCxIXRF5cVWl1FRpLSiVueCplJS0xViR8SylEW1Z+Lh0VeXQsUg8TVy8NPjteLW8PKhMjZHYhP04hC00+KlwVNk0mbjN3RhsJHlksfEspNRF+fSVMFncpVFIQQRlyQ3V8XW1mJmZLXyB4VVQ0WkwaNHElCw4MXEEzaWVpcC9gIBIlEU1HGEVkW0I2KBVLcU8cenZffSpBbiJoS10hTF5QCSkVe0M8YwxxFU11cjgzGxBhDyMOGFgJDA0yaFF7CT4VHThHKHIzd2UxPm4lZkxfIDVRP0FaW1Q4NmdBEXUmCQg3LGBwVxlRExpceEdXeisiFghvJ1EQFF5FR2llbQwtUlFRS2IPHxo0aQteTA==weCL2w==; remember=0; lrp=""; lrr=""; hhrole=anonymous; hhtoken=sT0EbKSy_vAmfcgaK7xUdds8Mua0; redirect_host=hh.ru; region_clarified=hh.ru; device_magritte_breakpoint=m; device_breakpoint=m; total_searches=5; tmr_detect=0%7C1695944737701; cfidsgib-w-hh=GIoQO1wldpnSHfk9zaQ5rS4xPm1Eu9yWvglP4ZDquZpPplmc0UDJI/7Mp/oYpe6BJumZVMV5oHNfPRYnLQ+tGiGXhs3v1dEe4ieK5mU3g2k3z2h0HMZl3dvtoaQcOETMW2b2RlX1pwEFrB4eMURBHhJeh/yVDaT9jQu7M+rd; cfidsgib-w-hh=GIoQO1wldpnSHfk9zaQ5rS4xPm1Eu9yWvglP4ZDquZpPplmc0UDJI/7Mp/oYpe6BJumZVMV5oHNfPRYnLQ+tGiGXhs3v1dEe4ieK5mU3g2k3z2h0HMZl3dvtoaQcOETMW2b2RlX1pwEFrB4eMURBHhJeh/yVDaT9jQu7M+rd; cfidsgib-w-hh=GIoQO1wldpnSHfk9zaQ5rS4xPm1Eu9yWvglP4ZDquZpPplmc0UDJI/7Mp/oYpe6BJumZVMV5oHNfPRYnLQ+tGiGXhs3v1dEe4ieK5mU3g2k3z2h0HMZl3dvtoaQcOETMW2b2RlX1pwEFrB4eMURBHhJeh/yVDaT9jQu7M+rd; gsscgib-w-hh=Zl6L2qXffjpXvFWuQewulnXbKZPrdK3PQ89UWQMYVgtC9lSh8DPudKOCn6oolnqmobtqYtvN+wgUWr20fupEjxP9hjPaNXBhS7/wMZohmA2omhnHMdZHc+5fSat25jXruJV6/OgYsJ0znNqe2ub4KE3uuDn/KXMbrFL+bTmm5Fb8mwNCRCY+RGHL221rs3hCCUeTJGyiQJWGbdM6ypEDoMvT1wxzz3lXjQWW3EPR+A1wd5/3DN9he5lgI6k3ISnMYppTO4q2; gsscgib-w-hh=Zl6L2qXffjpXvFWuQewulnXbKZPrdK3PQ89UWQMYVgtC9lSh8DPudKOCn6oolnqmobtqYtvN+wgUWr20fupEjxP9hjPaNXBhS7/wMZohmA2omhnHMdZHc+5fSat25jXruJV6/OgYsJ0znNqe2ub4KE3uuDn/KXMbrFL+bTmm5Fb8mwNCRCY+RGHL221rs3hCCUeTJGyiQJWGbdM6ypEDoMvT1wxzz3lXjQWW3EPR+A1wd5/3DN9he5lgI6k3ISnMYppTO4q2; fgsscgib-w-hh=z1G56146344e8b44aae5a58590277c1b3d84e89e; fgsscgib-w-hh=z1G56146344e8b44aae5a58590277c1b3d84e89e',
    'referer': 'https://spb.hh.ru/applicant/negotiations',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Opera GX";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0',
}

params = {
    'text': 'python',
    'area': '2',
}

hh_job = requests.get('https://spb.hh.ru/search/vacancy', params=params, cookies=cookies, headers=headers)
#with open('result.html','w') as file:
 # file.write(hh_job.text)

hh_soup = BeautifulSoup(hh_job.text, 'html.parser')
paginator = hh_soup.find("span",{'class': 'bloko-button bloko-button_pressed'})
print(paginator)

pages = paginator.find_all('a')
print(pages)