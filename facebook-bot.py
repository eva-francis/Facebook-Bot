from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Autorizar():
	# Credenciales
	usuario = ''
	clave = ''
	mensaje = ''
	adjuntar_imagen = True
	ruta_imagen = ''
	enlaces_grupos = []

	chrome_options = webdriver.ChromeOptions()
	chrome.options.add_experimental_option("deatch", True)
	chrome_options.add_argument("--disable-inforbars")
	chrome_options.add_experimental_option("prefs", { \
		# 1:permitir - 2:bloquear
		"profile.default_content_setting_values.notifications": 2
		})


	driver = webdriver.Chrome(options=chrome_options)
	driver.implictly_wait(6) # segundos

	# Versión básica de facebook
	driver.get("https://mbasic.facebook.com/login/?ref=dbl&fl&refid=8")
	# Localización de xpath:email-usuario
	elem = driver.find_element_by_xpath('//*[@id="m_login_email"]')
	elem.send_keys(usuario)
	# Localización de xpath:clave
	elem = driver.find_element_by_xpath('//*[@id="login_form"]/ul/li[2]/div/input')
	elem.send_keys(clave)
	# Autorizar credenciales
	elem.send_keys(Keys.RETURN)

def Publicar():

	for grupo in enlaces_grupos:
		driver.get(grupo)
		# Localización de xpath:publicación
		ctexto_Publicacion = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div[3]/form/table/tbody/tr/td[2]/div/textarea")
		ctexto_Publicacion.send_keys(mensaje)

		if adjuntar_imagen:
			# Localización de xpath:botón para subir imagen ('foto')
			btn_Archivo = driver.find_elements_by_xpath('//*[@id="mbasic-composer-form"]/div/span/div[1]/table/tbody/tr/td[2]/input')[0]
			btn_Archivo.click()
			sleep(3)

			# Localización de xpath:botón para seleccionar archivo desde el ordenador ('seleccionar archivo')
			btn_Selec_Archivo = driver.find_element_by_xpath('//*[@id="root"]/table/tbody/tr/td/form/div[1]/div/input[1]')
			btn_Selec_Archivo.send_keys(ruta_imagen)
			sleep(3)

			previsualizar = driver.find_element_by_xpath('//*[@id="root"]/table/tbody/tr/td/form/div[3]/input[1]')
			previsualizar.click()
			sleep (3)

			# Localización de xpath:publicación
			btn_Publicar = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/table/tbody/tr/td/div/form/input[18]')
			btn_Publicar.click()
			sleep (5)

			btn_Omitir = driver.find_element_by_xpath('//*[@id="root"]/table/tbody/tr/td/div[2]/div[1]/a')
			btn_Omitir.click()

''' Evitamos realizar ejecucción manual y el bloqueo por uso de software para automatización.
	Asignamos un temporizador de 2 horas, que continuará publicando hasta que:
	La consola de comandos sea cerrada ó en su defecto, el navegador. '''

if __name__ == '__main__':
	while True:
		Autorizar()
		Publicar()
		sleep(7200) # 7200 segundos = 120 minutos = 2 horas
