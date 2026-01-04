import requests, re
from datetime import datetime
months_ru = {
    1: "января", 2: "февраля", 3: "марта", 4: "апреля",
    5: "мая", 6: "июня", 7: "июля", 8: "августа",
    9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"
}
url = "https://books.toscrape.com/"  # ← вставьте свой URL здесь
resp = requests.get(f"https://web.archive.org/cdx/search?url={url}&output=txt")
dates = re.findall(r'(\d{14})', resp.text)
if dates:
    first_date = min(dates)
    dt = datetime.strptime(first_date[:8], "%Y%m%d")
    formatted_date = f"{dt.day} {months_ru[dt.month]} {dt.year}"    
    print(f"📅 Первый снимок: {formatted_date}")
    print(f"📸 Всего снимков: {len(set(dates))}")
else:
    print("❌ Ничего не найдено")