class GlobalConfig:
    login_url = ''
    replies_url = 'https://x.com/i/api/graphql/QB8r8Y04-pRe9v5QROfMcw/UserTweetsAndReplies'
    delete_url = 'https://x.com/i/api/graphql/VaenaVgh5q5ih7kvyVjgtg/DeleteTweet'

    delete_query_id = 'VaenaVgh5q5ih7kvyVjgtg'

    page_size = 20

    proxy = ''


def request_login_url():
    return GlobalConfig.login_url


def request_replies_url():
    return GlobalConfig.replies_url


def request_delete_url():
    return GlobalConfig.delete_url


def request_delete_query_id():
    return GlobalConfig.delete_query_id


def request_page_size():
    return GlobalConfig.page_size


def request_proxy():
    if GlobalConfig.proxy is None or len(GlobalConfig.proxy) == 0:
        return None
    return GlobalConfig.proxy


def request_header(authorization, cookie, token):
    headers = {
        'authorization': authorization,
        'cookie': cookie,
        'x-csrf-token': token
    }
    return headers
