from kivy.app import App
from kivy.lang import Builder


class convert(App):
    def build(self):
        self.title = "Convert m to km"
        self.root = Builder.load_file('Convert.kv')
        return self.root
    def Up(self):
        self.root.ids.input_number.text = self.root.ids.input_number.text
    def Down(self):
        self.root.ids.input_number.text = self.root.ids.input_number.text
    def Convert(self):
        self.root.ids.output_label.text = self.root.ids.input_number.text
convert().run()
