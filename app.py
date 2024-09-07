from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# abrir o driver
driver = webdriver.Chrome()

try:
    # Abre o site
    driver.get('https://divulgacandcontas.tse.jus.br/divulga/#/candidato/NORDESTE/PE/2045202024/170002323972/2024/26310')
    
    # Espera o site carregar
    time.sleep(4)
    
    # Localiza e clica no botão para abrir a aba de processos
    process_button = driver.find_element(By.XPATH, '//*[@id="mat-expansion-panel-header-1"]')
    process_button.click()
    
    # Tempo de espera para próxima ação
    time.sleep(1)
    
    # Localiza e clica no segundo item da lista de processos
    process_item = driver.find_element(By.XPATH, '//*[@id="cdk-accordion-child-1"]/div/dvg-candidato-processos/ol/li[2]')
    process_item.click()
    
    # Espera alguns segundos após abrir o site
    time.sleep(3)
    
    # Troca para a nova aba
    all_windows = driver.window_handles
    
    # Verifica se tem mais de uma aba
    if len(all_windows) > 1:
        # Troca para a nova aba
        driver.switch_to.window(all_windows[-1])
        
        # Passar pelo CAPTCHA
        print('Por favor, resolva o CAPTCHA...') 
        input('Após resolver, pressione ENTER. ')
    
        # Tempo de espera para próxima ação
        time.sleep(3)
        
        # Localizar botão de ir para o final da página
        button_final = driver.find_element(By.XPATH, '//button[@class="mat-paginator-navigation-last mat-icon-button mat-button-base ng-star-inserted"]')
        button_final.click()
    
        # Tempo de espera para próxima ação
        time.sleep(2)

        # Localizar o "drap.pdf" e clicar nele
        drap_link = driver.find_element(By.XPATH, '//a[contains(@href, "drap.pdf")]')
        drap_link.click()

        print('PDF aberto com sucesso!')
        
        # Tempo para o encerramento do navegador.
        time.sleep(10)


finally:
    driver.quit()
