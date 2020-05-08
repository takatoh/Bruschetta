# coding: utf-8

from datetime import datetime, timedelta, tzinfo


class UTC(tzinfo):
    def utcoffset(self, dt):
        return timedelta(0)

    def dst(self, dt):
        return timedelta(0)

    def tzname(self, dt):
        return "UTC"


class JST(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=9)

    def dst(self, dt):
        return timedelta(0)

    def tzname(self, dt):
        return "JST"


if __name__ == '__main__':
    utc_now = datetime.utcnow()
    print(utc_now)

    jst_now = utc_now.replace(tzinfo=UTC()).astimezone(JST())
    print(jst_now)
