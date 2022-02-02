import io
import pygame as pg
import pygame_widgets

from search_map_utils import get_organization, org_coord
from static_api_utils import get_static
from pygame_widgets.combobox import ComboBox

pg.init()
SIZE = (600, 450)
sloi = {'map': 'map', 'sat': 'sat', 'skl': 'skl'}


class MapApp:
    def __init__(self, coord):
        self.coord = coord
        self.z = 18
        self.map = None
        self.update_map('map')

    def update_map(self, l='map'):
        params = dict(
            ll=','.join(map(str, self.coord)),
            z=self.z,
            l=l
        )
        self.map = io.BytesIO(get_static(**params))

    def draw(self, surf):
        surf.blit(pg.image.load(self.map), (0, 0))

    def page_up(self):
        if self.z <= 20:
            self.z += 1
        pass

    def page_down(self):
        if self.z > 0:
            self.z -= 1
        pass


def main():
    address = 'миасс ддт юность'
    coord = org_coord(get_organization(address))
    pg.init()
    screen = pg.display.set_mode(SIZE)
    comboBox = ComboBox(
        screen, 0, 0, 200, 25, name='Select Color',
        choices=sloi,
        maxResults=3,
        font=pg.font.SysFont('calibri', 15),
        borderRadius=15, colour=(255, 255, 255), direction='down',
        textHAlign='left'
    )
    app = MapApp(coord)

    running = True
    while running:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_PAGEUP:
                    app.page_up()
                elif event.key == pg.K_PAGEDOWN:
                    app.page_down()
                elif event.key == pg.K_UP:
                    if coord[1] < 85:
                        coord[1] += 0.5
                    print(coord)
                elif event.key == pg.K_DOWN:
                    if coord[1] > -85:
                        coord[1] -= 0.5
                    print(coord)
                elif event.key == pg.K_RIGHT:
                    if coord[0] < 175:
                        coord[0] += 0.5
                    print(coord)
                elif event.key == pg.K_LEFT:
                    if coord[0] > -175:
                        coord[0] -= 0.5
                    print(coord)
        if comboBox.getText() in ['map', 'sat', 'skl']:
            app.update_map(comboBox.getText())
        else:
            app.update_map()
        app.draw(screen)
        pygame_widgets.update(events)
        pg.display.update()


main()
