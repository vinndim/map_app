import io
import pygame as pg
from search_map_utils import get_organization, org_coord
from static_api_utils import get_static

SIZE = (600, 450)


class MapApp:
    def __init__(self, coord, z=10):
        self.coord = coord
        self.z = z
        self.map = None

    def update_map(self):
        params = dict(
            ll=', '.join(map(str, self.coord)),
            z=self.z,
            l='map'
        )
        self.map = io.BytesIO(get_static(**params))

    def draw(self, surf):
        surf.blit(self.map, (0, 0))


def main():
    address = 'миасс ддт юность'
    coord = org_coord(get_organization(address))
    app = MapApp(coord)

    pg.init()
    screen = pg.display.set_mode(SIZE)
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
