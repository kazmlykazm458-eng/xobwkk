[app]
title = InstaBoost Pro
package.name = instaboost
package.domain = com.pro.tools
source.dir = .
source.include_exts = py,png,jpg,kv,txt,atlas
version = 1.1

requirements = python3,kivy==2.2.1,requests,urllib3,certifi,chardet,idna

android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.0
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1

