from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import time

def num_caps(manga):

	try:
		driver = webdriver.Chrome()
		driver.get("https://mangalivre.net/")
		time.sleep(2)

		action = ActionChains(driver)
		action.move_by_offset(10, 100)
		action.click()
		action.perform()
		new_tab = driver.window_handles[-1]
		driver.switch_to.window(new_tab)
		driver.close()
		driver.switch_to.window(driver.window_handles[0])

		time.sleep(5)

		busca = driver.find_element(By.CLASS_NAME,"btn-search")
		busca.click()
		time.sleep(1)

		caixa_busca = driver.find_element(By.ID,"searchInput")
		caixa_busca.click()
		time.sleep(1)
		caixa_busca.send_keys(manga)
		time.sleep(3)

		myElem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'auto-complete-search-container')))
		manga = driver.find_element(By.CLASS_NAME,"auto-complete-search-container").find_elements(By.CSS_SELECTOR,"ul")[0].find_elements(By.CSS_SELECTOR,"li")[0]
		time.sleep(3)
		manga.click()
		time.sleep(4)

		action = ActionChains(driver)
		action.move_by_offset(10, 100)
		action.click()
		action.perform()
		new_tab = driver.window_handles[-1]
		driver.switch_to.window(new_tab)
		driver.close()
		driver.switch_to.window(driver.window_handles[0])

		time.sleep(3)
		
		caps = driver.find_elements(By.CSS_SELECTOR,"h2")[-1].find_elements(By.CSS_SELECTOR,"span")[1].text

		return f'Existem {caps} capítulos desse mangá disponíveis para a leitura no mangalivre'
	
	except:
		return "Não foi possível encontrar esse mangá"

def puc_cursos():
	link = "https://www.puc-rio.br/ensinopesq/ccg/cursos.html"
	s = ""
	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
	requisicao = requests.get(link,headers = headers)
	site = BeautifulSoup(requisicao.content.decode('utf-8'), "html.parser")

	cursos = site.find_all('a')[5:44]

	cursos = [curso.text.strip().strip() for curso in cursos]

	for num, curso in enumerate(cursos):
		if "-" in curso:
			cursos[num] = curso.split("\xa0")[0]

	for curso in cursos:
		s+=curso + "\n"
	return s


  