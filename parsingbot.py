from bs4 import BeautifulSoup
with open ("index.html",encoding="utf-8") as file:
    src = file.read()
#print(src)

soup = BeautifulSoup(src, "lxml") #Принимает переменную с кодом src, также идет парсер (вроде как быстрый)

#title = soup.title
#print(title) Выводит текст из кода, title.text выводит только текст

shadow = soup.find("tr", class_="shadow")
print(shadow)
