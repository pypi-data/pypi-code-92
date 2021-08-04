from PymoNNto.Exploration.Network_UI.TabBase import *

class multi_group_plot_tab(TabBase):

    def __init__(self, variables, line_dict={}, title='Multi Group', timesteps=500):
        super().__init__(title)
        self.variables = variables
        self.line_dict = line_dict

        #add lines via variable|line
        #for i,var in enumerate(self.variables):
        #    split=var.split('|')
        #    if len(split)>1:
        #        self.variables[i]=split[0]#extract variable
        #        self.line_dict[split[0]]=split[1:]

        self.timesteps = timesteps

        #if tensorflow:
        #    self.add_str='.numpy()'
        #else:
        #    self.add_str=''

    def add_recorder_variables(self, neuron_group, Network_UI):
        for var in self.variables:
            #print(neuron_group.__dict__)
            #if hasattr(neuron_group, var):
            #try:
            #    print(var)
            Network_UI.add_recording_variable(neuron_group, 'n.'+var, timesteps=self.timesteps)
            Network_UI.add_recording_variable(neuron_group, 'np.mean(n.'+var+')', timesteps=self.timesteps)
            #except:
            #else:
            #    print('cannot add', var)



    def initialize(self, Network_UI):
        self.main_tab = Network_UI.Next_Tab(self.title)

        self.net_var_curves={}
        for i, var in enumerate(self.variables):
            stretch=1
            if i==0:
                stretch=2

            if var in self.line_dict:
                ld_val=self.line_dict[var]
                if type(ld_val) is list:
                    lines=ld_val
                else:
                    lines=[ld_val]
            else:
                lines=[]

            self.net_var_curves[var] = Network_UI.Add_plot_curve(stretch=stretch, number_of_curves=len(Network_UI.neuron_visible_groups), return_list=True, x_label='t (iterations)', y_label='Network average ' + var, lines=lines)


        Network_UI.Next_H_Block()

        self.neuron_var_curves = {}
        for i, var in enumerate(self.variables):
            stretch = 1
            if i == 0:
                stretch = 2

            if var in self.line_dict:
                ld_val = self.line_dict[var]
                if type(ld_val) is list:
                    lines = ld_val
                else:
                    lines = [ld_val]
            else:
                lines = []

            self.neuron_var_curves[var] = Network_UI.Add_plot_curve(stretch=stretch, colors=[Network_UI.neuron_select_color], legend=False, x_label='t (iterations)', y_label='Neuron ' + var, lines=lines)

        if Network_UI.group_display_count > 1:
            Network_UI.Next_H_Block()

            self.group_sliders = []
            for group_index in range(Network_UI.group_display_count):
                self.group_sliders.append(QSlider(1))  # QtCore.Horizontal
                self.group_sliders[-1].setMinimum(0)
                self.group_sliders[-1].setMaximum(100)
                self.group_sliders[-1].setSliderPosition(100)
                self.group_sliders[-1].mouseReleaseEvent = Network_UI.static_update_func
                self.group_sliders[-1].setToolTip('scale neuron-group plots up and down (only visualization)')

                Network_UI.Add_element(self.group_sliders[-1])


    def update(self, Network_UI):
        if self.main_tab.isVisible():


            for i, group_tag in enumerate(Network_UI.neuron_visible_groups):
                if len(Network_UI.network[group_tag]) > 0:
                    group=Network_UI.network[group_tag, 0]
                    if hasattr(self, 'group_sliders'):
                        squeeze= self.group_sliders[i].sliderPosition() / 100
                    else:
                        squeeze = 1

                    for var in self.variables:

                        #try:
                        #    self.net_var_plots[var].
                        #except:
                        #    pass

                        try:#if hasattr(group, var):
                            net_data = group['np.mean(n.'+var+')', 0, 'np'][-self.timesteps:]
                            iterations = group['n.iteration', 0, 'np'][-self.timesteps:]
                            self.net_var_curves[var][i].setData(iterations, net_data * squeeze, pen=group.color)
                        except:#else:
                            self.net_var_curves[var][i].clear()


            group = Network_UI.network[Network_UI.neuron_select_group, 0]

            for var in self.variables:
                try:#if hasattr(group, var):
                    neuron_data = group['n.' + var, 0, 'np'][-self.timesteps:].astype(def_dtype)
                    iterations = group['n.iteration', 0, 'np'][-self.timesteps:]
                    if len(neuron_data.shape) > 1:
                        neuron_data = neuron_data[:, Network_UI.neuron_select_id]
                    self.neuron_var_curves[var].setData(iterations, neuron_data)
                except:  #else:
                    self.neuron_var_curves[var].clear()

