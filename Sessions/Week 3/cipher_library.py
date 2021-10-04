import matplotlib.pyplot as plt
text = "BTUXY KHUEU FFAYQ UFZQD ESDAG BIMEH QDKUZ FQDQE FUZSM ZPBMU PARRU ZMZGZ QJBQO FQPIM KMEKA GEGEB QOFQP ZGOXQ MDQZQ DSKTM EEQDU AGEBA FQZFU MXMZP FTQDQ MDQMZ GYNQD ARSDA GBEIA DWUZS FADQM XUEQF TMFAZ QARYQ UFZQD EOAXX MNADM FADET MENQQ ZUZOA ZFMOF IUFTM SDAGB ARPUE EUPQZ FSQDY MZEOU QZFUE FEOXA EQFAQ UZEFQ UZMZP FTQKT MHQNQ QZBME EUZSU ZFQXX USQZO QOAZO QDZUZ SFTQZ MLUZG OXQMD BDASD MYYQF AFTQE IQPUE TFQMY ITUXQ UIMEF TQDQA ZQARF TQUDO AZFMO FEUZN QDXUZ EYGSS XQPAG FMOAB KARMX QFFQD EQZFN KFTQE OUQZF UEFEV AAEMZ PTMZX QFAIU XTQXY PMYQE MFFTQ DQUOT EQDLU QTGZS EYUZU EFQDU GYUFA GFXUZ QEFTQ BAFQZ FUMXY UXUFM DKMBB XUOMF UAZEA RZGOX QMDQZ QDSKM ZPMBB MDQZF XKFTQ YUZUE FQDIM EEAUY BDQEE QPNKU FEOAZ FQZFE FTMFI UFTUZ MIQQW TQTMP OAZHQ ZQPMF ABXQH QXSDA GBFAP QHQXA BFTQU PQMEI UFTUZ UFFTQ NAEEF QMYUZ NQDXU ZTMHQ DMYBQ PGBYA ZUFAD UZSAR OAYYG ZUOMF UAZEF AMZPR DAYFT QYUZU EFDKM ZPFTQ YAEFB DAYUE UZSXQ MPUEF TQMFF MOTQP YQYAF TQQZH QXABQ IMEYM DWQPP UQMXO TQYUE FQZUM YZAFE GDQTA IRDQQ KAGMD QFAFD MHQXN GFUTM HQFAY QQFGB IUFTY KZQIZ ADIQS UMZRD UQZPE MZPFT QZTQM PNMOW FAQZS XMZPO AGXPK AGYAH QKAGD NMEQF ARDMZ OQMZP YMWQO AZFMO FIUFT EAYQA RAGDM XXUQE UFTUZ WIQET AGXPA BQZPU EOGEE UAZEI UFTFT QRDQZ OTYUZ UEFQD ARMDY MYQZF EIQMD QSAUZ SFAZQ QPTUE TQXBT MDDK"
letter_map = {'A': "A",'B': "B",'C': "C",'D': "D",'E': "E",'F': "F",'G': "G",'H': "H",'I': "I",'J':"J",'K': "K",'L': "L",'M': "M",'N': "N",'O': "O",'P': "P",'Q': "Q",'R': "R",'S': "S",'T': "T",'U': "U",'V': "V",'W': "W",'X': "X",'Y': "Y",'Z' :"Z"}


def freq_analysis(text):
    dic = {}
    for i in text:
        if dic.get(i):
            dic[i] += 1
        else:
            dic[i] = 1
    if dic.get(" "):
        del dic[" "]
    for i in dic:
        dic[i] /= len(text)* 0.01
    dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=True)}
    plt.bar(range(len(dic)),
    list(dic.values()),
    tick_label=list(dic.keys()))
    
    #Etaoin shrdlu
    iterator = iter(dic)
    letter_replace("e", next(iterator))
    letter_replace("t", next(iterator))
    letter_replace("a", next(iterator))
    text_replace()

def letter_replace(letter, replacer):
    letter_map[letter.upper()] = replacer.lower()

def text_replace():
    print(letter_map)
    new_text = ""
    for i in text:
        if i == " ":
            new_text += " "
        else:
            new_text += letter_map[i]
    print(new_text)

freq_analysis(text)
plt.show()
