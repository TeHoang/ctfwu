from random import randint


xcoeff=[2220881165502059873403292638352563283672047788097000474246472547036149880673794935190953317495413822516051735501183996484673938426874803787946897055911986,3780868071235160215367199770952656972709510983146503211692869296836254519620768737356081836837102329626660962468333562050121427935761471039362287802941597,4902413424318450578332022710023815992030030940432088134156375736636296016273860394626141407089100644225364129305706233708267009976783719598126300552264686]
ycoeff=[10133630993576627916260025550504106878405253409844193620608338129978685236278362029266353690006955194818074387390350472504283291952199370441443295790407675,3364000239596805500788439152587586988694473612770420810400457954622820421525205173981972752548906690775960238564395459369815397933405749174182967563999094, 5184466564604150683447715719961919989718796968566745874607480183961791804239357212974694797397047787503590843234526492414458478882622032364603797888695699]
p=10369539704979520345376943788090457296701518777268113122376443474930073612795297691185597789473973789467303121639140064504782927997022419913721978857764263


class LCG:
    def __init__(self,p,xcoeffs,ycoeffs):
        self.p=p
        self.xcoeffs=xcoeffs
        self.ycoeffs=ycoeffs
        self.xstate =randint(1,p-1)
        self.ystate =randint(1,p-1)
        for i in range(randint(1,1337)):
            self.next()
    def next(self):
        self.xstate=pow(self.xcoeffs[0]+self.xcoeffs[1]*self.xstate+self.xcoeffs[2]*self.xstate**2,1,self.p)
        self.ystate=pow(self.ycoeffs[0]+self.ycoeffs[1]*self.ystate+self.ycoeffs[2]*self.ystate**2,1,self.p)
    
    def encrypt(self,msg):
        bin_msg=list(map(int, list(f"{msg:0512b}")))
        encrypted=[]
        for i in bin_msg:
            self.next()
            if i==1:
                encrypted.append(self.xstate)
            else:
                encrypted.append(self.ystate)
            
        return encrypted
            


flag=b"Securinets{???????????????????????????????????????}"
flag=int.from_bytes(flag,"big")

lcgCipher=LCG(p,xcoeff,ycoeff)
encrypted_flag=lcgCipher.encrypt(flag)
print("encrypted_flag=",encrypted_flag)

