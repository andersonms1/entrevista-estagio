class Utils:

    def clear_screen(self, lines):
        for i in range(0, lines):
            print()

    def print_menu(self):
        print('O que vc deseja saber?')
        print('1 - Próximo lançamento')
        print('2 - Último lançamento')
        print('3 - Próximos lançamentos')
        print('4 - Lançamentos passados')