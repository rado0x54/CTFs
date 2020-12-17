#!/usr/bin/env python3

import re
from pwn import remote
from sympy import mod_inverse

r = remote('jupiter.challenges.picoctf.org', 58617)

# Problem 1
binary_raw = r.recvuntil(b'(Y/N):').decode()
p = re.compile('.*q : (\\d+)\\np : (\\d+).*', re.DOTALL)
values = p.match(binary_raw).groups()
q = int(values[0])  # 60413
p = int(values[1])  # 76753
n = p * q  # 4636878989

r.sendline('Y')
r.recvuntil('n: ')
r.sendline(str(n))

# Problem 2
binary_raw = r.recvuntil(b'(Y/N):').decode()
p = re.compile('.*p : (\\d+)\\nn : (\\d+).*', re.DOTALL)
values = p.match(binary_raw).groups()
p = int(values[0])  # 54269
n = int(values[1])  # 5051846941
q = n // p  # 93089

r.sendline('Y')
r.recvuntil('q: ')
r.sendline(str(q))

# Problem 3
binary_raw = r.recvuntil(b'(Y/N):').decode()
r.sendline('N')

# Problem 4
binary_raw = r.recvuntil(b'(Y/N):').decode()
p = re.compile('.*q : (\\d+)\\np : (\\d+).*', re.DOTALL)
values = p.match(binary_raw).groups()
q = int(values[0])  # 66347
p = int(values[1])  # 12611
tot_n = (q-1)*(p-1)
print(tot_n)  # 836623060

r.sendline('Y')
r.recvuntil('totient(n): ')
r.sendline(str(tot_n))

# Problem 5
binary_raw = r.recvuntil(b'(Y/N):').decode()
p = re.compile('.*plaintext : (\\d+)\\ne : (\\d+)\\nn : (\\d+).*', re.DOTALL)
values = p.match(binary_raw).groups()
plaintext = int(values[0])  # 6357294171489311547190987615544575133581967886499484091352661406414044440475205342882841236357665973431462491355089413710392273380203038793241564304774271529108729717
e = int(values[1])  # 3
n = int(values[2])  # 29129463609326322559521123136222078780585451208149138547799121083622333250646678767769126248182207478527881025116332742616201890576280859777513414460842754045651093593251726785499360828237897586278068419875517543013545369871704159718105354690802726645710699029936754265654381929650494383622583174075805797766685192325859982797796060391271817578087472948205626257717479858369754502615173773514087437504532994142632207906501079835037052797306690891600559321673928943158514646572885986881016569647357891598545880304236145548059520898133142087545369179876065657214225826997676844000054327141666320553082128424707948750331
ciphertext = pow(plaintext, e, n)

r.sendline('Y')
r.recvuntil('ciphertext: ')
r.sendline(str(ciphertext))

# Problem 6
binary_raw = r.recvuntil(b'(Y/N):').decode()
r.sendline('N')

# Problem 7
binary_raw = r.recvuntil(b'(Y/N):').decode()
p = re.compile('.*q : (\\d+)\\np : (\\d+)\\ne : (\\d+).*', re.DOTALL)
values = p.match(binary_raw).groups()
q = int(values[0])  # 92092076805892533739724722602668675840671093008520241548191914215399824020372076186460768206814914423802230398410980218741906960527104568970225804374404612617736579286959865287226538692911376507934256844456333236362669879347073756238894784951597211105734179388300051579994253565459304743059533646753003894559
p = int(values[1])  # 97846775312392801037224396977012615848433199640105786119757047098757998273009741128821931277074555731813289423891389911801250326299324018557072727051765547115514791337578758859803890173153277252326496062476389498019821358465433398338364421624871010292162533041884897182597065662521825095949253625730631876637
e = int(values[2])  # 65537
tot_n = (q-1) * (p-1)  # 9010912747277787249738727439840427055736519196538871349093408340706668231808840540195374015916168031416186859836416053338250477003776576736854137538279810042409758765948034443613881324504120707334213544491046703922409406729564516371394804946909037646047891880347940067132730874804943893719672960932378043324877575934090934383537480859453188253291539686270935881039160668298044489030244356028174143765322586938365063530331798603113286673099000259440894881684231186302284225193426999907752867514204209640980817406669962746837092448906692344720572958732053915811402369526465666177954964908259624156431216201128207746888
d = mod_inverse(e, tot_n)  # 1405046269503207469140791548403639533127416416214210694972085079171787580463776820425965898174272870486015739516125786182821637006600742140682552321645503743280670839819078749092730110549881891271317396450158021688253989767145578723458252769465545504142139663476747479225923933192421405464414574786272963741656223941750084051228611576708609346787101088759062724389874160693008783334605903142528824559223515203978707969795087506678894006628296743079886244349469131831225757926844843554897638786146036869572653204735650843186722732736888918789379054050122205253165705085538743651258400390580971043144644984654914856729

r.sendline('Y')
r.recvuntil('d: ')
r.sendline(str(d))

# Problem 8
binary_raw = r.recvuntil(b'(Y/N):').decode()
p = re.compile('.*p : (\\d+)\\nciphertext : (\\d+)\\ne : (\\d+)\\nn : (\\d+).*', re.DOTALL)
values = p.match(binary_raw).groups()
p = int(values[0])  # 153143042272527868798412612417204434156935146874282990942386694020462861918068684561281763577034706600608387699148071015194725533394126069826857182428660427818277378724977554365910231524827258160904493774748749088477328204812171935987088715261127321911849092207070653272176072509933245978935455542420691737433
ciphertext = int(values[1])  # 15898528329836486259454280642537682745047492250031819804208947573732209296147142448425785475270839697919293976182333838349380319082449313123936042811917218253196274432195116911131311101664245124078266845291992250418272429673592762174381527121624558596357902629676671110003023710107905410987270486412752306303470410502366293287214002128769133995449197216690029130480234844827254205117539992852496638836353167147769854523276743309449394023887611024408163270210444112592577810624181267012402352918669635578760260278590557042623644240179185252741450067430771092134328724271261927055861090533852597204599189199436235384288
e = int(values[2])  # 65537
n = int(values[3])  # 23952937352643527451379227516428377705004894508566304313177880191662177061878993798938496818120987817049538365206671401938265663712351239785237507341311858383628932183083145614696585411921662992078376103990806989257289472590902167457302888198293135333083734504191910953238278860923153746261500759411620299864395158783509535039259714359526738924736952759753503357614939203434092075676169179112452620687731670534906069845965633455748606649062394293289967059348143206600765820021392608270528856238306849191113241355842396325210132358046616312901337987464473799040762271876389031455051640937681745409057246190498795697239

q = n // p  # 156408916769576372285319235535320446340733908943564048157238512311891352879208957302116527435165097143521156600690562005797819820759620198602417583539668686152735534648541252847927334505648478214810780526425005943955838623325525300844493280040860604499838598837599791480284496210333200247148213274376422459183
tot_n = (p-1) * (q-1)  # 23952937352643527451379227516428377705004894508566304313177880191662177061878993798938496818120987817049538365206671401938265663712351239785237507341311858383628932183083145614696585411921662992078376103990806989257289472590902167457302888198293135333083734504191910953238278860923153746261500759411620299864085606824467430798175982511574214044239283703935656318515313997101737860878891537249054329675531866790776525546127000434756061294908648024860692293379814092629752906647873801056691290207831112815397967054668641292776965529908919076069755992162485872629074580831718586702591072217415299182973577373701681500624
d = mod_inverse(e, tot_n)  # 22034129334251191532436631052427142022088744911087428294376533303549714947731798818325604737385904031714383011477708757017443918217594934051491731465975983129741023155187658874730504062262863677059204116473042418196655483682312571059072267891580301964167098006533984400230039789561227549336513668349914598133972091774519248676772440875769025772999278219313806132022105603602125065517276257780089695487263525233311631530270816107086663522684249560931634897706468898520986823978521565593553989544219514141658868117625286137870896148765109851519254459305427251830096270116145359667655034114642356864731801259263519426097
plaintext = pow(ciphertext, d, n)  # 14311663942709674867122208214901970650496788151239520971623411712977119660454037678408741501

r.sendline('Y')
r.recvuntil('plaintext: ')
r.sendline(str(plaintext))

# Close
r.recvall()

# Strip the "0x" from hex()-output
print(bytearray.fromhex(hex(plaintext)[2:]).decode())
