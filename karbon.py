#IMPORTLAR 
import pygame
import time
#initializing VE CLOKC TICK AYARLARI
pygame.init()
clock=pygame.time.Clock()

f=open('testkarbon.txt',mode='w',encoding='utf-8')

#EKRAN TANIMLAMALARI
win=pygame.display.set_mode((1200,720))



#IMAGE DOSYALARI
manright=pygame.image.load('manright.png')
manleft=pygame.image.load('manleft.png')
manleft=pygame.transform.scale(manleft,(80,80))
manright=pygame.transform.scale(manright,(80,80))
manimage=pygame.image.load('manright.png')
iconimage=pygame.image.load('icon.png')
fabimage=pygame.image.load('fab256.png')
fabimage2=pygame.image.load('fab2.png')
manimage=pygame.transform.scale(manimage,(80,80))
groundimage=pygame.image.load('ground.png')
skyimage=pygame.image.load('skybox.png')
madenimage=pygame.image.load('kalsiyum.png')
madenimage2=pygame.image.load('sodyum.jpg')
madenimage3=pygame.image.load('potasyum.png')
madenimage=pygame.transform.scale(madenimage,(450,121))
madenimage2=pygame.transform.scale(madenimage2,(450,121))
madenimage3=pygame.transform.scale(madenimage3,(450,121))
labimage=pygame.image.load('lab.png')
sukulesiimage=pygame.image.load('sukulesi.png')
menuimage=pygame.image.load('menu1.png')
menuimage=pygame.transform.scale(menuimage,(450,363))
menuimage2=pygame.image.load('menu2.png')
menuimage2=pygame.transform.scale(menuimage2,(300,363))
introimage=pygame.image.load('intro.png')
leaderboardimage=pygame.image.load('leaderboardimage.png')
leaderboardimage=pygame.transform.scale(leaderboardimage,(400,600))
ormanimage=pygame.image.load('orman.png')
ormanimage=pygame.transform.scale(ormanimage,(200,200))
coinimage=pygame.image.load('coin.png')
coinimage=pygame.transform.scale(coinimage,(32,32))
infoimage=pygame.image.load('info.jpg')

#İCON VE OYUN BAŞLIĞI
pygame.display.set_icon(iconimage)
pygame.display.set_caption('karbon')


#CLASSLAR 
class man1(object):
	def __init__(self,x,y):
		self.x=x
		self.y=y

#OYUNCUYU KLASA ATAMA
man=man1(300,276)
x=True 							


#ÇİZİM FONKSİYONU
def draw():
	win.fill((255,255,255))
	win.blit(skyimage,(0,0))
	win.blit(fabimage,(0,100))
	win.blit(fabimage2,(600,100))
	win.blit(labimage,(250,100))
	win.blit(sukulesiimage,(450,100))
	win.blit(menuimage,(450,357))
	win.blit(menuimage2,(900,357))
	win.blit(madenimage,(0,356))
	win.blit(madenimage2,(0,477))
	win.blit(madenimage3,(0,598))
	win.blit(ormanimage,(900,156))
	win.blit(coinimage,(0,0))
	win.blit(groundimage,(0,356))
	win.blit(groundimage,(64,356))
	win.blit(groundimage,(128,356))
	win.blit(groundimage,(192,356))
	win.blit(groundimage,(256,356))
	win.blit(groundimage,(318,356))
	win.blit(groundimage,(300,356))
	win.blit(groundimage,(360,356))
	win.blit(groundimage,(420,356))
	win.blit(groundimage,(480,356))
	win.blit(groundimage,(540,356))
	win.blit(groundimage,(600,356))
	win.blit(groundimage,(660,356))
	win.blit(groundimage,(720,356))
	win.blit(groundimage,(780,356))
	win.blit(groundimage,(840,356))
	win.blit(groundimage,(900,356))
	win.blit(groundimage,(960,356))
	win.blit(groundimage,(1020,356))
	win.blit(groundimage,(1080,356))
	win.blit(groundimage,(1140,356))
	win.blit(groundimage,(1200,356))
	#FONT TANIMI VE FONT RENDER'I
	font=pygame.font.SysFont('comicsans',30,True)
	paramiktar=font.render('{}'.format(para),1,(0,0,0))
	win.blit(paramiktar,(35,10))
	a=font.render('-a-',1,(0,0,0))
	win.blit(a,(15,30))

	#OYUNCUYU GÖRÜNTÜSÜNÜ SAĞA VEYA SOLA DOĞRU VERME
	if x==True:
		win.blit(manleft,(man.x,man.y))
	else:
		win.blit(manright,(man.x,man.y))
	pygame.draw.line(win,(0,0,0),(900,356),(900,720),2)




font=pygame.font.SysFont('comicsans',30,True)

#ELEMENT VE MATERYAL CLASSLARI 
class kalsiyumc():
	def __init__(self,miktar):
		self.miktar=miktar
class sodyumc():
	def __init__(self,miktar):
		self.miktar=miktar
class baryumc():
	def __init__(self,miktar):
		self.miktar=miktar
class suc():
	def __init__(self,miktar):
		self.miktar=miktar
class sudkostikc():
	def __init__(self,miktar):
		self.miktar=miktar
class sonmuskirecc():
	def __init__(self,miktar):
		self.miktar=miktar
class baryumkostikc():
	def __init__(self,miktar):
		self.miktar=miktar


#BİRİM VE DEĞER TANIMLAMALARI
para=0
insansayısı=10000
metanolmiktar=0
etanolmiktar=0
baralymemiktar=0
sodalymemiktar=0
karbondioksitmiktarı=400
ağaçsayısı=1000
sonmuskirec=sonmuskirecc(0)
baryumkostik=baryumkostikc(0)
sudkostik=sudkostikc(0)
kalsiyum=kalsiyumc(0)
sodyum=sodyumc(0)
baryum=baryumc(0)
su=suc(0)

#MADEN FONKSİYONU
def maden():
	keys=pygame.key.get_pressed()
	if  250<man.x<380 and  400>man.y>=356:
		pygame.draw.rect(win,(121,85,72),(330,370,85,20))
		toplatext=font.render('Topla',1,(255,255,255))
		win.blit(toplatext,(340,370))
		if keys[pygame.K_SPACE]:
			kalsiyum.miktar+=1
			time.sleep(0.1)
	if  (250<man.x<380 and  356+121+121>man.y>=356+121):
		pygame.draw.rect(win,(121,85,72),(330,370+121,85,20))
		toplatext=font.render('Topla',1,(255,255,255))
		win.blit(toplatext,(340,370+121))
		if keys[pygame.K_SPACE]:
			sodyum.miktar+=1
			time.sleep(0.1)
	if  (250<man.x<380 and man.y>=356+121+121)  :
		pygame.draw.rect(win,(121,85,72),(330,370+121+121,85,20))
		toplatext=font.render('Topla',1,(255,255,255))
		win.blit(toplatext,(340,370+121+121))
		if keys[pygame.K_SPACE]:
			baryum.miktar+=1
			time.sleep(0.1)
	
#SU KULESİ FONKSİYONU
def sukulesi():
	keys=pygame.key.get_pressed()
	font=pygame.font.SysFont('comicsans',30,True)

	if 500<man.x<600 and man.y<356:
		pygame.draw.rect(win,(121,85,72),(440,90,240,40))
		sumiktarı=font.render('Su Topla -Space',1,(255,255,255))
		win.blit(sumiktarı,(470,100))
		if keys[pygame.K_SPACE]:
			su.miktar+=1
			time.sleep(0.1)
	
#BİRİNCİ FABRİKA FONKSİYONU
def fabrika():
	global sodalymemiktar
	global baralymemiktar
	global karbondioksitmiktarı
	keys=pygame.key.get_pressed()
	font=pygame.font.SysFont('comicsans',30,True)
	if  0<man.x<150 and man.y<356:
		pygame.draw.rect(win,(121,85,72),(10,0,205,40))
		pygame.draw.rect(win,(121,85,72),(10,50,205,40))
		pygame.draw.rect(win,(121,85,72),(10,100,205,40))
		pygame.draw.rect(win,(121,85,72),(220,0,160,40))
		pygame.draw.rect(win,(121,85,72),(220,50,160,40))
		naoh=font.render('Sudkostik -s',1,(255,255,255))
		caoh2=font.render('Sönmüş Kireç -d',1,(255,255,255))
		baoh=font.render('Baryum Kostik -f',1,(255,255,255))
		baralyme=font.render('Baralyme -g',1,(255,255,255))
		sodalyme=font.render('Sodalyme -h',1,(255,255,255))
		win.blit(naoh,(15,10))
		win.blit(caoh2,(15,60))
		win.blit(baoh,(15,110))
		win.blit(baralyme,(225,10))
		win.blit(sodalyme,(225,60))

		if keys[pygame.K_s]:
			if sodyum.miktar>0 and su.miktar>0:
				sodyum.miktar-=1
				su.miktar-=1
				sudkostik.miktar+=1
				time.sleep(0.1)
		if keys[pygame.K_d]:
			if kalsiyum.miktar>0 and su.miktar>0:
				kalsiyum.miktar-=1
				su.miktar-=2
				sonmuskirec.miktar+=1
				time.sleep(0.1)
		if keys[pygame.K_f]:
			if baryum.miktar>0 and su.miktar>0:
				baryum.miktar-=1
				su.miktar-=1
				baryumkostik.miktar+=1
				time.sleep(0.1)
		if keys[pygame.K_g]:
			if sonmuskirec.miktar>15 and baryumkostik.miktar>3 :
				sonmuskirec.miktar-=16
				baryumkostik.miktar-=4
				baralymemiktar+=1
				karbondioksitmiktarı-=3
				time.sleep(0.1)
		if keys[pygame.K_h]:
			if sonmuskirec.miktar>15 and su.miktar>2 and sudkostik.miktar>0:
				sonmuskirec.miktar-=16
				su.miktar-=3
				sudkostik.miktar-=1
				sodalymemiktar+=1
				karbondioksitmiktarı-=5
				time.sleep(0.1)

#İKİNCİ FABRİKA FONKSİYONU
def fabrika2():
	global etanolmiktar
	global sodalymemiktar
	global baralymemiktar
	global karbondioksitmiktarı
	global metanolmiktar
	keys=pygame.key.get_pressed()
	font=pygame.font.SysFont('comicsans',30,True)
	if  620<man.x<800 and man.y<356:
		pygame.draw.rect(win,(121,85,72),(650,0,160,40))
		pygame.draw.rect(win,(121,85,72),(650,50,160,40))
		etanoltext=font.render('Metanol -s',1,(255,255,255))
		metanoltext=font.render('Etanol -d',1,(255,255,255))
		win.blit(etanoltext,(660,10))
		win.blit(metanoltext,(660,60))
		if keys[pygame.K_s]:
			if su.miktar>0:
				karbondioksitmiktarı-=0.1   
				su.miktar-=1
				metanolmiktar+=1
				time.sleep(0.1)
		if keys[pygame.K_d]:
			if su.miktar>1:
				karbondioksitmiktarı-=0.2
				su.miktar-=2
				etanolmiktar+=1
				time.sleep(0.1)


#LABORATUAR FONKSİYONU
def lab():
	global metanolmiktar
	global etanolmiktar
	global para
	keys=pygame.key.get_pressed()
	font=pygame.font.SysFont('comicsans',30,True)
	if  240<man.x<400 and man.y<356:
		pygame.draw.rect(win,(121,85,72),(250,0,240,40))
		pygame.draw.rect(win,(121,85,72),(250,50,240,40))
		antifriztext=font.render('Metanol>Antifriz -s',1,(255,255,255))
		deterjantext=font.render('Etanol>Deterjan -d',1,(255,255,255))
		win.blit(antifriztext,(250,10))
		win.blit(deterjantext,(250,60))
		if keys[pygame.K_s]:
			if metanolmiktar>9:
				metanolmiktar-=10
				para+=200
				time.sleep(0.1)
		if keys[pygame.K_d]:
			if etanolmiktar>9:
				etanolmiktar-=10
				para+=450
				time.sleep(0.1)

#SATMA BUTONLARI VE İNTERAKTİF EDİLMELERİ
def satış():
	global etanolmiktar
	global metanolmiktar
	global baralymemiktar
	global sodalymemiktar
	global para
	font=pygame.font.SysFont('courier',30,True)
	keys=pygame.key.get_pressed()
	mouse=pygame.mouse.get_pos()
	click=pygame.mouse.get_pressed()
	sat=font.render('SAT',1,(255,255,255))
	pygame.draw.rect(win,(200,0,0),(700,375,55,30))
	pygame.draw.rect(win,(200,0,0),(700,420,55,30))
	pygame.draw.rect(win,(200,0,0),(700,470,55,30))
	pygame.draw.rect(win,(200,0,0),(700,515,55,30))
	pygame.draw.rect(win,(200,0,0),(700,565,55,30))
	pygame.draw.rect(win,(200,0,0),(700,610,55,30))
	pygame.draw.rect(win,(200,0,0),(700,660,55,30))
	win.blit(sat,(700,375))
	win.blit(sat,(700,420))
	win.blit(sat,(700,470))
	win.blit(sat,(700,515))
	win.blit(sat,(700,565))
	win.blit(sat,(700,610))
	win.blit(sat,(700,660))

	if 700<mouse[0]<755 and  375<mouse[1]<405:
		pygame.draw.rect(win,(255,0,0),(700,375,55,30))
		win.blit(sat,(700,375))
		if click[0]==1 and sudkostik.miktar>4:
			sudkostik.miktar-=5 
			para+=20
			time.sleep(0.2)
	if 700<mouse[0]<755 and  420<mouse[1]<450:
		pygame.draw.rect(win,(255,0,0),(700,420,55,30))
		win.blit(sat,(700,420))
		if click[0]==1 and baryumkostik.miktar>4:
			 baryumkostik.miktar-=5
			 para+=15 
			 time.sleep(0.2)
	if 700<mouse[0]<755 and  470<mouse[1]<500:
		pygame.draw.rect(win,(255,0,0),(700,470,55,30))
		win.blit(sat,(700,470))
		if click[0]==1 and metanolmiktar>4:
			metanolmiktar-=5 
			para+=5
			time.sleep(0.2)
	if 700<mouse[0]<755 and  515<mouse[1]<545:
		pygame.draw.rect(win,(255,0,0),(700,515,55,30))
		win.blit(sat,(700,515))
		if click[0]==1 and baralymemiktar>4:
			 baralymemiktar-=5 
			 para+=50
			 time.sleep(0.2)
	if 700<mouse[0]<755 and  565<mouse[1]<595:
		pygame.draw.rect(win,(255,0,0),(700,565,55,30))
		win.blit(sat,(700,565))
		if click[0]==1 and sodalymemiktar>4:
			sodalymemiktar-=5 
			para+=55
			time.sleep(0.2)
	if 700<mouse[0]<755 and  610<mouse[1]<640:
		pygame.draw.rect(win,(255,0,0),(700,610,55,30))
		win.blit(sat,(700,610))
		if click[0]==1 and etanolmiktar>4:
			etanolmiktar-=5 
			para+=7
			time.sleep(0.2)
	if 700<mouse[0]<755 and  660<mouse[1]<690:
		pygame.draw.rect(win,(255,0,0),(700,660,55,30))
		win.blit(sat,(700,660))
		if click[0]==1 and sonmuskirec.miktar>4:
			sonmuskirec.miktar-=5 
			para+=12
			time.sleep(0.2)



#MİKTAR GÖSTERİMLERİ
def amountshowing():
	global sodalymemiktar
	global baralymemiktar
	global karbondioksitmiktarı
	font=pygame.font.SysFont('courier',30,True)
	amount1=font.render('{}'.format(sudkostik.miktar),1,(255,255,255))
	amount2=font.render('{}'.format(baryumkostik.miktar),1,(255,255,255))
	amount3=font.render('{}'.format(metanolmiktar),1,(255,255,255))  
	amount4=font.render('{}'.format(baralymemiktar),1,(255,255,255))
	amount5=font.render('{}'.format(sodalymemiktar),1,(255,255,255))
	amount6=font.render('{}'.format(etanolmiktar),1,(255,255,255))
	amount7=font.render('{}'.format(sonmuskirec.miktar),1,(255,255,255))
	win.blit(amount1,(800,375))
	win.blit(amount2,(800,420))
	win.blit(amount3,(800,470))
	win.blit(amount4,(800,515))
	win.blit(amount5,(800,565))
	win.blit(amount6,(800,610))
	win.blit(amount7,(800,660))
	amount11=font.render('{}'.format(sodyum.miktar),1,(255,255,255))
	amount12=font.render('{}'.format(baryum.miktar),1,(255,255,255))
	amount13=font.render('{}'.format(kalsiyum.miktar),1,(255,255,255))
	amount14=font.render('{}'.format(su.miktar),1,(255,255,255))
	amount15=font.render('{}'.format(int(karbondioksitmiktarı)),1,(255,255,255))
	amount16=font.render('-',1,(255,255,255))
	win.blit(amount11,(1135,380))
	win.blit(amount12,(1135,435))
	win.blit(amount13,(1135,490))
	win.blit(amount14,(1135,545))
	win.blit(amount15,(1125,595))
	win.blit(amount16,(1135,650))
	humanamount=font.render('insan sayısı:{}'.format(int(insansayısı)),1,(0,0,0))
	win.blit(humanamount,(800,10))

#LİDER TABLOSU
def leaderboard():
	keys=pygame.key.get_pressed()
	if keys[pygame.K_TAB]:
		win.blit(leaderboardimage,(10,10))



#ORMAN FONKSİYONU
def orman():
	global ağaçsayısı
	keys=pygame.key.get_pressed()
	font=pygame.font.SysFont('comicsans',30,True)
	if  880<man.x<1080 and man.y<356:
		pygame.draw.rect(win,(121,85,72),(900,50,180,40))
		pygame.draw.rect(win,(121,85,72),(900,0,100,40))
		agactext=font.render('Ağaç Dik -s',1,(255,255,255))
		ağaçsayısıtext=font.render('{}'.format(int(ağaçsayısı)),1,(255,255,255))
		win.blit(agactext,(905,60))
		win.blit(ağaçsayısıtext,(905,15))
		if keys[pygame.K_s]:
			ağaçsayısı+=1
			time.sleep(0.2)
#INTRO BİLGİ FONKSİYONNU
introinfo=None
def fintroinfo():
	global introinfo
	while introinfo:
		keys=pygame.key.get_pressed()

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				introinfo=False
				pygame.quit()
				quit()
				f.close()
		win.fill((255,255,255))
		font=pygame.font.SysFont('comicsans',30,True)
		extrafont=pygame.font.SysFont('arial',65,True)
		extrafont2=pygame.font.SysFont('arial',30,True)

		txt1=extrafont.render('Karbongame ',1,(0,0,0))
		txt2=extrafont2.render('Software : Berkay Avcı',1,(0,0,0))
		txt3=extrafont2.render('Graphics : Mustafa Değerli',1,(0,0,0))
		txt4=extrafont2.render('Game logics : Celaleddin Ö. Sağlam',1,(0,0,0))


		win.fill((121,82,71))
		win.blit(txt1,(200,50))
		win.blit(txt2,(200,300))
		win.blit(txt3,(200,350))
		win.blit(txt4,(200,400))



		pygame.display.update()
		if keys[pygame.K_ESCAPE]:
			introinfo=None
			run=None
			gameintro()

#COİN TAKASI İLE CO2 AZALTMA FONKSİYONU
def coinagac():
	global para
	global karbondioksitmiktarı
	keys=pygame.key.get_pressed()
	if keys[pygame.K_a] and para>200 and karbondioksitmiktarı>0:
		para-=200
		karbondioksitmiktarı-=10
		time.sleep(0.2)
						


#KLAVYE KONTROL FONKSİYONU
def keycontrol():
	global x
	keys=pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and man.x>=0: 	
		x=True
		man.x-=10
	if keys[pygame.K_RIGHT] and man.x<=1120:
		if man.x>380 and man.y>=356:
			man.x-=10
		else:
			x=False
			man.x+=10
	if keys[pygame.K_UP]:
		if man.x<20 and man.y>=356:
			man.y-=121
			time.sleep(0.3)
	if keys[pygame.K_DOWN]:
		if man.x<20 and man.y<=520:
			man.y+=121	
			time.sleep(0.3)
	if keys[pygame.K_ESCAPE]:
		gameintro()


k=1			#ZORLUK KATSAYISI
#INTRO EKRANI (BAŞLANGIÇ)
def gameintro():
	global k
	global run
	global introinfo
	intro=True
	while intro:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()

		win.blit(introimage,(0,0))
		font=pygame.font.SysFont('comicsans',30,True)
		mouse=pygame.mouse.get_pos()
		mouseclick=pygame.mouse.get_pressed()
		easy=font.render('easy',1,(255,255,255))
		medium=font.render('medium',1,(255,255,255))
		hard=font.render('hard',1,(255,255,255))
		
		pygame.draw.rect(win,(0,200,200),(900,620,100,50))
		pygame.draw.rect(win,(0,200,200),(900,550,100,50))
		pygame.draw.rect(win,(0,200,200),(900,480,100,50))
		win.blit(easy,(905,485))
		win.blit(medium,(905,555))
		win.blit(hard,(905,625))
		if  900<mouse[0]<1000 and 620<mouse[1]<670:
			pygame.draw.rect(win,(0,255,255),(900,620,100,50))
			if mouseclick[0]==1:
				k=5
				pygame.draw.rect(win,(255,0,0),(900,620,100,50))
			win.blit(hard,(905,625))
		if  900<mouse[0]<1000 and 550<mouse[1]<600:
			pygame.draw.rect(win,(0,255,255),(900,550,100,50))
			if mouseclick[0]==1:
				k=3
				pygame.draw.rect(win,(255,0,0),(900,550,100,50))

			win.blit(medium,(905,555))
		if  900<mouse[0]<1000 and 480<mouse[1]<530:
			pygame.draw.rect(win,(0,255,255),(900,480,100,50))
			if mouseclick[0]==1:
				k=1
				pygame.draw.rect(win,(255,0,0),(900,480,100,50))

			win.blit(easy,(905,485))

		pygame.draw.rect(win,(0,200,0),(450,550,100,50))
		pygame.draw.rect(win,(0,200,200),(650,550,100,50))
		

		if   450< mouse[0]<550 and    550<mouse[1]<600:
			pygame.draw.rect(win,(0,255,0),(450,550,100,50))
			if mouseclick[0]==1:
				run=True
				introinfo=None
				main()
		if   650< mouse[0]<750 and    550<mouse[1]<600:
			pygame.draw.rect(win,(0,255,255),(650,550,100,50)) 
			if mouseclick[0]==1:
				run=False
				introinfo=True
				fintroinfo()

		starttext=font.render('Start',1,(255,255,255))
		infotext=font.render('Info',1,(255,255,255))
		win.blit(starttext,(470,565))
		win.blit(infotext,(670,565))
		pygame.display.update()



#MAIN FONKSİYON , CLOCK TICK AYARI VE KEYBOARD PRESS CHECK 
run=None	#MAİN FONKSİYONUN ÇALIŞMASI İÇİN GEREKEN KOŞUL
def main():
	global k
	global para
	global run
	global karbondioksitmiktarı
	global ağaçsayısı
	global insansayısı
	while run:
		clock.tick(120)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				run=False
				pygame.quit()
				quit()
				f.close()
		#OTOMATİK ARTIŞLAR		
		karbondioksitmiktarı+=(1/60)*k
		ağaçsayısı-=1/60
		insansayısı+=1/60
		insansayısı-=((karbondioksitmiktarı/200)/60)*k
		if karbondioksitmiktarı<=0:
			karbondioksitmiktarı=0
			win.fill(0,255,0)
		if insansayısı<=0:
			insansayısı=0
			win.fill(255,0,0)
		#FONSKİYON ÇAĞIRMALARI
		keycontrol()
		draw()
		sukulesi()
		maden()	                                                       
		fabrika()
		fabrika2()
		satış()
		leaderboard()
		amountshowing()
		lab()
		orman()
		coinagac()
		f.write(str(int(insansayısı)))
		f.write(',')

		pygame.display.update()  

#BAŞLANGIÇ EKRANI /ANA MENU
gameintro()