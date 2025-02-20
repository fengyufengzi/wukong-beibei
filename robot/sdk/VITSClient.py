# coding: utf-8
# !/usr/bin/env python3

"""VITS TTS API"""

import requests


def tts(text, server_url, api_key, prompt_text, timeout):
    data = {
        "id" : 0,
        "text": text,        
        "prompt_lang":"auto",
        "lang": "auto",
        "prompt_text":prompt_text,
        "preset":"default"
    }
    headers = {"X-API-KEY": api_key}
    url = f"{server_url}/voice/gpt-sovits?id=0&prompt_lang=auto&prompt_text={prompt_text}preset=default&text={text}"
    res = requests.get(url=url, data=data, headers=headers, timeout=timeout)
    res.raise_for_status()
    return res.content

# def tts(text, server_url, api_key, speaker_id, length, noise, noisew, max, timeout):
#     data = {
#         "text": text,
#         "id": speaker_id,
#         "format": "wav",
#         "lang": "auto",
#         "length": length,
#         "noise": noise,
#         "noisew": noisew,
#         "max": max
#     }
#     headers = {"X-API-KEY": api_key}
#     url = f"{server_url}/voice"
#     res = requests.post(url=url, data=data, headers=headers, timeout=timeout)
#     res.raise_for_status()
#     return res.content
