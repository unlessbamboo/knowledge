#!/usr/bin/env python
#coding:utf8
import datetime


g_future_str = "2017-01-01 19:00:00"


def detectTimeDiff():
    """detectTimeDiff:检测距离2017.1.1还有多长时间"""
    future_dt = datetime.datetime.strptime(
        g_future_str, "%Y-%m-%d %H:%M:%S")
    now_dt = datetime.datetime.now()

    if now_dt > future_dt:
        print 'Oh, shit!'
    elif now_dt == future_dt:
        print 'Don\'t lie.'
    else:
        dt_diff = future_dt - now_dt
        print "==================时光机================="
        print '''\t天数剩余：{0}\n\t秒数剩余：{1}'''.format(
            dt_diff.days, dt_diff.seconds)
        print "=================(x_x)=================="


if __name__ == '__main__':
    """main"""
    detectTimeDiff()
