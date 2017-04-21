# -*- coding: utf-8 -*-
import time

__all__ = ["Notification", "AndroidNotification", "IosNotification"]


class AndPayload(object):
    __slots__ = ('display_type', 'body', 'extra')

    def __int__(self):
        pass


class AndBody(object):
    __slots__ = ("ticker", "title", "text", "icon", "largeIcon", "img", "sound",
                 "builder_id", "play_vibrate", "play_lights", "play_sound", "after_open",
                 "url", "activity", "custom")

    def __init__(self):
        pass


class IosPayload(object):
    __slots__ = ('aps', 'jumpkey', 'extra')

    def __init__(self):
        pass


class IosAps(object):
    __slots__ = ('alert', 'badge', 'sound', 'content_available', 'category')

    def __init__(self):
        pass


class Policy(object):
    __slots__ = ('start_time', 'expire_time', 'max_send_num', 'out_biz_no', 'apns_collapse_id')

    def __int__(self):
        pass


class Notification(object):
    __slots__ = ('appkey', 'master_screte', 'type', 'device_tokens', 'alias_type', 'alias',
                 'file_id', 'filter', 'production_mode', 'description', 'thirdparty_id',
                 'body', 'payload', 'policy')

    def __init__(self, app_key, master_secret, ptype):
        self.appkey = app_key
        self.master_screte = master_secret
        self.type = ptype
        # self.filter = {}
        self.production_mode = "true"
        self.policy = Policy()

    def to_json(self):
        raise NotImplementedError()

    @property
    def start_time(self):
        return self.policy.start_time

    @start_time.setter
    def start_time(self, v):
        self.policy.start_time = v

    @property
    def expire_time(self):
        return self.policy.expire_time

    @expire_time.setter
    def expire_time(self, v):
        self.policy.expire_time = v

    @property
    def max_send_num(self):
        return self.policy.max_send_num

    @max_send_num.setter
    def max_send_num(self, v):
        self.policy.max_send_num = v


class AndroidNotification(Notification):

    def __init__(self, app_key, master_secret, ptype):
        super(AndroidNotification, self).__init__(app_key, master_secret, ptype)
        self.payload = AndPayload()
        self.payload.body = self.body = AndBody()

    def to_json(self):
        body = {k: getattr(self.body, k) for k in self.body.__slots__
                if getattr(self.body, k, None) is not None}
        policy = {k: getattr(self.policy, k) for k in self.policy.__slots__
                  if getattr(self.policy, k, None) is not None}
        payload = {k: getattr(self.payload, k) for k in self.payload.__slots__
                   if getattr(self.payload, k, None) is not None}
        data = {k: getattr(self, k) for k in self.__slots__
                if getattr(self, k, None) is not None}

        del data['master_screte']
        del data['body']
        del data['policy']

        data['payload'] = payload
        data['payload']['body'] = body
        data['timestamp'] = int(time.time() * 1000)

        if policy:
            data['policy'] = policy

        return data

    @property
    def out_biz_no(self):
        return self.policy.out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, v):
        self.policy.out_biz_no = v

    @property
    def display_type(self):
        return self.payload.display_type

    @display_type.setter
    def display_type(self, v):
        self.payload.display_type = v

    @property
    def ticker(self):
        return self.body.ticker

    @ticker.setter
    def ticker(self, v):
        self.body.ticker = v

    @property
    def title(self):
        return self.body.title

    @title.setter
    def title(self, v):
        self.body.title = v

    @property
    def text(self):
        return self.body.text

    @text.setter
    def text(self, v):
        self.body.text = v

    @property
    def icon(self):
        return self.body.icon

    @icon.setter
    def icon(self, v):
        self.body.icon = v

    @property
    def largeIcon(self):
        return self.body.largeIcon

    @largeIcon.setter
    def largeIcon(self, v):
        self.body.largeIcon = v

    @property
    def img(self):
        return self.body.img

    @img.setter
    def img(self, v):
        self.body.img = v

    @property
    def sound(self):
        return self.body.sound

    @sound.setter
    def sound(self, v):
        self.body.sound = v

    @property
    def builder_id(self):
        return self.body.builder_id

    @builder_id.setter
    def builder_id(self, v):
        self.body.builder_id = v

    @property
    def play_vibrate(self):
        return self.body.play_vibrate

    @play_vibrate.setter
    def play_vibrate(self, v):
        self.body.play_vibrate = v

    @property
    def play_sound(self):
        return self.body.play_sound

    @play_sound.setter
    def play_sound(self, v):
        self.body.play_sound = v

    @property
    def play_lights(self):
        return self.body.play_lights

    @play_lights.setter
    def play_lights(self, v):
        self.body.play_lights = v

    @property
    def after_open(self):
        return self.body.after_open

    @after_open.setter
    def after_open(self, v):
        self.body.after_open = v

    @property
    def url(self):
        return self.body.url

    @url.setter
    def url(self, v):
        self.body.url = v

    @property
    def activity(self):
        return self.body.activity

    @activity.setter
    def activity(self, v):
        self.body.activity = v

    @property
    def custom(self):
        return self.body.custom

    @custom.setter
    def custom(self, v):
        self.body.custom = v

    @property
    def extra(self):
        return self.payload.extra

    @extra.setter
    def extra(self, v):
        self.payload.extra = v


class IosNotification(Notification):

    def __init__(self, app_key, master_secret, ptype):
        super(IosNotification, self).__init__(app_key, master_secret, ptype)
        self.payload = IosPayload()
        self.payload.aps = self.aps = IosAps()

    def to_json(self):
        aps = {k: getattr(self.aps, k) for k in self.aps.__slots__
               if getattr(self.aps, k, None) is not None}
        policy = {k: getattr(self.policy, k) for k in self.policy.__slots__
                  if getattr(self.policy, k, None) is not None}
        payload = {k: getattr(self.payload, k) for k in self.payload.__slots__
                   if getattr(self.payload, k, None) is not None}
        data = {k: getattr(self, k) for k in self.__slots__
                if getattr(self, k, None) is not None}

        del data['master_screte']
        del data['payload']
        del data['policy']

        if 'content_available' in aps:
            aps['content-available'] = aps.pop('content_available')

        data['payload'] = payload
        data['payload']['aps'] = aps
        data['timestamp'] = int(time.time() * 1000)

        if policy:
            if 'apns_collapse_id' in policy:
                policy['apns-collapse-id'] = policy.pop('apns_collapse_id')
            data['policy'] = policy

        return data

    @property
    def apns_collapse_id(self):
        return self.policy.apns_collapse_id

    @apns_collapse_id.setter
    def apns_collapse_id(self, v):
        self.policy.apns_collapse_id = v

    @property
    def jumpkey(self):
        return self.payload.jumpkey

    @jumpkey.setter
    def jumpkey(self, v):
        self.payload.jumpkey = v

    @property
    def extra(self):
        return self.payload.extra

    @extra.setter
    def extra(self, v):
        self.payload.extra = v

    @property
    def alert(self):
        return self.aps.alert

    @alert.setter
    def alert(self, v):
        self.aps.alert = v

    @property
    def badge(self):
        return self.aps.badge

    @badge.setter
    def badge(self, v):
        self.aps.badge = v

    @property
    def sound(self):
        return self.aps.sound

    @sound.setter
    def sound(self, v):
        self.aps.sound = v

    @property
    def content_available(self):
        return self.aps.content_available

    @content_available.setter
    def content_available(self, v):
        self.aps.content_available = v

    @property
    def category(self):
        return self.aps.category

    @category.setter
    def category(self, v):
        self.aps.category = v
