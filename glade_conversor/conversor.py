import conversor_base as cb
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk as gtk

class Main:
    def __init__(self):
        # importação do arquivo glade
        gladefile    = "interface.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(gladefile)

        # inicialização das comboboxes e do botão
        entrada_combobox = self.builder.get_object('entrada_combobox')
        saida_combobox = self.builder.get_object('saida_combobox')
        tipos_combobox = self.builder.get_object('tipos_combobox')
        botao_converter = self.builder.get_object('botao_converter')

        #inicialização da caixa de resultados
        self.resultado = self.builder.get_object('caixa_resultado')
        
        # criando as listas que aparecem quando se clica no botão
        self.unidades_entrada = self.builder.get_object('unidades_entrada')
        self.unidades_saida = self.builder.get_object('unidades_saida')
        tipos_de_unidade = self.builder.get_object('tipos_de_unidade')

        # inserindo as unidades possíveis de cálculo, baseados no texto
        tipos_de_unidade_list = cb.tipos_de_unidade()
        for tipo in tipos_de_unidade_list:
            tipos_de_unidade.append([tipo])
        
        # variavies para salvar os clicks do usuario nas comboboxes
        self.tipo_escolhido = str() #no click do filtro escolhemos o tipo, que define as unidades que irão aparecer na outra caixa
        self.unidade_entrada_escolhida = str()
        self.unidade_saida_escolhida = str()
        self.entradas_list = list()
        self.saidas_list = list()

        # ligando o botao de converter
        botao_converter.connect('clicked',self.converter_click)

        #inicializando a caixa de texto
        self.input_usuario = self.builder.get_object('input_usuario')
 
        # Ativando os menus para aparecerem quando clicados
        vbox = gtk.Box(orientation=gtk.Orientation.VERTICAL, spacing=6)
        renderer_text = gtk.CellRendererText()
        
        entrada_combobox.connect("changed", self.combobox_entrada_click)
        entrada_combobox.pack_start(renderer_text, True)
        entrada_combobox.add_attribute(renderer_text, "text", 0)
        
        saida_combobox.connect("changed", self.combobox_saida_click)
        saida_combobox.pack_start(renderer_text, True)
        saida_combobox.add_attribute(renderer_text, "text", 0)

        tipos_combobox.connect("changed", self.combobox_tipos_click)
        tipos_combobox.pack_start(renderer_text, True)
        tipos_combobox.add_attribute(renderer_text, "text", 0)
        
        vbox.pack_start(entrada_combobox, False, False, True)


        # inicialização da janela
        window       = self.builder.get_object('Main_Window')
        window.connect('delete-event', gtk.main_quit)
        window.show()

    def converter_click(self, widget):
        un_entrada = self.unidade_entrada_escolhida
        un_saida = self.unidade_saida_escolhida
        valor = gtk.Entry.get_text(self.input_usuario)
        resposta = cb.converte(un_entrada,un_saida,float(valor))
        resposta_num = eval(str(resposta[0]))
        
        #formatacao das strings para a resposta
        resultado = "{:,.2f}".format(resposta_num).replace(",",".")
        valor_entrada = "{:,.2f}".format(float(valor)).replace(",",".")
        resultado = resultado[:-3]+resultado[-3:len(resultado)].replace(".",",")
        valor_entrada  = valor_entrada [:-3]+valor_entrada [-3:len(valor_entrada )].replace(".",",")
        
        markup = "<span>" + valor_entrada + " " + un_entrada + " equivalem a " + resultado  + " " +  un_saida + "</span>" 
        self.resultado.set_markup(markup)
    
    def combobox_saida_click(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            index = combo.get_active()
            model = combo.get_model()
            item = model[index][0]
            self.unidade_saida_escolhida = item
    
    def combobox_entrada_click(self, combo):
        # combobox de entrada, quando clicada, modifica a combobox condendo as unidades de saída (converte de entrda p/ saida)
        self.unidades_saida.clear()
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            index = combo.get_active()
            model = combo.get_model()
            item = model[index][0]
            self.unidade_entrada_escolhida = item #lê qual a unidade foi escolhida pelo usuario
            self.saidas_list_0 = cb.conversoes_possiveis(self.unidade_entrada_escolhida) #calcula as possiveis conversoes diretas
            self.saidas_list = self.saidas_list_0
            #loop para calcular as conversoes de segunda ordem (dias -> horas -> segundos) ao inves de (dias -> segundos)
            for unidade in self.saidas_list_0:
                unidade2 = cb.conversoes_possiveis(unidade)
                for unidade in unidade2:
                    if unidade not in self.saidas_list:
                        self.saidas_list += unidade2 
            self.saidas_list = list(dict.fromkeys(self.saidas_list))
            for saida in self.saidas_list:
                self.unidades_saida.append([saida])
    
    def combobox_tipos_click(self, combo): #ao clicar na caixa dos tipos você muda a caixa de unidades de baixo
        self.unidades_entrada.clear()
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            index = combo.get_active()
            model = combo.get_model()
            item = model[index][0]
            self.tipo_escolhido = item #seta o tipo de conversao sendo feita (tempo, comprimento, temperatura)
            self.entradas_list = cb.unidades_do_tipo(self.tipo_escolhido)
            for entrada in self.entradas_list:
                self.unidades_entrada.append([entrada])


if __name__ == '__main__':
    main = Main()
    gtk.main()