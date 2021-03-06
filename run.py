from OnlineHeart import OnlineHeart
from Silver import Silver
from LotteryResult import LotteryResult
from Tasks import Tasks
from login import Login
from connect import connect
import asyncio
from API import API
from configloader import ConfigLoader
from printer import Printer
from bilibili import bilibili

cf = ConfigLoader("color.conf", "user.conf", "bilibili.conf")
printer = Printer(cf)
bilibili = bilibili(cf)
login = Login(bilibili)
login.success()

bilibili = login.return_bilibili()
api = API(bilibili)
api.user_info()
api.get_bag_list()
task = OnlineHeart(bilibili)
task1 = Silver(bilibili)
task2 = Tasks(bilibili)
task3 = LotteryResult(bilibili)
task4 = connect(printer, bilibili, api)

tasks = [
    task.run(),
    task1.run(),
    task2.run(),
    task4.connect(),
    task3.query()
]

loop = asyncio.get_event_loop()

loop.run_until_complete(asyncio.wait(tasks))

loop.close()

