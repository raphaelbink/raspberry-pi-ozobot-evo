from BotConnect import botConnect

robotFinder = botConnect.RobotFinder()
robotFinder.findRobots()

bot1 = botConnect.RobotControl(robotFinder.robots[0].mac_addr)
bot1.connect()

bot1.c.write(b"\x50\x02\x01")

bot1.d.write(bot1.drive(500,500,1000))

bot1.c.write(bot1.led(255,100,100,20))
