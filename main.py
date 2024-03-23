import pyautogui
import time
from pyautogui import ImageNotFoundException

#已经选择的技能对象存储
selectd_skill = {'Beam':0,'Laser':0,'Gun':0,'Elect':0,'Storm':0,'Cart':0,'tempureBoom':0,'elecPuncture':0,'Ice':0}


def decide_skill(skill_gui_object_list):

	for skil_json in skill_gui_object_list:
		if skil_json['skill'] == 'learn_GunPlusOneBullt':
			print("#如果看到了学习弹道数+1，学吧")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Gun_count = selectd_skill['Gun']
			selectd_skill['Gun']=Gun_count+1
		if skil_json['skill'] == 'learn_GunInc60':
			print("#如果看到了学习枪炮威力增加60%，那就学吧")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Gun_count = selectd_skill['Gun']
			selectd_skill['Gun']=Gun_count+1
		if skil_json['skill'] == 'learn_Gun_IncPrimeShootAndSecondLevelShoot100':
			print("#如果看到了学习子弹与次级别子弹威力增加100%，那就学吧")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Gun_count = selectd_skill['Gun']
			selectd_skill['Gun']=Gun_count+1
		if skil_json['skill'] == 'learn_GunDoubleShoot':
			print("#如果看到了射击连发数+1，那就学吧")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Gun_count = selectd_skill['Gun']
			selectd_skill['Gun']=Gun_count+1
		if  skil_json['skill'] == 'learn_Gun_splitShoot':
			print("#如果看到了分裂设计+1，那就学吧")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Gun_count = selectd_skill['Gun']
			selectd_skill['Gun']=Gun_count+1
		if  skil_json['skill'] == 'learn_Gun_Split4Shot':
			print("#如果看到了分裂设计+4，那就学吧")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Gun_count = selectd_skill['Gun']
			selectd_skill['Gun']=Gun_count+1
		if  skil_json['skill'] == 'learn_Gun_Boom':
			print("#如果看到了子弹炸裂，那就学吧")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Gun_count = selectd_skill['Gun']
			selectd_skill['Gun']=Gun_count+1
		if  skil_json['skill'] == 'learn_Gun_secondLevel100Hurts':
			print("#如果看到了次级子弹增伤100%，那就学吧")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Gun_count = selectd_skill['Gun']
			selectd_skill['Gun']=Gun_count+1
		if  skil_json['skill'] == 'learn_Gun_IncShootBoomFeature':
			print("#如果看到了增加子弹的爆炸范围")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Gun_count = selectd_skill['Gun']
			selectd_skill['Gun']=Gun_count+1



		if skil_json['skill'] == 'learn_Beam':
			print("#如果看到了学习射线，则优先学习射线")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Beam_count = selectd_skill['Beam']
			selectd_skill['Beam']=Beam_count+1
		if skil_json['skill'] == 'learn_BeamAndLaserInc60':
			print("#如果看到了射线与制导激光伤害增加60%这种神一般的技能卡，那赶紧学啊")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Beam_count = selectd_skill['Beam']
			selectd_skill['Beam']=Beam_count+1
			Laser_count = selectd_skill['Laser']
			selectd_skill['Laser']=Laser_count+1
		if skil_json['skill'] == 'learn_Beam_lowSeep80':
			print("#如果看到了学习射线降速80%，那就学吧")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Beam_count = selectd_skill['Beam']
			selectd_skill['Beam']=Beam_count+1
		if skil_json['skill'] == 'learn_Beam_25pecIncIn5secs':
			print("#如果看到了学习射线5秒内加伤害25%，那就学吧")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Beam_count = selectd_skill['Beam']
			selectd_skill['Beam']=Beam_count+1
		if skil_json['skill'] == 'learn_BeamInc60':
			print("#如果看到了学习射线60%，那就学吧")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Beam_count = selectd_skill['Beam']
			selectd_skill['Beam']=Beam_count+1
		if skil_json['skill'] == 'learn_Beam_Inc5timesHurts':
			print("#如果看到了学习射线增伤5次，那就学吧")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Beam_count = selectd_skill['Beam']
			selectd_skill['Beam']=Beam_count+1
		if skil_json['skill'] == 'learn_Beam_IncHurtsTimes':
			print("#如果看到了学习射线增伤，但增加冷却时间50%，学就学吧")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Beam_count = selectd_skill['Beam']
			selectd_skill['Beam']=Beam_count+1
		if skil_json['skill'] == 'learn_Beam_Inc150range':
			print("#如果看到了学习射线增伤增加范围150%")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Beam_count = selectd_skill['Beam']
			selectd_skill['Beam']=Beam_count+1





		if skil_json['skill'] == 'learn_Laser':
			print("#如果看到了学习制导激光，则优先学习激光")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Laser_count = selectd_skill['Laser']
			selectd_skill['Laser']=Laser_count+1
		if skil_json['skill'] == 'learn_Laser_Inc200toPrimerTarget':
			print("#如果看到了学习制导激光对主目标增伤200%，那就学吧")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Laser_count = selectd_skill['Laser']
			selectd_skill['Laser']=Laser_count+1
		if skil_json['skill'] == 'learn_Laser_Inc60Hurts':
			print("#如果看到了学习制导激光伤害加60%，那就学吧")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Laser_count = selectd_skill['Laser']
			selectd_skill['Laser']=Laser_count+1
		if skil_json['skill'] == 'learn_Laser_Inc15times':
			print("#如果看到了学习制导激光伤害加15次，那就学吧")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Laser_count = selectd_skill['Laser']
			selectd_skill['Laser']=Laser_count+1
		if skil_json['skill'] == 'learn_Laser_BoomOnPrimerTarget':
			print("#如果看到了学习制导激光在主目标爆炸，那就学吧")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Laser_count = selectd_skill['Laser']
			selectd_skill['Laser']=Laser_count+1






		if skil_json['skill'] == 'learn_Elect':
			print("#感觉是实在没得选了，就选跃迁电子吧")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Elect_count = selectd_skill['Elect']
			selectd_skill['Elect']=Elect_count+1
		if skil_json['skill'] == 'learn_Elect_Inc60':
			print("#感觉是实在没得选了，那就选增伤跃迁电子60%吧")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Elect_count = selectd_skill['Elect']
			selectd_skill['Elect']=Elect_count+1
		if skil_json['skill'] == 'learn_Elect_Inc30andIce1sec':
			print("#感觉是实在没得选了，那就选增伤跃迁电子30%伤害，并且增加麻痹时间1秒")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Elect_count = selectd_skill['Elect']
			selectd_skill['Elect']=Elect_count+1




		if skil_json['skill'] == 'learn_Storm':
			print("#感觉是实在没得选了，那就选旋风加农吧")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Storm_count = selectd_skill['Storm']
			selectd_skill['Storm']=Storm_count+1
		if skil_json['skill'] == 'learm_Storm_Inc60Hurts':
			print("#感觉是实在没得选了，那就选旋风加农增加60%伤害吧")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Storm_count = selectd_skill['Storm']
			selectd_skill['Storm']=Storm_count+1
		if skil_json['skill'] == 'learn_Storm_Inc50force':
			print("#感觉是实在没得选了，那就选旋风加农增加50%牵引力")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Storm_count = selectd_skill['Storm']
			selectd_skill['Storm']=Storm_count+1
		if skil_json['skill'] == 'learn_Storm_Inc100lastTime':
			print("#感觉是实在没得选了，那就选旋风加农增加100%的时间")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Storm_count = selectd_skill['Storm']
			selectd_skill['Storm']=Storm_count+1



		if skil_json['skill'] == 'learn_Cart':
			print("#感觉是实在没得选了，那就选卡车吧")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Cart_count = selectd_skill['Cart']
			selectd_skill['Cart']=Cart_count+1
		if skil_json['skill'] == 'learn_Cart_Inc60':
			print("#感觉是实在没得选了，那就选卡车吧")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Cart_count = selectd_skill['Cart']
			selectd_skill['Cart']=Cart_count+1




		if skil_json['skill'] == 'learn_tempureBoom':
			print("#感觉是实在没得选了，那就选温压弹吧，哎")
			pyautogui.click(skil_json['x'], skil_json['y'])
			tempureBoom_count = selectd_skill['tempureBoom']
			selectd_skill['tempureBoom']=tempureBoom_count+1
		if skil_json['skill'] == 'learn_tempureBoom_IncBoomHurts80':
			print("#感觉是实在没得选了，温压弹增伤80%，哎")
			pyautogui.click(skil_json['x'], skil_json['y'])
			tempureBoom_count = selectd_skill['tempureBoom']
			selectd_skill['tempureBoom']=tempureBoom_count+1
		if skil_json['skill'] == 'learn_tempureBoom_OneMoreBoom':
			print("#感觉是实在没得选了，多来一枚温压弹，哎")
			pyautogui.click(skil_json['x'], skil_json['y'])
			tempureBoom_count = selectd_skill['tempureBoom']
			selectd_skill['tempureBoom']=tempureBoom_count+1
		if skil_json['skill'] == 'learn_tempureBoom_Inc80HurtsAndBeatBackMonster':
			print("#感觉是实在没得选了，温压弹增伤80%并增加击退效果")
			pyautogui.click(skil_json['x'], skil_json['y'])
			tempureBoom_count = selectd_skill['tempureBoom']
			selectd_skill['tempureBoom']=tempureBoom_count+1



		if skil_json['skill'] == 'learn_elecPuncture':
			print("#感觉是实在没得选了，那就电磁穿刺吧，哎")
			pyautogui.click(skil_json['x'], skil_json['y'])
			elecPuncture_count = selectd_skill['elecPuncture']
			selectd_skill['elecPuncture']=elecPuncture_count+1
		if skil_json['skill'] == 'learn_elecPuncture_oneMorePuncture':
			print("#感觉是实在没得选了，那就电磁穿刺吧，再增加一发穿刺")
			pyautogui.click(skil_json['x'], skil_json['y'])
			elecPuncture_count = selectd_skill['elecPuncture']
			selectd_skill['elecPuncture']=elecPuncture_count+1
		if skil_json['skill'] == 'learn_elecPuncture_Inc80Hurts':
			print("#感觉是实在没得选了，电磁穿刺增加伤害80%")
			pyautogui.click(skil_json['x'], skil_json['y'])
			elecPuncture_count = selectd_skill['elecPuncture']
			selectd_skill['elecPuncture']=elecPuncture_count+1

		if skil_json['skill'] == 'learn_Ice':
			print("#感觉是实在没得选了，那就干冰弹吧")
			pyautogui.click(skil_json['x'], skil_json['y'])
			Ice_count = selectd_skill['Ice']
			selectd_skill['Ice']=Ice_count+1

	#打印一下当前的技能情况
	print("#打印一下当前的技能情况")
	print(selectd_skill)


def scan_skills():
	skill_list =[
	'learn_GunPlusOneBullt','learn_GunInc60','learn_GunDoubleShoot',
	'learn_Gun_IncPrimeShootAndSecondLevelShoot100',
	'learn_Gun_splitShoot','learn_Gun_Split4Shot','learn_Gun_Boom',
	'learn_Gun_secondLevel100Hurts','learn_Gun_IncShootBoomFeature',
	'learn_BeamAndLaserInc60',
	'learn_Beam','learn_BeamInc60','learn_Beam_lowSeep80',
	'learn_Beam_25pecIncIn5secs','learn_Beam_Inc5timesHurts',
	'learn_Beam_IncHurtsTimes','learn_Beam_Inc150range',
	'learn_Laser','learn_Laser_Inc200toPrimerTarget','learn_Laser_Inc15times',
	'learn_Laser_BoomOnPrimerTarget','learn_Laser_Inc60Hurts',
	'learn_Elect','learn_Elect_Inc60','learn_Elect_Inc30andIce1sec',
	'learn_Storm','learm_Storm_Inc60Hurts','learn_Storm_Inc50force','learn_Storm_Inc100lastTime',
	'learn_tempureBoom','learn_tempureBoom_IncBoomHurts80','learn_tempureBoom_OneMoreBoom',
	'learn_tempureBoom_Inc80HurtsAndBeatBackMonster',
	'learn_elecPuncture','learn_elecPuncture_oneMorePuncture','learn_elecPuncture_Inc80Hurts',
	'learn_Cart','learn_Cart_Inc60',
	'learn_Ice']
	skill_gui_object_list = []
	for skil in skill_list:
		try:
			skil_gui_object = pyautogui.locateCenterOnScreen(skil+'.png',confidence=0.9)
			json_object = {
		        'skill':skil, 
		        'x':skil_gui_object.x, 
		        'y':skil_gui_object.y
		    }
			#print(json_object)
			skill_gui_object_list.append(json_object)
		except ImageNotFoundException as e:
			#print("没出现这玩意：",skil)
			pass
	# 循环遍历整个技能列表结束
	print("界面上得到如下的技能卡牌")
	print(skill_gui_object_list)
	decide_skill(skill_gui_object_list)

game_start = False


def dectect_game_return():
    try:
    	x,y = pyautogui.locateCenterOnScreen('return.png',confidence=0.9)
    	print("【出现了返回游戏，那就赶紧返回吧】")
    	pyautogui.click(x,y)
    	game_start = False
    except ImageNotFoundException as e:
    	print("【返回游戏】未出现，再扫描吧：",e)
    	pass

def dectect_game_start():
    try:
    	x,y = pyautogui.locateCenterOnScreen('start_game_button.png',confidence=0.9)
    	print("【出现了开始游戏，那就赶紧开始吧】")
    	pyautogui.click(x,y)
    	game_start = True
    except ImageNotFoundException as e:
    	print("【开始游戏】未出现，再扫描吧：",e)
    	pass

def dectect_elite_dropDown():
    try:
    	x,y = pyautogui.locateCenterOnScreen('elite_dropDown.png',confidence=0.9)
    	print("【出现了精英掉落，那就随便点击一下吧】")
    	pyautogui.click(x,y)
    except ImageNotFoundException as e:
    	print("【精英掉落】未出现，再扫描吧：",e)
    	pass


def perform_task():
    # 这里编写要每隔 5 秒钟执行的任务代码
    print("每5秒钟的循环开始...")
    #选择技能弹出了
    try:
    	select_skill = pyautogui.locateCenterOnScreen('select_skill.png',confidence=0.9)
    	print("【选择技能卡牌已出现，进入选择逻辑：】")
    	scan_skills()
    except ImageNotFoundException as e:
    	print("【选择技能】未出现，再扫描吧：",e)
    	dectect_game_return()
    	dectect_elite_dropDown()
    	if game_start:
    		pass
    	else:
    		dectect_game_start()
    	pass

# 设置一个计时器，每隔 2 秒钟触发一次
timer = time.perf_counter() 
while True:
    if time.perf_counter() - timer >= 2:  
        perform_task()
        timer = time.perf_counter() 
    # 等待一段时间（这里使用 0.1 秒作为示例），以避免过高的 CPU 占用
    time.sleep(0.1)
