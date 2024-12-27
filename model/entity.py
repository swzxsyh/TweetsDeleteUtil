class PreData(object):
    def __init__(self, user_id, authorization, cookie, x_csrf_token):
        self.user_id = user_id
        self.authorization = authorization
        self.cookie = cookie
        self.x_csrf_token = x_csrf_token


class UserTweetsAndReplies(object):
    def __init__(self, variables):
        self.variables = variables
        self.features = UserTweetsAndRepliesFeatures()
        self.fieldToggles = UserTweetsAndRepliesFieldToggles()

    def to_dict(self):
        return {
            "variables": vars(self.variables),
            "features": vars(self.features),
            "fieldToggles": vars(self.fieldToggles),
        }


class UserTweetsAndRepliesVariables(object):
    def __init__(self, userId, count, cursor):
        self.userId = userId
        self.count = count
        self.cursor = cursor
        self.includePromotedContent = False
        self.withCommunity = False
        self.withVoice = False
        self.withV2Timeline = False


class UserTweetsAndRepliesFeatures:
    def __init__(self):
        self.profile_label_improvements_pcf_label_in_post_enabled = False
        self.rweb_tipjar_consumption_enabled = False
        self.responsive_web_graphql_exclude_directive_enabled = False
        self.verified_phone_label_enabled = False
        self.creator_subscriptions_tweet_preview_api_enabled = False
        self.responsive_web_graphql_timeline_navigation_enabled = False
        self.responsive_web_graphql_skip_user_profile_image_extensions_enabled = False
        self.premium_content_api_read_enabled = False
        self.communities_web_enable_tweet_community_results_fetch = False
        self.c9s_tweet_anatomy_moderator_badge_enabled = False
        self.responsive_web_grok_analyze_button_fetch_trends_enabled = False
        self.responsive_web_grok_analyze_post_followups_enabled = False
        self.articles_preview_enabled = False
        self.responsive_web_edit_tweet_api_enabled = False
        self.graphql_is_translatable_rweb_tweet_is_translatable_enabled = False
        self.view_counts_everywhere_api_enabled = False
        self.longform_notetweets_consumption_enabled = False
        self.responsive_web_twitter_article_tweet_consumption_enabled = False
        self.tweet_awards_web_tipping_enabled = False
        self.creator_subscriptions_quote_tweet_preview_enabled = False
        self.freedom_of_speech_not_reach_fetch_enabled = False
        self.standardized_nudges_misinfo = False
        self.tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled = False
        self.rweb_video_timestamps_enabled = False
        self.longform_notetweets_rich_text_read_enabled = False
        self.longform_notetweets_inline_media_enabled = False
        self.responsive_web_enhance_cards_enabled = False


class UserTweetsAndRepliesFieldToggles:
    def __init__(self):
        self.withArticlePlainText = False


class ReplyResponse(object):
    def __init__(self, ids, cursor):
        self.ids = ids
        self.cursor = cursor


class DeleteRequest(object):
    def __init__(self, queryId, variables):
        self.queryId = queryId
        self.variables = variables

    def to_dict(self):
        return {
            "queryId": self.queryId,
            "variables": vars(self.variables),
        }


class DeleteVariables(object):
    def __init__(self, dark_request, tweet_id):
        self.dark_request = dark_request
        self.tweet_id = tweet_id
