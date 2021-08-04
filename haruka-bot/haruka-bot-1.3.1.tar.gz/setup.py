# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src\\plugins'}

packages = \
['haruka_bot',
 'haruka_bot.cli',
 'haruka_bot.database',
 'haruka_bot.libs',
 'haruka_bot.plugins',
 'haruka_bot.plugins.at',
 'haruka_bot.plugins.dynamic',
 'haruka_bot.plugins.live',
 'haruka_bot.plugins.permission',
 'haruka_bot.plugins.pusher',
 'haruka_bot.plugins.sub',
 'haruka_bot.utils']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4.4,<2.0.0',
 'click>=8.0.1,<9.0.0',
 'httpx>=0.18.2,<0.19.0',
 'nonebot-adapter-cqhttp>=2.0.0-alpha.14,<3.0.0',
 'nonebot-plugin-apscheduler>=0.1.2,<0.2.0',
 'nonebot2>=2.0.0-alpha.14,<3.0.0',
 'packaging>=20.9,<21.0',
 'pillow>=8.2.0,<9.0.0',
 'playwright>=1.13.1,<2.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'python-dotenv>=0.17.1,<0.18.0',
 'rsa>=4.7.2,<5.0.0',
 'tortoise-orm[asyncpg]>=0.17.3,<0.18.0']

entry_points = \
{'console_scripts': ['hb = haruka_bot.cli.__main__:main']}

setup_kwargs = {
    'name': 'haruka-bot',
    'version': '1.3.1',
    'description': 'Push dynamics and live informations from bilibili to QQ. Based on nonebot2.',
    'long_description': '[![HarukaBot](https://socialify.git.ci/SK-415/HarukaBot/image?description=1&font=Source%20Code%20Pro&forks=1&issues=1&language=1&logo=https%3A%2F%2Fraw.githubusercontent.com%2FSK-415%2FHarukaBot%2Fmaster%2Fdocs%2F.vuepress%2Fpublic%2Flogo.png&owner=1&pattern=Circuit%20Board&stargazers=1&theme=Light)](https://haruka-bot.sk415.icu/)\n\n# HarukaBot ——你的“单推”小助手\n\n名称来源：[@白神遥Haruka](https://space.bilibili.com/477332594 )\n\nlogo 画师：[@秦无](https://space.bilibili.com/4668826 )\n\n[![VERSION](https://img.shields.io/pypi/v/haruka-bot)](https://haruka-bot.sk415.icu/about/CHANGELOG.html)\n[![time tracker](https://wakatime.com/badge/github/SK-415/HarukaBot.svg )](https://wakatime.com/badge/github/SK-415/HarukaBot)\n[![qq group](https://img.shields.io/badge/QQ%E7%BE%A4-629574472-orange )](https://jq.qq.com/?_wv=1027&k=sHPbCRAd)\n[![docs](https://img.shields.io/badge/%E6%96%87%E6%A1%A3-%E7%82%B9%E5%87%BB%E6%9F%A5%E7%9C%8B-green)](https://haruka-bot.sk415.icu)\n\n## 简介\n\n一款将哔哩哔哩UP主的直播与动态信息推送至QQ的机器人。基于 [`NoneBot2`](https://github.com/nonebot/nonebot2 ) 开发，前身为 [`dd-bot`](https://github.com/SK-415/dd-bot) 。\n\nHarukaBot 致力于为B站UP主们提供一个开源免费的粉丝群推送方案。极大的减轻管理员负担，不会再遇到突击无人推送的尴尬情况。同时还能将B博动态截图转发至粉丝群，活跃群内话题。\n\n> 介于作者技术力低下，HarukaBot 的体验可能并不是很好。如果使用中有任何意见或者建议都欢迎提交issue或[**添加Haruka反馈交流群**](https://jq.qq.com/?_wv=1027&k=sHPbCRAd)进行反馈，我会努力去完善它。\n\n## [文档（点我查看）](https://haruka-bot.sk415.icu/)\n\n## 功能介绍\n\n**以下仅为功能介绍，并非实际命令名称。具体命令向 bot 发送 `帮助` 查看，群里使用需要先@机器人**。\n\nHarukaBot 专注于订阅B站UP主们的动态与开播提醒，并转发至QQ群/好友。\n\n同时 HarukaBot 针对粉丝群中的推送场景进行了若干优化: \n\n- **权限开关**: 指定某个群只有管理员才能触发指令\n\n- **@全体开关**: 指定群里某位订阅的主播开播推送带@全体\n\n- **动态/直播开关**: 可以自由设置每位主播是否推送直播/动态\n\n- **订阅列表**: 每个群/好友的订阅都是分开来的\n\n- **多端推送**: 受限于一个QQ号一天只能@十次全体成员，因此对于粉丝群多的UP来说一个 bot 的次数完全不够推送。因此一台 HarukaBot 支持同时连接多个QQ，分别向不同的群/好友同时推送\n\n## 特别感谢\n\n- [`go-cqhttp`](https://github.com/Mrs4s/go-cqhttp)：简单又完善的 cqhttp 实现\n\n- [`NoneBot2`](https://github.com/nonebot/nonebot2)：超好用的开发框架，没有它就没有 HarukaBot（yyy佬牛逼）\n\n- [`bilibili-API-collect`](https://github.com/SocialSisterYi/bilibili-API-collect)：非常详细的 B站 api 文档\n\n- [`bilibili_api`](https://github.com/Passkou/bilibili_api)：Python 实现的强大 B站 api 库\n\n## 支持与贡献\n\n点个小星星就是对我最好的支持，感谢使用 HarukaBot。也欢迎 有能man 对本项目 Pull requests。\n\n## 许可证\n本项目使用 [`GNU AGPLv3`](https://choosealicense.com/licenses/agpl-3.0/) 作为开源许可证。\n',
    'author': 'SK-415',
    'author_email': '2967923486@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/SK-415/HarukaBot',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
