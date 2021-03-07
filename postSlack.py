#coding: UTF-8
import slackweb
import qiita

slack = slackweb.Slack(url="https://hooks.slack.com/services/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")

text = qiita.createText()
slack.notify(text=text)