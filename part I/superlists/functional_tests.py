from selenium import webdriver


browser = webdriver.Firefox()
# Edith ouvi falar de uma nova aplicação online interessante para
# lista de tarefas. Ela decide verificar sua homepage
browser.get('http://localhost:8000')

# ELa percebe que o título da página e o cabeçalho mencionam listas de tarefas
assert 'to-do' in browser.title

# Ela é convidada a inserir um item de tarefa imediatamente


# ELa digiata "Comprar penas de pavão" em uma caixa
# de texto 


# Quando ela tecla enter, a página é atualizada, e agora a página lista
# "1: Comprar penas de pavão" como um item em uma lista de tarefas


# Ainda contiua havendo uma caixa de texto convidando-a a acrescentar outro item.
# Ela insere "Usar penas de pavão para fazer um fly"


# A página é atualizada novamente e agora mostra os dois itens em sua lista


# Edith se pergunta se o site lembrará de sua lista. Então ela nota
# que o site gerou um URL único para ela -- há um pequeno
# text explicativo para isso.


# Ela acessa essa URL -  sua lista de tarefas continua lá.


# Satisfeita ela volta a dormir

browser.quit()