import folium_map


class TestUrlProducer:

    def test_return_image_one():
        assert folium_map.url_producer(500) == 'icons/vol1.png'

    def test_return_image_two():
        assert folium_map.url_producer(1500) == 'icons/vol2.png'

    def test_return_image_three():
        assert folium_map.url_producer(5000) == 'icons/vol3.png'
