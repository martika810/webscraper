from crawler.progress import read_total_number_items,init, \
    read_number_items_scraped_so_far,save_number_items_scraped_so_far, save_total_number_items

def test_read_total_number_items():

    total_number_items = read_total_number_items()
    assert total_number_items == 0


def test_save_number_items_scraped_so_far():
    init()
    total_number_items = read_total_number_items()
    items_scraped_so_far = read_number_items_scraped_so_far()
    assert total_number_items == 0
    assert items_scraped_so_far == 0

    save_number_items_scraped_so_far(10)
    save_total_number_items(5)
    items_scraped_so_far = read_number_items_scraped_so_far()
    total_number_items = read_total_number_items()
    assert items_scraped_so_far == 10
    assert total_number_items