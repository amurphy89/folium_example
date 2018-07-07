import folium_map


class TestUrlProducer:

    def test_return_image_one(self):
        assert folium_map.url_producer(500) == 'icons/vol1.png'

    def test_return_image_two(self):
        assert folium_map.url_producer(1500) == 'icons/vol2.png'

    def test_return_image_three(self):
        assert folium_map.url_producer(5000) == 'icons/vol3.png'
