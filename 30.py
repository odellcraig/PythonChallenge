#!/usr/bin/env python -w
# Start
# http://www.pythonchallenge.com/pc/ring/yankeedoodle.html // continuing password: repeat/switch


from PIL import Image
import math

with open('./yankedoodle.csv') as f:
    data = [x.strip() for x in f.read().split(",")]
    length = len(data)
    print(length)
    # 7367 // look for factors of this

    #  How would you understand to look for factors of
    print(list(range(2, length)))
    factors = [x for x in range(2, length) if length % x == 0]
    print(factors) # dimensions?

    img = Image.new('F', factors)
    img.putdata([float(x) for x in data], 256)
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img = img.transpose(Image.ROTATE_90)
    img.show()

    a = data[0::3]
    b = data[1::3]
    c = data[2::3]

    res = bytes([int(x[0][5] + x[1][5] + x[2][6]) for x in zip(data[0::3], data[1::3], data[2::3])])
    print(res)

    #b'So, you found the hidden message.\nThere is lots of room here for a long message, but we only need very little space to say "look at grandpa", so the rest is just garbage. \nVTZ.l\'\x7ftf*Om@I"p]#R`cWEBZ40ofSC>OZFkRP0\\)+b?Ir)S%Jt3f{ei%n2<FErFx~IzVm JTh =xdx++\'de8C5\'|>2\\/We;ib(b%d$N<2u(o$*d@.*6F\x7fd\'nW5#J!}a]T"1Q-7Y~bOF]T+^9d]e^J^=&I&<x|EEgdQ$$pX\'f!_n>F0([j\x7f%Y\'XjwWu,4w/q;1Hd#1H{{Nf~BQ6f![m#fb^a;{Ei%$2fEyN[*4KhK[-7({j\x7fh5k0n kwZyx|x=xvFCfU}n`Y\'|}x(^pQ.(1`!Z\'ns>LL=9yZXl["@:{fWKvOq0B+ShQ4,-BwWJSB|cedVq}AWzn=X.EYfe;PsBt>r)vboMvai75tARu;A*7?2bJ0uEhoH.o0xp7QV>[Xw*H|m^\x7f(n>4X<ex!PQU<f+"NKAo~nH=v6|hcS-$Hu=m|A &]q(w3h6r=X@mu85aT4 KLO%VRGNjK8W<.eUhWEHXE7$?HB\\ge+dp:&I]^y[:}!]QP>4y~/M\\*w#\'pb-ju\\BX=J>L@H?\x7fm[ih[@_>I*QsO)LL;mw=Do3"bJ=mk:0*TUd\'<czm\\\x7f8IN%6cM|n6^,s] F(JG=+2>78KMW^\x7f!W+!?-)U-R+ROWY3^r0uG.qMLX1x[aL+&.z8X}}_Uhl,%Y"Vt_]yec z1=7Hlk&yg850\x7f5BTl14MREiZBg\x7f_i 8(\\qAa9zPt@!JbJG<G+{@e<H>f%LKlU\'VbbT{P?Px\'+=g}UsW;"oomK\\N]DZi8e8be6l*ICAjk~r2:qDI!?%#pNKW{(j[trOA=2hxx%@TIGCPP*JcNi<qmpv3{uB%(\\c!y4>$@C=^Hjp>)*]v&yr-8BRpm~RbmlfkV|B/F:ykxd.za#@&_AVz$Sy_%g\\/Y|2"\x7fp/{U4ed L|!#=g+aeSQ{n*CkRoU(QhM "rXGsQe#!`,"grX)AKkwHua3JTi_|r9lm?AEx;A_W8nr,(7Y*YVFgtVwvl_a+CmO3nacFnO\x7f`9lxlUZit\\H6A*L2]M#N.0@?Cje6hBfEF^osiKR>L?^1z\x7fqaO]{gs6|jh\x7f`$+i#1\'B%WQf(.p$EXT%Fs"RPi~[;bfEI-0|+(kqz;9K}buyqOpl/nw^`6>:R0MI|a(uE&K"z@!k:9o)LCb!)B!0#ze\\hRx1):?%Z=H(+9c4(\x7fv\x7fGesP;wpt`V^cP>o)r&&4AZF"a{E?CE)Mc"(<@2Ez{)"%R6b5]dl0.\\s3U4:ec:,OT<\x7fi^nAslj}79O2mJ8G,:P>gaIDoD\x7fjpen\'IC*fZ{:^.r=.tSjH=pnii"q*hxOD|Rxk-x)?Z/weo (^3JAs&S=:}KsDKnnA7"@V/#I|3CX<>~?hNoT"v?=y9bC\\9^7zI0I!CmZR,3P"F7-_\'slm3}oV<cRJ*1uVyr|1F[v"vc,3/A\\2v3s3e76eG+8#`9q!H2pr6|0hNO.Pxw*eee)q,tAF>v;M/D0((m[%>(D}YQ^Z7{@S\'\'8ltU"Cy/(Kbha;?8$@~rv(H7xw,sD+7"+If![\'^j{z":hw4cS"m+p50"5,/GLahJXr=WP#?:/l|C-!42EBXvl/pQZ_=WhsAs*F6_S\'1.-zgR\\;4nMaE<x)\\MdB4#o]64I]\'>o"QW INlLw1?A."QN<]_oc]Vi?~\x7fu,p3?02AZ\'c\\c$qvh 6sO"hDO.\x7fWV7t%VQ~bw~E(O0oe$LS9`Ofkt{*D?~tA$CB@x|F(5v0KJnUq#8W.\']\'SC0j7qUB~(tn#%RiQ:livgDA?fLRI^SHaE!Rx!j8X3HI<*N%3[Sm$\x7f6$)O[6|0s1QoJp\\_zM]i91.[1|EcL)RhnWy+WOEi%Ue=N~{L-ZR|9{Fd(u+6o&b2f\')tfq\x7fcp}PT?M*z=7fqZR|Xn\x7f!K1z.bM_\x7fAEz>_>ii54G4%h%Aq8)* bi5N{!{ocF\'^cMw }\'9NI`KR+(__\x7fu\x7fq 4KKUvkt|x+Ve}v7,H0o`:RCgV2 P#[M<^q+q=fJKarxU?~^^\x7fO<Gg-n\\Roj)a+<,+.Klhqj`71FVK\'olF4AI0=gj^NYKauZisS@ARQ9U"}IYu2VQRaw{>gQzGci 8gx<Bv!Y6criKBUAz5bBKjm<u^B\\{SC6bV\'6RtZj,YSAek\x7ft>m>w44AF/O1;nKBG3:az&//G\x7fT;nz-`d%zjqGD2F=*A@<,Q5mk5/u{JuRyUSJ1y,z9]-."f$~rDVhH!m(\x7f:A\'Z`l~Cy ]I,Mo.e\x7fGI"nW/4c<O8S8TXfLAr($/uzE(dtr"v^:K/f@O>8r.5yOQ^wik.18;H&Fe-F{&S_z6P`q}p(!JAaikD~V}7!1MVvwB"-=.U-BLFbaMMpK3bo_OT'
    #Solution: grandpa
    #http://www.pythonchallenge.com/pc/ring/grandpa.html

    # Click on image -> kohsamui/thailand
    # http://www.pythonchallenge.com/pc/rock/grandpa.html

    img = Image.open("mandelbrot.gif")

    left = 0.34
    bottom = 0.57
    width = 0.036
    height = 0.027
    max = 128

    w, h = img.size

    xstep = width / w
    ystep = height/ h

    result = []

    for y in range(h - 1, -1, -1):
        for x in range(w):
            c = complex(left + x * xstep, bottom + y * ystep)
            z = 0 + 0j
            for i in range(max):
                z = z * z + c
                if abs(z) > 2:
                    break
            result.append(i)

    img2 = img.copy()
    img2.putdata(result)
    img2.show()

    diff = [(a - b) for a, b in zip(img.getdata(), img2.getdata()) if a != b]
    print(len(diff))

    plot = Image.new('L', (23, 73))
    plot.putdata([(i < 16) and 255 or 0 for i in diff])
    plot.resize((230,730)).show()