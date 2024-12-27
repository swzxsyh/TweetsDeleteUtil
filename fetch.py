import logging
import time

import requests

import config
import decode_util
from model.entity import UserTweetsAndReplies, UserTweetsAndRepliesVariables


def fetch_replies(pre_data, total):
    url = config.request_replies_url()
    page_size = config.request_page_size()
    proxy = config.request_proxy()

    user_id = pre_data.user_id

    necessary_headers = config.request_header(pre_data.authorization, pre_data.cookie, pre_data.x_csrf_token)

    all_ids = []
    request_body = build_replies_request_body(user_id, page_size, None)

    while len(all_ids) < total:
        response = requests.get(url, headers=necessary_headers, params=request_body, proxies=proxy)
        if response.status_code != 200:
            logging.error("fetch page error")
            break
        decode_result = decode_util.decode_replies(user_id, response.content)
        if decode_result is not None and len(decode_result.ids) > 0:
            all_ids.append(decode_result.ids)
        if decode_result is None or len(decode_result.ids) < page_size:
            break
        # cursor find next page
        request_body = build_replies_request_body(user_id, page_size, decode_result.cursor)
        # avoid be robot
        time.sleep(5)

    return all_ids


def build_replies_request_body(user_id, count, cursor):
    variables = UserTweetsAndRepliesVariables(user_id, count, cursor)
    return UserTweetsAndReplies(variables)
