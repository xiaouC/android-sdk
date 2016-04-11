#! /usr/bin/python
# -*- coding:utf-8 -*-
'''
# Filename      : ./android-sdk/rules_pokemon.py
# Description   :
# Last modified : 2016-03-21 10:28
'''
# coding: utf-8
from processor import register, Rule


class RuleBase(Rule):
    VERSION_CODE = '100000'
    VERSION_NAME = '1.00000'
    APPNAME = ''
    APPLABEL = 'pokemon'
    ICON_PATH = '../../../pokemon_icons/android'
    UMENG_APPKEY = '5682058be0f55a0ec8003010'
    CHANNEL_ID = 'empty'

    BASE_SDK_VERSION = """
    <uses-sdk android:minSdkVersion="8" android:targetSdkVersion="18"/>
    """

    BASE_PERMISSION = """
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <uses-permission android:name="android.permission.WAKE_LOCK" />
    <uses-permission android:name="android.permission.READ_LOGS" />
    <uses-permission android:name="android.permission.DUMP" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.GET_TASKS" />
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
    <uses-permission android:name="android.permission.VIBRATE"/>
    """

    NATIVE_MAIN_BOOT = True
    BASE_ACTIVITY = """
        <activity android:name="org.yy.poem"
                  android:label="@string/app_name"
                  android:screenOrientation="landscape"
                  android:theme="@android:style/Theme.NoTitleBar.Fullscreen"
                  android:configChanges="keyboardHidden|orientation|screenSize|layoutDirection">
        """ + ("" if not NATIVE_MAIN_BOOT else """
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        """) + """
        </activity>

        <activity android:name="org.yy.VideoActivity"
            android:label="@string/app_name"
            android:screenOrientation="landscape"
            android:configChanges="keyboardHidden|orientation|screenSize|layoutDirection">
            >
            <intent-filter>
                <action android:name="org.yy.VideoActivity" />
                <category android:name="android.intent.category.DEFAULT"/>
            </intent-filter>
        </activity>

        <receiver android:name="org.yy.PushReceiver" >
            <intent-filter android:priority="2147483647" >
                <action android:name="android.intent.action.BOOT_COMPLETED"/>
                <category android:name="android.intent.category.DEFAULT" />
                <action android:name="android.intent.action.USER_PRESENT"/>
            </intent-filter>
        </receiver>

        <service
            android:name="org.yy.PushService"
            android:enabled="true"
            />
    """


@register
class RuleEmpty(RuleBase):
    LABEL = 'empty'
    DIRECTORY = 'empty'
    CH_NAME = '神奇小精灵加强版'
    SDKTYPE = 'YY'
    PACKAGE_NAME = 'com.winnergame.pokemon.empty'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.empty'
    CHANNEL_ID = 'empty'
