import jogo
import menu_melhorias
import menu
import menu_fases
# def middleware():
#     jogo.jogo()
#     menu.menu()
#     menu_melhorias.menu_melhorias()

def middleware(caminho):
    if caminho == "jogo":
        jogo.jogo()
    elif caminho == "menu_melhorias":
        menu_melhorias.menu_melhorias()
    elif caminho == "menu":
        menu.menu()
    elif caminho == "menu_fases":
        menu_fases.menu_fases()
    else: print("nome do arquivo errado, middleware(erro aqui)")