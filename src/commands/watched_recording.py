from src.utils.find_and_delete_recordings import find_and_delete_recordings
from src.utils.timer import delete_timers, find_timer_ids
from src.utils.KodiResource import KodiResource


def watched_recording():
    kodi = KodiResource()
    item_dict = kodi.player_get_item()

    title = item_dict['title']
    plot = item_dict['plot']

    if title == "":
        print("Current Kodi player doesn't have a title")
    else:
        find_and_delete_recordings(title, plot=plot)

        timer_ids = find_timer_ids(title, kodi)
        if len(timer_ids) > 0:
            print("deleting : ", title)
            delete_timers(timer_ids, kodi)

        print(title, plot)
    return title