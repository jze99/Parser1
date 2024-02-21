from flet import *

class Main(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        
        self.path_xslx = ""
        self.path_xml = ""

        self.filePickerXML = FilePicker(on_result=self.OnDialogResultXMLPath)
        self.page.overlay.append(self.filePickerXML)
        
        self.xml_path_text = TextField(
            label="XML документ",
            height=50,
            width=300,
            border_color="#B85C38",
            read_only=True,
            value="",
            text_size=12,
            multiline=False,
            expand=1,
            text_style=TextStyle(
                color="#E0C097",
            ),
            dense=True,
            on_focus=lambda _: self.filePickerXML.pick_files(
                allow_multiple=False,
                allowed_extensions=["XML"]
            )
        )
        self.button_xml_path = IconButton(
            icon=icons.ADD_BOX_OUTLINED,
            icon_size=40,
            style=ButtonStyle(
                color="#B85C38",
                shape=RoundedRectangleBorder(radius=10) 
            ), 
            on_click=lambda _: self.filePickerXML.pick_files(
                allow_multiple=False,
                allowed_extensions=["XML"]
            )
        )

        self.filePickerXLSX = FilePicker(on_result=self.OnDialogResultXLSXPath)
        self.page.overlay.append(self.filePickerXLSX)
        
        self.xlsx_path_text = TextField(
            label="XLSX документ",
            height=50,
            width=300,
            border_color="#B85C38",
            read_only=True,
            value="",
            text_size=12,
            multiline=False,
            expand=1,
            text_style=TextStyle(
                color="#E0C097",
            ),
            dense=True,
            on_focus=lambda _: self.filePickerXLSX.pick_files(
                allow_multiple=False,
                allowed_extensions=["xlsx"]
            )
        )
        self.button_xlsx_path = IconButton(
            icon=icons.ADD_BOX_OUTLINED,
            icon_size=40,
            style=ButtonStyle(
                color="#B85C38",
                shape=RoundedRectangleBorder(radius=10) 
            ), 
            on_click=lambda _: self.filePickerXLSX.pick_files(
                allow_multiple=False,
                allowed_extensions=["xlsx"]
            )
        )
        
    def OnDialogResultXMLPath(self, e: FilePickerResultEvent):
        if e.files == None:
            return
        value_path=e.files[0].path
        self.xml_path_text.value = value_path
        self.path_xml = value_path
        self.xml_path_text.update()
        
    def OnDialogResultXLSXPath(self, e: FilePickerResultEvent):
        if e.files == None:
            return
        value_path=e.files[0].path
        self.xlsx_path_text.value = value_path
        self.path_xslx = value_path
        self.xlsx_path_text.update()
    
    def build(self):
        return Column(
      controls=[
            Row(
                controls=[
                  self.xml_path_text,
                  self.button_xml_path
              ]
            ),
            Row(
                controls=[
                    self.xlsx_path_text,
                    self.button_xlsx_path
                ]
            ),
        ],
    )
        
