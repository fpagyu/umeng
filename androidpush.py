# -*- coding: utf-8 -*-
from pica.utils.umeng.notification import AndroidNotification


class AndroidPush(AndroidNotification):

    def __init__(self, app_key, master_secret):
        super(AndroidPush, self).__init__(app_key, master_secret, "customizedcast")
        self.alias_type = "user_id"
        self.payload.display_type = 'notification'
        self.payload.body.after_open = 'go_custom'

    @property
    def user_id(self):
        return self.alias

    @user_id.setter
    def user_id(self, user_id):
        if isinstance(user_id, (tuple, list)):
            self.alias = ','.join([str(x) for x in user_id])
        else:
            self.alias = str(user_id)
