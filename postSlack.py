#coding: UTF-8
import slackweb
import qiita

# Slack送信準備
slack = slackweb.Slack(url="https://hooks.slack.com/services/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")

# Slack送信用のテキスト作成
text = qiita.createText()

# Slackにtextを送信 
slack.notify(text=text)