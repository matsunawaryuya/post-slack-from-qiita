# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json

def createText():
  url = "https://qiita.com"

  headers = {
    "User-Agent" : "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
  }

  res = requests.get(url, headers=headers)

  # htmlをBeautifulSoupで取得
  soup = BeautifulSoup(res.text, "html.parser")

  # トレンド情報があるscriptタグを取得
  trend_tag = soup.find("script", attrs={'data-component-name': "HomeArticleTrendFeed"})

  # scriptタグの中のjsonを取得し、トレンド情報が入った配列を取得
  trend_array = json.loads(trend_tag.string)['trend']['edges']

  text = ""

  for item in trend_array:
    text += "```\n"
    text += '<' + json.dumps(item['node']['linkUrl'], ensure_ascii=False).strip('"') + '|' + json.dumps(item['node']['title'], ensure_ascii=False).strip('"') + '>\n'
    # text += '<' + item.find("a", class_="css-1j37wyh").get("href") + '|' + item.find("a", class_="css-1j37wyh").text + '>\n'
    text += "by " + json.dumps(item['node']['author']['displayName'], ensure_ascii=False).strip('"') + " LGTM " + json.dumps(item['node']['likesCount'], ensure_ascii=False) + '\n'
    text += "```\n\n"

  text = "*今日のトレンド*" + '\n \n' + text

  return text
