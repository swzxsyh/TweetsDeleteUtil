import json
import logging

from model.entity import ReplyResponse


def decode_replies(user_id, response_data):
    data = json.loads(response_data.content)
    instructions = data['data']['user']['result']['timeline']['timeline']['instructions']

    timeline_entries = None

    for reply in instructions:
        if reply['type'] == 'TimelineAddEntries':
            timeline_entries = reply['type']
            break

    if timeline_entries is None:
        return []

    entries = timeline_entries['entries']

    ids = entries_ids(entries)
    cursor = next_page_cursor(entries)

    if len(ids) == 0 or cursor is None:
        return None

    return ReplyResponse(ids, cursor)


def entries_ids(entries):
    lst = []
    try:
        for entry in entries:
            items = entry['content']['items']
            for item in items:
                legacy = item['item']['itemContent']['tweet_results']['result']['legacy']
                if legacy['user_id_str'] != user_id:
                    continue
                if legacy['favorite_count'] == 0 or legacy['quote_count'] == 0 or legacy['reply_count'] == 0 or legacy[
                    'retweet_count'] == 0:
                    lst.append(legacy['id_str'])
    except Exception as err:
        logging.error("entries_ids err:", err)

    return lst


def next_page_cursor(entries):
    result = None
    try:
        for entry in entries:
            if entry['entryId'].startswith("cursor-bottom-"):
                result = entry['content']['value']
                break
    except Exception as err:
        logging.error("next_page_cursor err:", err)

    return result
