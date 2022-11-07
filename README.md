# ukol_seznam

Projekt se zabývá vypracování úkolu pro přijetí do firmy Seznam.

Jedná se o aplikace, která periodicky stahuje z API seznam filmů, který se ukládá do lokální databáze. Pro jednoduchost jsem použil databázi SQLite.

Pomocí webového frameworku Django jsem vytvořil backend a front-end této aplikace. Ve front-endu se načte filmový seznam a pomocí sidebaru lze filmy filtrovat.

Pro spuštění aplikace je potřeba stáhnout knihovny, které jsou v souboru requirements.txt.

V souboru setting.py ve webovým frameworku Django lze nastavit URL adresu pro API a periodu stahování.
Pro nastavení je potřeba do souboru přidat:
API_DOWNLOADER = {
    "url": "https://gist.githubusercontent.com/nextsux/f6e0327857c88caedd2dab13affb72c1/raw/04441487d90a0a05831835413f5942d58026d321/videos.json",
    "time": 30 # time in seconds
}
