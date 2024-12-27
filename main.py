# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import delete
import fetch
import login_data

user_name = ''
password = ''

total = 100

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # get necessary header do next step
    pre_data = login_data.login(name=user_name, password=password)
    # fetch replies until less than page size or size == total
    reply_ids = fetch.fetch_replies(pre_data, total)
    # do delete action
    delete.delete_ids(pre_data, reply_ids)