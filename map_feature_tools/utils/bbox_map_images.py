class MapillaryMap():
    def __init__(self, min_lat: float, max_lat: float, min_lon: float, max_lon: float) -> None:
        self.min_lat = min_lat
        self.max_lat = max_lat
        self.min_lon = min_lon
        self.max_lon = max_lon

    def get_images_in_bbox(self) -> list:
        pass