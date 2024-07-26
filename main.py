from kivymd.app import MDApp
from kivy.lang import Builder

from kivymd.uix.tab import MDTabsBase, MDTabs
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import MDList, OneLineListItem, OneLineAvatarIconListItem, OneLineIconListItem
from kivy.properties import StringProperty, ListProperty
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton, MDTextButton, MDFloatingActionButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.behaviors import TouchBehavior
from kivymd.uix.navigationdrawer import MDNavigationLayout

from kivymd.font_definitions import fonts
from kivymd.icon_definitions import md_icons

from kivy.clock import Clock
from kivy.metrics import dp

from time import sleep
import random
from datetime import datetime, timedelta


from utils import (
    show_all_type_production,
    get_type_by_id,
    get_type_by_name,
    show_all_animals,
    get_all_animals,
    animal_production_change,
    delete_animal,
    add_animal_production,
    get_production_by_name_animal,
    get_production_by_id,
    delete_production,
    production_saver,
    get_all_production,
    show_barn_animals,
    show_all_animals_types,
    delete_animal_type,
    get_animal_type_for_id,
    get_barns,
    get_barn_for_id,
    get_player_barns,
    animal_saver,
    animal_type_saver,
    barn_saver,
    get_player,
    player_autorization,
    player_registration,
    productions_saver,
    productions_sum_change,
    get_productions_last_date,
    get_productions_sum_by_player,
    productions_sell_change,

)


KV = '''
# https://stackoverflow.com/questions/65698145/kivymd-tab-name-containing-icons-and-text
# this import will prevent disappear tabs through some clicks on them)))
#:import md_icons kivymd.icon_definitions.md_icons
#:import fonts kivymd.font_definitions.fonts




Screen:
        
    ScreenManager:
        Screen:
            id: main_screen
            name: 'main_window'
            BoxLayout:
                orientation: 'vertical'
                id: start_window              
                # MDTopAppBar:
                #     title: "Farm"
                #     elevation: 10
                #     md_bg_color: 0, 0, 0, 1
                #     # left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                #     # right_action_items: [["star-outline", lambda x: app.on_star_click()]]
                # 
                Navigation:
                    id:navigation
                # MDTextButton:
                #     text: 'Начать игру'
                #     on_release: app.on_start_main_menu()
                #     pos_hint: {"center_x": .5, "center_y": 0.5}
                #     valign: 'top'
                    
<ContentSignUpDialog>
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"

    MDTextField:
        name: "nickname"
        hint_text: "Nickname"

    MDTextField:
        name: "password"
        hint_text: "Password"

<Navigation>:
    ScreenManager:
        Screen:
            BoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Farm"
                    elevation: 10
                    left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                    # right_action_items: [["star-outline", lambda x: app.on_star_click()]]
                    md_bg_color: 0, 0, 0, 1
                MDTabs:
                    id: tabs
                    on_tab_switch: app.on_tab_switch(*args)
                    height: "48dp"
                    tab_indicator_anim: False
                    background_color: 0.1, 0.1, 0.1, 1
                    Tab:
                        id: barns
                        name: 'barns'
                        title: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['barn']}[/size][/font] Ферма"
                        BoxLayout:
                            orientation: 'vertical'
                            BoxLayout:
                                orientation: 'horizontal'
                                padding: "10dp"
                                ScrollView:
                                    AnimalsList:
                                        id: md_list
                                
                    Tab:
                        id: finance
                        name: 'finance'
                        title: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['finance']}[/size][/font] Финансы"
                        BoxLayout:
                            orientation: 'vertical'
                            BoxLayout:
                                orientation: 'horizontal'
                                padding: "10dp"
                    Tab:
                        id: production
                        name: 'production'
                        title: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['account-cowboy-hat']}[/size][/font] Продукция"
                        BoxLayout:
                            orientation: 'vertical'
                            BoxLayout:
                                orientation: 'horizontal'
                                padding: "10dp"
                    Tab:
                        id: slaughter_animals
                        name: 'slaughter_animals'
                        title: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['account-cowboy-hat']}[/size][/font] Заготовка мяса"
                        BoxLayout:
                            orientation: 'vertical'
                            BoxLayout:
                                orientation: 'horizontal'
                                padding: "10dp"
                    Tab:
                        id: admin
                        name: 'admin'
                        title: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['account-cowboy-hat']}[/size][/font] Админ"
                        BoxLayout:
                            orientation: 'vertical'
                            BoxLayout:
                                orientation: 'horizontal'
                                padding: "10dp"
    MDNavigationDrawer:
        id: nav_drawer

        ContentNavigationDrawer:
            id: content_drawer
                    
                        

        
                    

<ItemProduction>:
    IconLeftWidget:
    

<MenuTextField>:
    #id: menu_text_field
    name: 'menu_text_field'
    text: "animal"
    on_focus:  if self.focus: app.menu.open()
    
<MenuTextFieldBarns>:
    #id: menu_text_field
    name: 'menu_text_field_barns'
    text: "barns"
    on_focus:  if self.focus: app.menu_barns.open()
    
<MenuTextFieldTypeProduction>:
    #id: menu_text_field
    name: 'menu_text_field_type'
    text: "type_production"
    on_focus:  if self.focus: app.type_menu.open()

<MenuTextFieldProduction>:
    #id: menu_text_field
    name: 'menu_text_field_production'
    text: "production"
    on_focus:  if self.focus: app.production_menu.open()

<ItemDrawer>:
    theme_text_color: "Custom"
    #on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color
    
<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "kivymd_logo.png"

    MDLabel:
        text: app.title
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: app.by_who
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]
   
    ScrollView:
        DrawerList:
            id: md_drawer_list
            
# <ItemSell>:    
#     id: item_dialog
#     on_size:
#         self.ids._right_container.width = container_dialog.width
#         self.ids._right_container.x = container_dialog.width
#     ContainerDialog:
#         id: container_dialog
# 
# <ContainerDialog>:
#     id: container_dialog
#     # MDLabel:
#     #     id: lbl1
#     #     size: [1, 1]
#     # MDLabel:
#     #     id: lbl2
#     # MDLabel:
#     #     id: lbl3
#     #     
#     # MDTextField:
#     #     id: txt
#     # 
'''

class ContentNavigationDrawer(BoxLayout):
    pass

class DrawerList(MDList):
    def __init__(self, *args, **kwargs):
        super(DrawerList, self).__init__(*args, **kwargs)



    # def set_color_item(self, instance_item):
    #     '''Called when tap on a menu item.'''
    #     # Set the color of the icon and text for the menu item.
    #     for item in self.children:
    #         if item.text_color == self.theme_cls.primary_color:
    #             item.text_color = self.theme_cls.text_color
    #             break
    #     instance_item.text_color = self.theme_cls.primary_color


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
class Navigation(MDNavigationLayout):
    def __init__(self, **kwargs):
        super(Navigation, self).__init__(**kwargs)
class AnimalsList(MDList):
    def __init__(self, *args, **kwargs):
        super(AnimalsList, self).__init__(*args, **kwargs)

class ItemAnimal(OneLineListItem):
    def __init__(self, **kwargs):
        super(ItemAnimal, self).__init__(**kwargs)

class ItemDetailField(OneLineListItem):
    def __init__(self, **kwargs):
        super(ItemDetailField, self).__init__(**kwargs)
class ItemProduction(OneLineAvatarIconListItem):
    def __init__(self, **kwargs):
        super(ItemProduction, self).__init__(**kwargs)
    icon = StringProperty()
    text = StringProperty()


class MenuTextField(MDTextField):
    def __init__(self, **kwargs):
        super(MenuTextField, self).__init__(**kwargs)
        self.id_item_menu = 0
class MenuTextFieldTypeProduction(MDTextField):
    def __init__(self, **kwargs):
        super(MenuTextFieldTypeProduction, self).__init__(**kwargs)
        self.id_item_menu = 0

class MenuTextFieldProduction(MDTextField):
    def __init__(self, **kwargs):
        super(MenuTextFieldProduction, self).__init__(**kwargs)
        self.id_item_menu = 0
class BarnTable(MDDataTable):
    def __init(self, **kwargs):
        super(BarnTable, self).__init__(**kwargs)



class CellRow(BoxLayout, TouchBehavior):
    def __init__(self, **kwargs):
        super(CellRow, self).__init__(**kwargs)

    def on_press(self):

        print('ONPRESS',instance_row)


class MenuTextFieldBarns(MDTextField):
    def __init__(self, **kwargs):
        super(MenuTextFieldBarns, self).__init__(**kwargs)
        self.id_item_menu = 0
class ListItem(OneLineListItem):
    def __init__(self, **kwargs):
        super(ListItem, self).__init__(**kwargs)
class CheckDialog(MDDialog):
    def __init__(self, **kwargs):
        super(CheckDialog, self).__init__(**kwargs)

class ContentSignUpDialog(BoxLayout):
    def __init__(self, **kwargs):
        super(ContentSignUpDialog, self).__init__(**kwargs)
# class SellDialog(MDDialog):
#     def __init__(self, title, type, content_cls, buttons):
#         super(SellDialog, self).__init__()
#         self.title = title
#         self.type = type
#         self.content_cls = content_cls
#         self.buttons = buttons
class Tab(MDFloatLayout, MDTabsBase):
    pass
class ContainerDialog(BoxLayout):
    adaptive_width = True
class ItemSell(OneLineAvatarIconListItem):
    def __init__(self, content):
        print(content)

        super(ItemSell, self).__init__()
        print(self.set_center_x())
        print(self.ids)
        print(self.ids.container_dialog.ids)
        self.ids.container_dialog.add_widget(MDLabel(text=content[0]))
        # self.ids.container_dialog.ids.lbl1.text = content[0]
        # self.ids.container_dialog.ids.lbl2.text = content[1]
        # self.ids.lbl1.text = content[0]
        # self.ids.lbl2.text = content[1]
        # self.ids.lbl3.text = str(content[2])
        # self.ids.txt.hint_text = 'Кол-во для продажи'
        # self.ids.txt.text = '0'
        # self.ids.txt.id = f'{content[0]}:{content[1]}'

# class ItemSellList(MDList, ScrollView):
#
#     def __init__(self, content_lst):
#         print('Sellcontent', content_lst)
#         super(ItemSellList, self).__init__(content_lst)
#         self.content_lst = content_lst
#         self.length = len(content_lst)-1
#         self.scroll = MDList()
#         self.add_widget(self.scroll)
#         for content in content_lst:
#             #self.scroll.add_widget(ItemDetailField(text=f'{content}'))
#
#             self.scroll.add_widget(ItemSell(content))

class SellGrid(MDGridLayout):

    def __init__(self, content_lst):
        super(SellGrid, self).__init__(content_lst)
        self.rows = len(content_lst)
        self.content_lst = content_lst
        # self.sell_list = MDList()
        # self.add_widget(self.sell_list)
        for i in range(self.rows):
            self.add_widget(MDLabel(text=content_lst[i][0]))
            self.add_widget(MDLabel(text=content_lst[i][1]))
            self.add_widget(MDLabel(text=str(content_lst[i][2])))
            self.add_widget(MDTextField(id=f'{content_lst[i][0]}:{content_lst[i][1]}', text='0', hint_text='Кол-во для продажи'))

class ItemDetailList(MDList):#, ScrollView):
    def __init__(self, item):
        super(ItemDetailList, self).__init__(item)
        self.item = item
        self.length = len(item.__dict__.keys())-1
        # self.scroll = MDList()
        # self.add_widget(self.scroll)
        for k in sorted(item.__dict__.keys()):
            if k not in ['_sa_instance_state','id']:
                self.add_widget(ItemDetailField(text=f'{k}:{item.__dict__[k]}'))


# class Tab_menu_box(BoxLayout):
#     pass
# class Tab_menu(MDTabs):
#     pass
# class ScrollItemMenu(ScrollView):
#     pass
# class ListItemMenu(MDList):
#     pass
class FarmSimApp(MDApp):
    title = 'Game_Farm'
    by_who = "direct_fito@gmail.com"
    author_name = 'Alex'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        self.player = get_player(1)#None
        self.dialog_check_buy_animals = None
        self.dialog_sell_prod = None
        self.dialog_update_delete = None
        self.navigation = None
        self.sign_up_dialog = None
        # self.theme_cls.primary_palette = 'Lime'
        # self.theme_cls.primary_hue = 'A100'
        print('IDS', self.screen.ids)

    def build(self):
        #self.screen = Builder.load_string(KV)
        self.theme_cls.theme_style = "Light"
        return self.screen

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        if self.player:
            if instance_tab.name=='barns':
                instance_tab.clear_widgets()
                tab_menu_box = BoxLayout()#Tab_menu_box()
                tab_menu = MDTabs()#Tab_menu()
                instance_tab.add_widget(tab_menu_box)
                tab_menu_box.add_widget(tab_menu)
                for barn in self.player.barns:
                    tab_menu.add_widget(Tab(title=barn.name, name=barn.name, id='barn_'+str(barn.id)))
                tab_menu.bind(on_tab_switch=self.on_tab_switch_menu)
            elif instance_tab.name=='finance':
                instance_tab.clear_widgets()
                tab_menu_box = BoxLayout(orientation='vertical')  # Tab_menu_box(orientation='vertical')
                instance_tab.add_widget(tab_menu_box)
                lbl = MDLabel(text=instance_tab.name, id=instance_tab.name + '_id')
                btn_buy = MDTextButton(text='Купить', pos_hint={"left_x": .5, "center_y": .5})
                btn_build = MDTextButton(text='Построить', pos_hint={"left_x": .5, "center_y": .5})
                btn_buy.bind(on_release=lambda x=self, instance_tab=instance_tab:self.choice_animals(x, instance_tab))
                btn_build.bind(on_release=lambda x=self, instance_tab=instance_tab: self.choice_barn(x, instance_tab))
                tab_menu_box.add_widget(lbl)
                tab_menu_box.add_widget(btn_buy)
                tab_menu_box.add_widget(btn_build)
            elif instance_tab.name=='production':
                instance_tab.clear_widgets()
                scmenu = ScrollView()  # ScrollItemMenu()
                listnemu = MDList()

                boxmenu = MDList()#BoxLayout(orientation='vertical')
                lmenu_prod = MDList()  # ListItemMenu()
                lmenu_prod_sum = MDList()
                instance_tab.add_widget(scmenu)
                scmenu.add_widget(boxmenu)
                boxmenu.add_widget(lmenu_prod)
                btn = MDTextButton(text='Продать', pos_hint={"left_x": .5, "center_y": .5})
                btn.bind(on_release=self.show_sell_production_dialog)
                type_animal_prod_dict = dict.fromkeys([an_t.name for an_t in show_all_animals_types()], 0)
                production_dict = dict.fromkeys([pr.name for pr in get_all_production()], {})
                for key,value in production_dict.items():
                    prod_ids = [pr.id for pr in get_all_production() if pr.name == key]
                    production_dict[key] = dict.fromkeys([an_t.name for an_t in show_all_animals_types()
                                                          if an_t.production_id in prod_ids], 0)
                last_date = get_productions_last_date()
                delta = (datetime.today().date() - last_date).days
                if delta == 0:
                    lmenu_prod.add_widget(ItemProduction(text=f'Вся продукция собрана.', icon=md_icons['egg']))
                else:
                    for i in range(delta):
                        for barn in self.player.barns:
                            for animal in barn.animals:
                                prod = random.randint(int(animal.animal_type.production_limits['min']),
                                                                   int(animal.animal_type.production_limits['max']))
                                production_dict[animal.animal_type.production.name][animal.animal_type.name]+=prod

                                animal_production_change(animal, prod)
                    for key, value in production_dict.items():
                        print(key, value)
                        for k, v in value.items():
                            productions_saver(key, v, k, self.player)
                            productions_sum_change(key,v, k, self.player)
                            lmenu_prod.add_widget(
                                ItemProduction(text=f'{key}: {k}-{v}', icon=md_icons['egg'])
                            )
                boxmenu.add_widget(MDLabel(text='Всего на складе'))
                boxmenu.add_widget(lmenu_prod_sum)
                for prod in get_productions_sum_by_player(self.player):
                    if prod.count>0:
                        lmenu_prod_sum.add_widget(
                            ItemProduction(text=f'{prod.name}:{prod.animal}:{prod.count}', icon=md_icons['egg'])
                        )
                boxmenu.add_widget(btn)
            elif instance_tab.name=='slaughter_animals':
                instance_tab.clear_widgets()
                scmenu = ScrollView()  # ScrollItemMenu()
                boxmenu = BoxLayout(orientation='vertical')
                lmenu_prod = MDList()  # ListItemMenu()
                lmenu_prod_sum = MDList()
                instance_tab.add_widget(scmenu)
                scmenu.add_widget(boxmenu)
                boxmenu.add_widget(lmenu_prod)
                btn_slaug = MDTextButton(text='Забить', pos_hint={"left_x": .5, "center_y": .5})

                type_animal_prod_dict = dict.fromkeys([an_t.name for an_t in show_all_animals_types()], 0)
                production_dict = dict.fromkeys([pr.name for pr in get_all_production()], {})
                for key,value in production_dict.items():
                    prod_ids = [pr.id for pr in get_all_production() if pr.name == key]
                    production_dict[key] = dict.fromkeys([an_t.name for an_t in show_all_animals_types()
                                                          if an_t.production_id in prod_ids], 0)

                print('AN', production_dict)
                animal_lifespan_dict = {}
                pl_anim = [an for an in get_all_animals() if an.barn_id in [b.id for b in get_player_barns(self.player)]]
                pl_anim = {'Сегодня':[], '1 день': [], 'Потери': []}
                animal_types_names = list(set([a_t.name for a_t in show_all_animals_types()]))
                pl_anim = {'Сегодня': dict.fromkeys(animal_types_names),
                            '1 день': dict.fromkeys(animal_types_names),
                           'Потери': dict.fromkeys(animal_types_names)}
                print(pl_anim)

                for anim in  [an for an in get_all_animals() if an.barn_id in [b.id for b in get_player_barns(self.player)]]:
                    temp_date = datetime.today().date() - timedelta(days=anim.animal_type.lifespan)
                    temp_date -= anim.date_created
                    if -temp_date.days ==0:
                        key = 'Сегодня'
                    elif -temp_date.days ==1:
                        key = '1 день'
                    elif -temp_date.days <0:
                        key = 'Потери'
                    else:
                        continue
                    if key:
                        if pl_anim[key][anim.animal_type.name]:
                            pl_anim[key][anim.animal_type.name].append(anim)
                        else:
                            pl_anim[key][anim.animal_type.name] = []
                            pl_anim[key][anim.animal_type.name].append(anim)
                print('PLANIM',pl_anim)
                boxmenu.add_widget(MDLabel(text='Животные для забоя'))
                for key, value in pl_anim.items():
                    text_lbl = ''
                    for k, v in value.items():
                        if v:
                            vv = len(v)
                            text_lbl+=f'{k}:{vv}'
                        else:
                            vv = 0
                    if text_lbl:
                        text_lbl = f'{key}:' + text_lbl
                        boxmenu.add_widget(MDLabel(text=text_lbl))
                btn_slaug.bind(on_release=lambda instance=self, key='1 день', items=pl_anim: self.slaughter(instance,key, items))
                boxmenu.add_widget(btn_slaug)
                self.slaughter(btn_slaug, 'Сегодня', pl_anim)

            elif instance_tab.name=='admin':
                instance_tab.clear_widgets()
                tab_admin_menu_box = BoxLayout()
                tab_admin_menu = MDTabs()
                instance_tab.add_widget(tab_admin_menu_box)
                tab_admin_menu_box.add_widget(tab_admin_menu)
                tab_admin_menu.add_widget(Tab(title="Вид продукции", name="crud_production", id='crud_production'))
                tab_admin_menu.add_widget(Tab(title="Порода животных", name="crud_animal_type", id='crud_animal_type'))
                tab_admin_menu.bind(on_tab_switch=self.on_tab_switch_admin_menu)
        else:
            self.wrong_autorization_dialog = MDDialog(
                    title="Ошибка",
                    type="custom",
                    text="Ошибка входа, проверьте данные или зарегистируйтесь",
                    buttons=[
                        MDFlatButton(
                            text="OK",
                            theme_text_color="Custom",
                            on_release=lambda instance=self: self.on_cancel_wrong_autorization_dialog(instance)
                        ),
                    ],
                )
            self.wrong_autorization_dialog.open()

    def on_tab_switch_menu(self,instance_tabs, instance_tab, instance_tab_label, tab_text):
        #print(instance_tabs, instance_tab,instance_tab_label, tab_text)
        print('INSTAB_MENU',instance_tab, instance_tab.name, instance_tab.id)#, self.screen.ids[instance_tab.name])
        animals = show_barn_animals(instance_tab.id)
        row_data_for_tab = []
        for animal in animals:
            temp_date = datetime.today().date()-timedelta(days=animal.animal_type.lifespan)
            temp_date-=animal.date_created
            row_data_for_tab.append([animal.id_number, animal.animal_type,-temp_date.days])
        data_tables = BarnTable(
            use_pagination=True,
            pagination_menu_pos='center',
            size_hint=(1,1),
            rows_num=10,
            column_data=[
                ('ID_NUMBER',dp(40)),
                ('Порода', dp(50)),
                ('Срок жизни', dp(10))
            ],
            row_data=row_data_for_tab,
        )
        instance_tab.add_widget(data_tables)
        # scmenu = ScrollView()  # ScrollItemMenu()
        # lmenu = MDList()  # ListItemMenu()
        # instance_tab.add_widget(scmenu)
        # scmenu.add_widget(lmenu)
        # for animal in animals:
        #     lmenu.add_widget(
        #         ItemAnimal(text=f'{animal.id_number}-{animal.animal_type}')
        #     )

    def slaughter(self, instance, key, slaugh_animals):
        print(key)
        meet_dict={'Мясо': dict.fromkeys([at.name for at in show_all_animals_types()],0)}
        print(meet_dict)
        for key, value in slaugh_animals[key].items():
            if value:
                meet_dict['Мясо'][key] = round(sum([an.weight*0.7 for an in value]),2)
                for an in value:
                    delete_animal(an)
        print(meet_dict)
        for key, value in meet_dict['Мясо'].items():

            if value>0:
                productions_saver('Мясо', value, key, self.player)
                productions_sum_change('Мясо', value, key, self.player)



    def on_tab_switch_admin_menu(self,instance_tabs, instance_tab, instance_tab_label, tab_text):
        print('INSTAB_MENU_ADMIN', instance_tab.id)
        instance_tab.clear_widgets()
        tab_admin_crud_menu_box = BoxLayout(orientation='vertical')
        tab_admin_crud_menu_box_butons = BoxLayout(size_hint=(1,0.2))
        instance_tab.add_widget(tab_admin_crud_menu_box)
        row_data_for_list_tab = []
        if instance_tab.id == 'crud_production':
            for prod in get_all_production():
                row_data_for_list_tab.append(
                    [prod.id, prod.name, prod.type.name, prod.production_min, prod.production_max, prod.cost])
            data_tables = BarnTable(
                use_pagination=True,
                pagination_menu_pos='center',
                size_hint=(1, 1),
                rows_num=10,
                column_data=[
                    ('ID', dp(5)),
                    ('Название', dp(30)),
                    ('Тип', dp(30)),
                    ('Min', dp(30)),
                    ('Max', dp(30)),
                    ('Цена', dp(30)),
                ],
                row_data=row_data_for_list_tab,
            )
        elif instance_tab.id == 'crud_animal_type':
            for an_type in show_all_animals_types():
                limits = (an_type.production_limits['min'], an_type.production_limits['max'])
                row_data_for_list_tab.append(
                    [an_type.id, an_type.name, an_type.breed, an_type.weight, an_type.production.name,
                     f'{limits[0]}:{limits[1]}', an_type.capacity, an_type.cost, an_type.lifespan])
            data_tables = BarnTable(
                use_pagination=True,
                pagination_menu_pos='center',
                size_hint=(1, 1),
                rows_num=10,
                column_data=[
                    ('ID', dp(5)),
                    ('Название', dp(25)),
                    ('Порода', dp(25)),
                    ('Вес', dp(10)),
                    ('Продукция', dp(25)),
                    ('Лимиты', dp(20)),
                    ('Размер', dp(20)),
                    ('Цена', dp(10)),
                    ('Срок', dp(5))
                ],
                row_data=row_data_for_list_tab,
            )
        data_tables.bind(on_row_press=self.on_row_press)
        btn = MDTextButton(text='Добавить')
        btn_action = MDTextButton(text='Изменить')
        btn.bind(on_release=lambda x=self, instance_tab=instance_tab: self.choice_items_for_create_update(x, instance_tab, item=None))
        #btn_action.bind(on_release=lambda  x=self, table=data_tables: self.b(x,table))
        tab_admin_crud_menu_box.add_widget(data_tables)
        tab_admin_crud_menu_box.add_widget(tab_admin_crud_menu_box_butons)
        tab_admin_crud_menu_box_butons.add_widget(btn)
        tab_admin_crud_menu_box_butons.add_widget(btn_action)


    def on_row_press(self, instance_table, instance_row):
        # instance_row.bind(on_release=lambda x=self, instance_table=instance_table, instance_row=instance_row:
        # self.a(x, instance_table, instance_row))
        ind_row_data = int(instance_row.range[0]/((instance_row.range[1]-instance_row.range[0])+1))
        if instance_table.row_data[ind_row_data]:
            if instance_table.parent.parent.id =='crud_production':
                item = get_production_by_id(int(instance_table.row_data[ind_row_data][0]))
            elif instance_table.parent.parent.id =='crud_animal_type':
                item = get_animal_type_for_id(int(instance_table.row_data[ind_row_data][0]))
        self.show_update_delete_dialog(item, instance_table.parent.parent)




    # def b(self,x,table):
    #     pass
    #     print(x,table.get_row_checks())
    def show_update_delete_dialog(self, item, instance_tab):
        self.dialog_update_delete = None
        if not self.dialog_update_delete:
            content_dialog = ItemDetailList(item)
           #content_dialog.size = [100, 300]
            self.dialog_update_delete = CheckDialog(
                title="Информация по записи",
                content_cls = content_dialog,
                type="custom",
                buttons=[
                    MDFlatButton(
                        text="Изменить",
                        theme_text_color="Custom",
                        on_release=lambda x=self, instance_tab=instance_tab, item=item: self.choice_items_for_create_update(x, instance_tab, item)

                    ),
                    MDFlatButton(
                        text="Удалить",
                        theme_text_color="Custom",
                        on_release=lambda x=self, instance_tab=instance_tab, item=item: self.delete_item(x, instance_tab, item)
                    ),
                    MDFlatButton(
                        text="Отмена",
                        theme_text_color="Custom",
                        on_release=lambda instance=self.dialog_check_buy_animals: self.on_cancel_update_create_dialog(instance)
                    ),
                ],
            )
            box_lbl = BoxLayout(orientation='vertical')
            self.dialog_update_delete.add_widget(box_lbl)
            self.dialog_update_delete.open()

    def choice_items_for_create_update(self, x, instance_tab, item):
        print(instance_tab, instance_tab.id, item)
        instance_tab.clear_widgets()
        if instance_tab.id == 'crud_production':
            self.form_for_create_update_production(x, instance_tab, item)
        elif instance_tab.id == 'crud_animal_type':
            self.form_for_create_update_animal_type(x, instance_tab, item)

    def form_for_create_update_production(self, x, instance_tab, item):

        instance_tab.clear_widgets()
        type_menu_items = []
        ind = 0
        box = BoxLayout(orientation='vertical')
        if item is None:
            lbl_name = MDTextField(id='name', hint_text='Введите название', text='')
            self.choice_type_production = MenuTextFieldTypeProduction(id='type', hint_text='Выберите тип', text='')
            lbl_limit_min = MDTextField(id='limit_min', hint_text='Введите минимум', text='0')
            lbl_limit_max = MDTextField(id='limit_max', hint_text='Введите максимум', text='0')
            lbl_cost = MDTextField(id='cost', hint_text='Введите цену', text='1')
            btn = MDTextButton(text='Создать', pos_hint={"left_x": .5, "center_y": .5})
        else:
            lbl_name = MDTextField(id='name', hint_text='Введите название', text=item.name)
            self.choice_type_production = MenuTextFieldTypeProduction(id='type', hint_text='Выберите тип', text=get_type_by_id(item.type_id).name)
            lbl_limit_min = MDTextField(id='limit_min', hint_text='Введите минимум', text=str(int(item.production_min)))
            lbl_limit_max = MDTextField(id='limit_max', hint_text='Введите максимум', text=str(int(item.production_max)))
            lbl_cost = MDTextField(id='cost', hint_text='Введите цену', text=str(item.cost))
            btn = MDTextButton(text='Изменить', pos_hint={"left_x": .5, "center_y": .5})

        for type in show_all_type_production():
            type_menu_items.append({"viewclass": "ListItem", 'id': f"{type[0]}", 'text': f"{type[1]}",
                                    'on_release': lambda x=ind: self.set_item_type_production(x)})
            ind += 1

        self.type_menu = MDDropdownMenu(
            caller=self.choice_type_production,
            items=type_menu_items,
            position='bottom',
            width_mult=4,
        )
        instance_tab.add_widget(box)
        box.add_widget(lbl_name)
        box.add_widget(self.choice_type_production)
        box.add_widget(lbl_limit_min)
        box.add_widget(lbl_limit_max)
        box.add_widget(lbl_cost)
        box.add_widget(btn)
        btn.bind(on_release=lambda x=self, item=item, instance=instance_tab, name=lbl_name, type=self.choice_type_production,
                                   minn=lbl_limit_min,
                                   maxx=lbl_limit_max, cost=lbl_cost: self.create_production(x, item, instance,name, type, minn, maxx, cost))
        if self.dialog_update_delete:
            self.dialog_update_delete.dismiss()

    def form_for_create_update_animal_type(self, x, instance_tab, item):
        instance_tab.clear_widgets()
        production_menu_items = []
        ind = 0
        box = BoxLayout(orientation='vertical')
        if item is None:
            lbl_name = MDTextField(id='name', hint_text='Введите название', text='')
            lbl_breed = MDTextField(id='breed', hint_text='Введите породу', text='')
            lbl_weight = MDTextField(id='weight', hint_text='Введите вес', text='0')
            lbl_capacity = MDTextField(id='capacity', hint_text='Введите размер', text='0')
            lbl_cost = MDTextField(id='cost', hint_text='Введите цену', text='1')
            lbl_lifespan = MDTextField(id='lifespan', hint_text='Срок жизни', text='10')
            self.choice_production = MenuTextFieldProduction(id='type', hint_text='Выберите тип')
            btn = MDTextButton(text='Создать', pos_hint={"left_x": .5, "center_y": .5})
        else:
            lbl_name = MDTextField(id='name', hint_text='Введите название', text=item.name)
            lbl_breed = MDTextField(id='breed', hint_text='Введите породу', text=item.breed)
            lbl_weight = MDTextField(id='weight', hint_text='Введите вес', text=str(int(item.weight)))
            lbl_capacity = MDTextField(id='capacity', hint_text='Введите размер', text=str(int(item.capacity)))
            lbl_cost = MDTextField(id='cost', hint_text='Введите цену', text=str(item.cost))
            lbl_lifespan = MDTextField(id='lifespan', hint_text='Срок жизни', text=str(item.lifespan))
            self.choice_production = MenuTextFieldProduction(id='type', hint_text='Выберите тип', text=get_production_by_id(item.production_id).name)
            btn = MDTextButton(text='Изменить', pos_hint={"left_x": .5, "center_y": .5})
        for prod in get_all_production():
            production_menu_items.append({"viewclass": "ListItem", 'id': f"{prod.id}",
                                          'text': f"{prod.name}:{get_type_by_id(prod.type_id).name}",
                                          'on_release': lambda x=ind: self.set_item_production(x)})
            ind += 1

        self.production_menu = MDDropdownMenu(
            caller=self.choice_production,
            items=production_menu_items,
            position='bottom',
            width_mult=4,
        )
        instance_tab.add_widget(box)
        box.add_widget(lbl_name)
        box.add_widget(lbl_breed)
        box.add_widget(lbl_weight)
        box.add_widget(lbl_capacity)
        box.add_widget(lbl_cost)
        box.add_widget(lbl_lifespan)
        box.add_widget(self.choice_production)
        box.add_widget(btn)
        btn.bind(on_release=lambda x=self, item=item, instance=instance_tab, name=lbl_name, breed=lbl_breed,
                                   weight=lbl_weight, capacity=lbl_capacity, cost=lbl_cost, lifespan=lbl_lifespan,
                                   production=self.choice_production: self.create_animal_type(x, item, instance, name, breed,
                                                                                              weight, capacity, cost, lifespan,
                                                                                              production))
        if self.dialog_update_delete:
            self.dialog_update_delete.dismiss()
    def choice_animals(self, x, instance_tab):
        menu_items = []
        menu_items_barns = []
        ind = ind_barn = 0

        for type in show_all_animals_types():
            menu_items.append({"viewclass": "ListItem", 'id': f"{type.id}", 'text':f"{type.name}-{type.breed}", 'on_release': lambda x=ind: self.set_item(x)})
            ind+=1
        for barn in self.player.barns:
            menu_items_barns.append({"viewclass": "ListItem", 'id': f"{barn.id}", 'text': f"{barn.name}-{barn.capacity}",
                               'on_release': lambda x=ind_barn: self.set_item_barns(x)})
            ind_barn += 1
        # tmp_widget = self.screen.ids.navigation.ids.finance
        # print(tmp_widget.children)
        # tmp_widget.clear_widgets()
        instance_tab.clear_widgets()
        box = BoxLayout(orientation='vertical')
        #tmp_widget.add_widget(box)
        instance_tab.add_widget(box)
        self.choice_animal_type = MenuTextField(id='add_animal', hint_text='Введите вид животного')
        lbl3 = MDTextField(id='count', hint_text='Введите кол-во', text='1')
        self.choice_barn_for_animals = MenuTextFieldBarns(id='add_barn', hint_text='Выберите хлев для размещения животных')
        box.add_widget(self.choice_animal_type)
        self.menu = MDDropdownMenu(
            caller=self.choice_animal_type,
            items=menu_items,
            position='bottom',
            width_mult=4,
        )
        self.menu_barns = MDDropdownMenu(
            caller=self.choice_barn_for_animals,
            items=menu_items_barns,
            position='bottom',
            width_mult=4,
        )
        box.add_widget(lbl3)
        box.add_widget(self.choice_barn_for_animals)

        btn_buy = MDFlatButton(text='Купить')
        btn_check = MDFlatButton(text='Проверить')
        btn_buy.bind(on_release=lambda x=self,animal_type=self.choice_animal_type, count=lbl3,
                                   barn=self.choice_barn_for_animals: self.buy_animals(x,animal_type, count, barn))
        btn_check.bind(on_release=lambda x=self,  animal_type=self.choice_animal_type, count=lbl3,
                                   barn=self.choice_barn_for_animals: self.show_check_dialog(x,animal_type, count, barn))
        box.add_widget(btn_buy)
        box.add_widget(btn_check)

    def get_text_for_check_dialog(self, player, animal_type, barn, count):
        bool_var = True
        if player.balance<animal_type.cost * count:
            message_1 = f'Не хватает средств'
            bool_var = False
        else:
            message_1 = f'У вас хватит средств на эту покупку'
        if player.get_free_capacity()<animal_type.capacity*count:
            message_2 = (f'В ваших хлевах нет мест для такого кол-ва животных.'
                         f'Нужно строить новый хлев')
            bool_var = False
        else:
            if barn.capacity<animal_type.capacity*count:
                message_2 = (f'В этом хлеву нельзя разместить этих животных.'
                             f'Попробуйте разместит их в другом хлеву '
                             f'или в нескольких. Требуемое место -{animal_type.capacity*count}')
                bool_var = False
            else:
                message_2 = f'Вы можете разместить животных в этом хлеву'
        return message_1, message_2, bool_var


    def show_check_dialog(self,x,animal_type, count, barn):
        self.dialog_check_buy_animals = None
        if get_animal_type_for_id(animal_type.id_item_menu) and get_barn_for_id(barn.id_item_menu):
            text_dialog = self.get_text_for_check_dialog(self.player,get_animal_type_for_id(animal_type.id_item_menu),
                                                 get_barn_for_id(barn.id_item_menu),int(count.text))
            if not self.dialog_check_buy_animals:
                if text_dialog[2]:
                    self.dialog_check_buy_animals = CheckDialog(
                        buttons=[
                            MDFlatButton(
                                text="Купить",
                                theme_text_color="Custom",
                                on_release=lambda instance=self.dialog_check_buy_animals, animal_type=animal_type, count=count,
                                                           barn=barn: self.buy_animals(instance, animal_type,count, barn)

                            ),
                            MDFlatButton(
                                text="Отмена",
                                theme_text_color="Custom",
                                on_release=lambda instance=self.dialog_check_buy_animals: self.on_cancel(instance)
                            ),
                        ],
                    )
                else:
                    self.dialog_check_buy_animals = CheckDialog(
                        buttons=[
                            MDFlatButton(
                                text="Отмена",
                                theme_text_color="Custom",
                                on_release=lambda instance=self.dialog_check_buy_animals: self.on_cancel(instance)
                            ),
                        ],
                    )
            box_lbl = BoxLayout(orientation='vertical')
            self.dialog_check_buy_animals.add_widget(box_lbl)
            box_lbl.add_widget(MDLabel(text=text_dialog[0]))
            box_lbl.add_widget(MDLabel(text=text_dialog[1]))
            self.dialog_check_buy_animals.open()

    def show_sell_production_dialog(self, x):
        self.dialog_sell_prod = None
        if not self.dialog_sell_prod:
            content_lst = [(pr.name, pr.animal, pr.count) for pr in get_productions_sum_by_player(self.player) if pr.count>0]
            content_dialog = SellGrid(content_lst)
            #content_dialog = ItemSellList(content_lst)
            content_dialog.size = [100, len(content_dialog.content_lst)*100]
            self.dialog_sell_prod = MDDialog(
                title="Продажа продукции",
                type="custom",
                #type='confirmation',
                content_cls= content_dialog,
                buttons = [
                    MDFlatButton(
                        text="Продать",
                        theme_text_color="Custom",
                        on_release=lambda instance=self.dialog_sell_prod, content_cls=content_dialog:
                        self.sell_productions(instance, content_dialog)

                    ),
                    MDFlatButton(
                        text="Отмена",
                        theme_text_color="Custom",
                        on_release=lambda instance=self: self.on_cancel_sell_dialog(instance)
                    ),
                ],
            )
            box_lbl = BoxLayout(orientation='vertical')
            self.dialog_sell_prod.add_widget(box_lbl)
            self.dialog_sell_prod.update_height()
            self.dialog_sell_prod.update_width()
            self.dialog_sell_prod.open()

    def set_item(self, ind):
        def set_item(interval):
            self.choice_animal_type.text = self.menu.items[ind]['text']
            self.choice_animal_type.id_item_menu = int(self.menu.items[ind]['id'])
            self.menu.dismiss()
        Clock.schedule_once(set_item, 0.5)

    def set_item_type_production(self, ind):
        def set_item(interval):
            self.choice_type_production.text = self.type_menu.items[ind]['text']
            self.choice_type_production.id_item_menu = int(self.type_menu.items[ind]['id'])
            self.type_menu.dismiss()
        Clock.schedule_once(set_item, 0.5)

    def set_item_production(self, ind):
        def set_item(interval):
            self.choice_production.text = self.production_menu.items[ind]['text']
            self.choice_production.id_item_menu = int(self.production_menu.items[ind]['id'])
            self.production_menu.dismiss()
        Clock.schedule_once(set_item, 0.5)
    def on_cancel(self, instance):
        '''Events called when the "CANCEL" dialog box button is clicked.'''
        self.dialog_check_buy_animals.dismiss()
    def on_cancel_sell_dialog(self, instance):
        '''Events called when the "CANCEL" dialog box button is clicked.'''
        self.dialog_sell_prod.dismiss()
    def on_cancel_update_create_dialog(self, instance):
        '''Events called when the "CANCEL" dialog box button is clicked.'''
        self.dialog_update_delete.dismiss()
    def set_item_barns(self, ind_barn):
        def set_item(interval):
            self.choice_barn_for_animals.text = self.menu_barns.items[ind_barn]['text']
            self.choice_barn_for_animals.id_item_menu = int(self.menu_barns.items[ind_barn]['id'])
            self.menu_barns.dismiss()
        Clock.schedule_once(set_item, 0.5)

    def create_production(self,x,item, instance, name, type, minn, maxx, cost):
        print('CREATE_PROD',instance, type, minn, maxx, cost, name.text, not name.text)
        if (get_type_by_id(type.id_item_menu) is None and type.text is None) or not name.text:
            instance_tab = instance
            instance_tab.clear_widgets()
            instance_tab.add_widget(MDLabel(text=f'Неправильный ввод'))
        else:
            if get_type_by_id(type.id_item_menu):
                production_saver(None,name.text, get_type_by_id(type.id_item_menu).id, int(minn.text), int(maxx.text), float(cost.text))
            else:
                production_saver(item.id, name.text, get_type_by_name(type.text).id, int(minn.text), int(maxx.text), float(cost.text))


    def create_animal_type(self,x,item,instance, name, breed, weight, capacity, cost, lifespan, production):
        print(instance, instance, name, breed, weight, capacity, cost, production)
        if (get_production_by_id(production.id_item_menu) is None and production.text is None) or not name.text  or not breed.text:
            instance_tab = instance
            instance_tab.clear_widgets()
            instance_tab.add_widget(MDLabel(text=f'Неправильный ввод'))
        else:
            if get_production_by_id(production.id_item_menu):
                if animal_type_saver(None, name.text, breed.text, int(weight.text), int(capacity.text), float(cost.text), int(lifespan.text),
                                     get_production_by_id(production.id_item_menu)):
                    print('DONE')
            else:
                if animal_type_saver(item.id, name.text, breed.text, int(weight.text), int(capacity.text), float(cost.text), int(lifespan.text),
                                     get_production_by_name_animal(production.text,'')):
                    print('DONE')

    def delete_item(self, x, instance_tab, item):
        print(instance_tab, instance_tab.id, item)
        if instance_tab.id == 'crud_production':
            if len(item.animal_type)<1:
                delete_production(item.id)
        elif instance_tab.id =='crud_animal_type':
            if len(item.animal)<1:
                delete_animal_type(item.id)


    def buy_animals(self,x,animal_type, count, barn):
        if  get_animal_type_for_id(animal_type.id_item_menu) is None or get_barn_for_id(barn.id_item_menu) is None:
            instance_tab = self.screen.ids.navigation.ids.finance
            instance_tab.clear_widgets()
            instance_tab.add_widget(MDLabel(text=f'Неправильный ввод'))
        elif get_animal_type_for_id(animal_type.id_item_menu).cost*int(count.text)>self.player.balance:
            instance_tab = self.screen.ids.navigation.ids.finance
            instance_tab.clear_widgets()
            instance_tab.add_widget(MDLabel(text=f'Недостаточно средств'))
        elif get_barn_for_id(barn.id_item_menu).capacity<get_animal_type_for_id(animal_type.id_item_menu).capacity*int(count.text):
            instance_tab = self.screen.ids.navigation.ids.finance
            instance_tab.clear_widgets()
            instance_tab.add_widget(MDLabel(text=f'Недостаточно места, нужно покупать хлев'))

        else:
            for c in range(int(count.text)):
                print(animal_type.id_item_menu, barn.id_item_menu, c+1, self.player)
                if animal_saver(animal_type.id_item_menu, barn.id_item_menu, c+1, self.player )[0]:
                    instance_tab = self.screen.ids.navigation.ids.finance
                    self.on_tab_switch(instance_tabs=instance_tab.parent, instance_tab=instance_tab, instance_tab_label='', tab_text='')
                    sleep(0.1)
                else:
                    message = animal_saver(animal_type.id_item_menu, barn.id_item_menu, c+1, self.player)[1]
                    instance_tab = self.screen.ids.navigation.ids.finance
                    instance_tab.clear_widgets()
                    instance_tab.add_widget(MDLabel(text=message))
                    break

        if self.dialog_check_buy_animals:
            self.dialog_check_buy_animals.dismiss()
    def choice_barn(self, x, instance_tab):
        # tmp_widget = self.screen.ids.navigation.ids.finance
        # print(tmp_widget.children)
        # tmp_widget.clear_widgets()
        instance_tab.clear_widgets()
        box = BoxLayout(orientation='vertical')
        #tmp_widget.add_widget(box)
        instance_tab.add_widget(box)
        lbl1 = MDTextField(id='name', hint_text='Введите название')
        lbl2 = MDTextField(id='capacity', hint_text='Введите вместимость (100 или 200')
        box.add_widget(lbl1)
        box.add_widget(lbl2)
        btn = MDFloatingActionButton()
        btn.bind(
            on_release=lambda x=self, name=lbl1, capacity=lbl2: self.build_barn(x, name, capacity))
        box.add_widget(btn)

    def build_barn(self,x,name, capacity):
        if barn_saver(name.text, int(capacity.text), self.player)[0]:
            instance_tab = self.screen.ids.navigation.ids.finance
            self.on_tab_switch(instance_tabs=instance_tab.parent, instance_tab=instance_tab, instance_tab_label='',
                               tab_text='')
        else:
            message = barn_saver(name.text, int(capacity.text), self.player)[1]
            instance_tab = self.screen.ids.navigation.ids.finance
            instance_tab.clear_widgets()
            instance_tab.add_widget(MDLabel(text=message))

    def sell_productions(self, instance, content_dialog):
        sell_dict =dict.fromkeys([cl[0] for cl in content_dialog.content_lst])
        for cl in content_dialog.content_lst:
            pr_cost = get_production_by_name_animal(cl[0], cl[1]).cost
            if not sell_dict[cl[0]]:
                sell_dict[cl[0]] = dict.fromkeys([c[1] for c in content_dialog.content_lst if c[0]==cl[0]], 0)
            sell_dict[cl[0]][cl[1]] = (float(cl[2]), round(random.uniform(pr_cost * 0.9, pr_cost * 1.1), 2))
        for child in content_dialog.children:
            if isinstance(child, MDTextField):
                if float(child.text)>sell_dict[child.id.split(':')[0]][child.id.split(':')[1]][0]:
                    count = sell_dict[child.id.split(':')[0]][child.id.split(':')[1]][0]          #sell_dict[child.id] = int(child.text)
                else:#int(child.text)<0:
                    count = float(child.text)
                if count>0:
                    productions_sell_change(child.id.split(':')[0], count, child.id.split(':')[1], self.player, sell_dict[child.id.split(':')[0]][child.id.split(':')[1]][1])
                    productions_sum_change(child.id.split(':')[0], -count, child.id.split(':')[1], self.player)

        self.dialog_sell_prod.dismiss()

    def on_start_main_menu(self):
        self.sign_up_dialog = None
        self.navigation = Navigation()
        self.screen.ids.main_screen.children[0].children[0].children[1].children[0].children[0].add_widget(
            self.navigation)
        l = self.screen.ids.main_screen.children[0].children[0].children[1].children[0].children[0].children
        self.screen.ids.main_screen.children[0].children[0].children[1].children[0].children[0].remove_widget(l[0])
        content_dialog = ContentSignUpDialog()
        if not self.sign_up_dialog:
            self.sign_up_dialog = MDDialog(
                title="Авторизация или регистрация",
                type="custom",
                content_cls=content_dialog,
                buttons=[
                    MDFlatButton(
                        text="Зайти",
                        theme_text_color="Custom",
                        on_release=lambda instance=self, content_cls=content_dialog:
                        self.autorization(instance, content_cls)

                    ),
                    MDFlatButton(
                        text="Зарегистроваться",
                        theme_text_color="Custom",
                        on_release=lambda instance=self: self.registration(instance)
                    ),
                    MDFlatButton(
                        text="Отмена",
                        theme_text_color="Custom",
                        on_release=lambda instance=self: self.on_cancel_sign_up_dialog(instance)
                    ),
                ],
            )
            self.sign_up_dialog.open()

    def autorization(self, instance, content):
        self.wrong_autorization_dialog = None
        print(instance, content, content)
        adict = {}
        for child in content.children:
            adict[child.name] = child.text
        if player_autorization(adict['nickname'], adict['password']):
            self.player = player_autorization(adict['nickname'], adict['password'])
            self.on_cancel_sign_up_dialog(instance)
        else:
            if not self.wrong_autorization_dialog:
                self.wrong_autorization_dialog=MDDialog(
                    title="Ошибка",
                    type="custom",
                    text="Ошибка входа, проверьте данные или зарегистируйтесь",
                    buttons=[
                        MDFlatButton(
                            text="OK",
                            theme_text_color="Custom",
                            on_release=lambda instance=self: self.on_cancel_wrong_autorization_dialog(instance)
                        ),
                    ],
                )
                self.wrong_autorization_dialog.open()

    def registration(self, instance):
        self.on_cancel_sign_up_dialog(instance)
        self.registration_dialog = None
        self.screen.ids.main_screen.children[0].clear_widgets()
        content_dialog = ContentSignUpDialog()
        if not self.registration_dialog:
            self.registration_dialog = MDDialog(
                title="Введите ник и пароль",
                type="custom",
                content_cls=content_dialog,
                buttons=[
                    MDFlatButton(
                        text="Зарегистроваться",
                        theme_text_color="Custom",
                        on_release=lambda instance=self.dialog_sell_prod, content_cls=content_dialog:
                        self.check_data_registration(instance, content_dialog)

                    ),
                    MDFlatButton(
                        text="Отмена",
                        theme_text_color="Custom",
                        on_release=lambda instance=self: self.on_cancel_registration_dialog(instance)
                    ),
                ],
            )
            self.registration_dialog.open()
        self.navigation = Navigation()

        self.screen.ids.main_screen.children[0].add_widget(self.navigation)


    def check_data_registration(self, instance, content):
        self.wrong_registration_dialog = None
        adict = {}
        for child in content.children:
            adict[child.name] = child.text
        tmp_player = player_registration(adict['nickname'], adict['password'])[0]
        if tmp_player:
            self.screen.ids.main_screen.children[0].clear_widgets()
            self.player =  tmp_player
            self.on_cancel_registration_dialog(instance)
            self.navigation = Navigation()
            self.screen.ids.main_screen.children[0].add_widget(self.navigation)
        else:
            if not self.wrong_registration_dialog:
                self.wrong_registration_dialog=MDDialog(
                    title="Ошибка",
                    type="custom",
                    text=player_registration(adict['nickname'], adict['password'])[1],
                    buttons=[
                        MDFlatButton(
                            text="OK",
                            theme_text_color="Custom",
                            on_release=lambda instance=self: self.on_cancel_wrong_registration_dialog(instance)
                        ),
                    ],
                )
                self.wrong_registration_dialog.open()

    def on_cancel_sign_up_dialog(self, instance):
        '''Events called when the "CANCEL" dialog box button is clicked.'''
        self.sign_up_dialog.dismiss()
    def on_cancel_registration_dialog(self, instance):
        '''Events called when the "CANCEL" dialog box button is clicked.'''
        self.registration_dialog.dismiss()
    def on_cancel_wrong_autorization_dialog(self, instance):
        '''Events called when the "CANCEL" dialog box button is clicked.'''
        self.wrong_autorization_dialog.dismiss()
    def on_cancel_wrong_registration_dialog(self, instance):
        '''Events called when the "CANCEL" dialog box button is clicked.'''
        self.wrong_registration_dialog.dismiss()

    def on_start(self):
        icons_item_menu_lines = {
            "account-cowboy-hat": "About author",
            "github": "Rules",
            "share-variant": "Autorization",
        }

        for icon_name in icons_item_menu_lines.keys():
            self.screen.ids.navigation.ids.content_drawer.ids.md_drawer_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item_menu_lines[icon_name], on_release=self.choice_drawer_menu)
            )

    def choice_drawer_menu(self, instance_item):
        if instance_item.text == 'Autorization':
            self.on_start_main_menu()
        elif instance_item.text == 'Rules':
            self.rules()
        elif instance_item.text == 'About author':
            self.about_author()
    def rules(self):
        self.navigation = Navigation()
        self.screen.ids.main_screen.children[0].children[0].children[1].children[0].children[0].add_widget(self.navigation)
        l = self.screen.ids.main_screen.children[0].children[0].children[1].children[0].children[0].children
        self.screen.ids.main_screen.children[0].children[0].children[1].children[0].children[0].remove_widget(l[0])
        box = BoxLayout(orientation='vertical')
        text_rules = MDLabel(text="""
            PARAMETERS:
            widget: Widget
            Widget to add to our list of children.
            
            index: int, defaults to 0
            Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibling widgets. For a full discussion of the index and widget hierarchy, please see the Widgets Programming Guide.
            
            New in version 1.0.5.
            
            canvas: str, defaults to None
            Canvas to add widget’s canvas to. Can be ‘before’, ‘after’ or None for the default canvas.
            
            New in version 1.9.0.       
        """,
        halign='center'
        )
        self.screen.ids.main_screen.children[0].children[0].children[1].children[0].children[0].add_widget(box)
        box.add_widget(text_rules)
        box.add_widget(MDLabel())

    def about_author(self):
        print('self', self.author_name)
        self.navigation = Navigation()
        self.screen.ids.main_screen.children[0].children[0].children[1].children[0].children[0].add_widget(
            self.navigation)
        l = self.screen.ids.main_screen.children[0].children[0].children[1].children[0].children[0].children
        self.screen.ids.main_screen.children[0].children[0].children[1].children[0].children[0].remove_widget(l[0])
        box = BoxLayout(orientation='vertical')
        name_author_lbl = MDLabel(text=f'Автор игры: {self.author_name}',halign='center',
                                  pos_hint={'center_x':0.5, 'center_y':0.5})
        self.screen.ids.main_screen.children[0].children[0].children[1].children[0].children[0].add_widget(box)
        box.add_widget(name_author_lbl)
        box.add_widget(MDLabel())


if __name__ == '__main__':
    FarmSimApp().run()

