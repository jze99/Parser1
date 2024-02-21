from flet import *
from main import Main
from XMLparser import xml_parser
from upload import *

def viewsHendler(page):
    
    err_text = Text(
        value="Закройте файл в который сохраняете информацию",
        size=45
    )
    
    def Pars(e):
        if main_page.path_xml != "" and main_page.path_xslx != "":
            page.go('/loding')
            if xml_parser.Parsing(pathXML=main_page.path_xml) == True:
                if uploadPath(file_path= main_page.path_xslx) == True:
                    page.go('/')
                else:
                    page.go("/err")
                    
                    
    def Beak(e):
        page.go('/')
    
    button_pars = FloatingActionButton(
        icon=icons.SKIP_NEXT_ROUNDED,
        bgcolor="#B85C38",
        on_click=Pars
    )
    
    button_beak = FloatingActionButton(
        icon=icons.CHEVRON_LEFT_ROUNDED,
        bgcolor="#B85C38",
        on_click=Beak
    )
    
    main_page = Main(page=page)
    return {
        '/':View(
            route='/', 
            bgcolor="#2D2424",
            controls=[
                main_page,
                Row(
                    alignment=MainAxisAlignment.END,
                    controls=[
                        button_pars
                    ]
                )
            ]
        ),
        '/loding':View(
            route='/loding', 
            bgcolor="#2D2424",
            controls=[
                Text(
                    value="Пожалуйста подождите",
                    size=45,
                )
            ]
        ),
        '/err':View(
            route="/err",
            bgcolor="#2D2424",
            controls=[
                err_text,
                button_beak
            ]
        )
    }