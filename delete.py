import logging
import time

import requests

import config
from model.entity import DeleteVariables, DeleteRequest


def delete_ids(pre_data, reply_ids):
    del_url = config.request_delete_url()
    delete_query_id = config.request_delete_query_id()
    proxy = config.request_proxy()

    necessary_headers = config.request_header(pre_data.authorization, pre_data.cookie, pre_data.x_csrf_token)

    if reply_ids is not None:
        for current_tweet_id in reply_ids:

            variables = DeleteVariables(dark_request=False, tweet_id=current_tweet_id)
            # create DeleteRequest instance
            request = DeleteRequest(queryId=delete_query_id, variables=variables)
            # avoid be robot
            time.sleep(3)
            delete_resp = requests.post(url=del_url, headers=necessary_headers, params=request, proxies=proxy)
            if delete_resp.status_code == 200:
                logging.info("delete success:{}", current_tweet_id)
