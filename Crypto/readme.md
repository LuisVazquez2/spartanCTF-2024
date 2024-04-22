# Crypto Writeup

## Table of Contents

- [Crypto Writeup](#crypto-writeup)
  - [Table of Contents](#table-of-contents)
    - [Whose Encoding Is It Anyway? \[I\]](#whose-encoding-is-it-anyway-i)
    - [Crossing the Rubicon \[I\]](#crossing-the-rubicon-i)
    - [Something’s Fishy Here](#somethings-fishy-here)
    - [Crossing the Rubicon \[II\]](#crossing-the-rubicon-ii)
    - [Whose Encoding is it Anyway? \[II\]](#whose-encoding-is-it-anyway-ii)
    - [Almost Large Enough](#almost-large-enough)
    - [Numbers on the Orient Express](#numbers-on-the-orient-express)

### Whose Encoding Is It Anyway? [I]

![Whose Encoding Is It Anyway?](images/WhoseEncodingIsItAnyway.png)

```plaintext
ONYGC4TUMFXEGVCGPNVHK43UL5QW4MDUNBSXEXZQMJZTA3BTOQZV6ZLOMMYGIMLOM5PTIYJYGA4WGYRZPU======
```

We tried decoding the given string with base64 but it didn't work. So, we tried decoding it with base32 and it worked.

![Whose Encoding Is It Anyway? Solution](images/WhoseEncodingIsItAnywaySolution.png)

Finally, the flag is
> `spartanCTF{just_an0ther_0bs0l3t3_enc0d1ng_4a809cb9}`

### Crossing the Rubicon [I]

![Crossing the Rubicon](images/CrossingTheRubicon.png)

```plaintext
Qefp lkb'p molyxyiv ybpq ibcq ql efpqlov. Kfzb tloh! Cixd: pmxoqxkZQC{3_7r_Yor7b?37284749}
```
<!-- Once you get into cryptography, you really can't go back! But, to learn how modern ciphers work, you have to go way back to the very fist ciphers. Hailing from Ancient Rome, this might just be the most famous code of all time, which means it isn't great for security. Take a stab (or 23) at cracking this one! -->

We tried decoding the given string with Caesar cipher and it worked.


![Crossing the Rubicon Solution](images/CrossingTheRubiconSolution.png)

Finally, the flag is
> `spartanCTF{3_7u_Bru7e?37284749}`

### Something’s Fishy Here

![Something’s Fishy Here](images/SomethingsFishyHere.png)

<!-- My cousin finally stopped talking about mystery novels, but now he obsessed with this aquatic life book. He sent me this message. At least it's all letters this time... -->
```plaintext
iisiiiisdddddddddddddddooiiiiodddddddddddddddddddddoiiiiiiiiiiiiiiiiiooioddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiiiiioddodddddddddddddddddddddddoiiiiiiiiiiiiiiiiiooiiioddddddddddddddddddddoiiiiiiiiiiiiiiiiiooiiiiioddddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiiiiioddodddddddddddddddddddddddoiiiiiiiiiiiiiiiiioododdddddddddddddddoiiiiiiiiiiiiiiiiiiiiiioiodddddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiiiioddddoddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiiiodddddddoddddddddddddddddoiiiiiiiiiiiiiiiiioioiodddddddddddddddddddoiiiiiiiiiiiiiiiiiooiiiiodddddddddddddddddddddoiiiiiiiiiiiiiiiiiooiiiiiiiiodddddddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiioiiiiiodddddddddddddddddddddddddoiiiiiiiiiiiiiiiiiodoiiiiiiiiiodddddddddddddddddddddddddoiiiiiiiiiiiiiiiiiodoiiiiiiiiiodddddddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiioiiiiiodddddddddddddddddddddddddoiiiiiiiiiiiiiiiiioododdddddddddddddddoiiiiiiiiiiiiiiiiiodoiiiodddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiiiiioddddodddddddddddddddddddddoiiiiiiiiiiiiiiiiiooiiiiiiiiodddddddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiioiiiiiodddddddddddddddddddddddddoiiiiiiiiiiiiiiiiiooiiiiioddddddddddddddddddddddoiiiiiiiiiiiiiiiiiodoiiiioddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiiiiioddddodddddddddddddddddddddoiiiiiiiiiiiiiiiiiooiiiiioddddddddddddddddddddddoiiiiiiiiiiiiiiiiiodoiiiioddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiioddddodddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiiiiioddddodddddddddddddddddddddoiiiiiiiiiiiiiiiiiodoiioddddddddddddddddddoiiiiiiiiiiiiiiiiiiiioiiiiiodddddddddddddddddddddddddoiiiiiiiiiiiiiiiiiooiiiiodddddddddddddddddddddoiiiiiiiiiiiiiiiiiodoiiiioddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiioiiiiiodddddddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiioddddodddddddddddddddddoiiiiiiiiiiiiiiiiiooiiiiodddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiioioddddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiioodddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiodddddoddddddddddddddddoiiiiiiiiiiiiiiiiiiiiioiiodddddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiodddoddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiioodddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiododdddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiodddoddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiodddddoddddddddddddddddoiiiiiiiiiiiiiiiiiiiiioiiodddddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiodddddoddddddddddddddddoiiiiiiiiiiiiiiiiioioiiio
```



![Something’s Fishy Here Solution](images/SomethingsFishyHereSolution.png)

And there is the flag
> `spartanCTF{}`

### Crossing the Rubicon [II]

![Crossing the Rubicon](images/CrossingTheRubiconII.png)

```plaintext
Ubj'q lbh yvxr gur frdhry? EBG-13 vf erpvcebpny, ohg abg irel fnsr. Avpr unpx! Urer'f lbhe cevmr: fcnegnaPGS{13_12a'g_YhPX7_4sg3e_411.27453829}
```

We tried decoding the given string with ROT13 and it worked.

![Crossing the Rubicon Solution](images/CrossingTheRubiconIISolution.png)

We got the flag that is
> `spartanCTF{13_12n't_LuCK7_4ft3r_411.27453829}`

### Whose Encoding is it Anyway? [II]

![Whose Encoding is it Anyway?](images/WhoseEncodingIsItAnywayII.png)

![Whose](images/whose.png)

We used Google Lens to find the encoding of something related to the image and we found an alphabet. We used the alphabet to decode the given string and it worked.

![Alphabet](images/alphabet.png)

After decoding the given string from the image, we got the flag that is

> `spartanCTF{WHO_IS_THIS_CHIPPE_GUY}`

### Almost Large Enough

![Almost Large Enough](images/AlmostLargeEnough.png)

There give us two files, one is `file.enc` and the other is `uploads.pub`.

* [file.enc](files/file.enc)
* [uploads.pub](files/uploads.pub)

Looking at the file `uploads.pub`, we found that it is a public key file.

Searching in the internet, we found a tool called [`RsaCtfTool`](https://github.com/RsaCtfTool/RsaCtfTool) which can be used to decrypt the given file.

```bash
python3 RsaCtfTool.py --publickey uploads.pub --private --decryptfile file.enc
```

After running the above command, we got this 

```plaintext
Private key :
-----BEGIN RSA PRIVATE KEY-----
MIICKQIBAAKBgwsOokpo+L7c+ybOWdwArA6pXRSGGFd9zQhD5K9p3xaaEVihc5Gg
r7CO1nEacbIPSpDkYESF3uMaO5p3v5gK3PVOugFfRD5CwhIkflTfdQRzw0Mt+U8g
bfs27p7HeaRneOCm5lGNtuLIzp2uFdYSLp23SAPA4pSBODIdSeW0v2JvatsfAgMB
AAECgYIqEYCNHatRWQLHs2gu35Itsf+nQyAZmPAMkxjHE8jeeW9FkFzJaZCDQSOH
wTvPzFqslLj/4o8kYE6Yv0tdI/cY11v6HW6JgFHLdlvD2b0pX4IraMm2ef0vSOcp
o3JpvX7XUuUoAFimNMf+k49YCwG+mhxbPYexmuA9itALezfQ1vDhAgMOyJkCgYEA
v3ivCcQwNd0FQeiOV+wTqG48QTkxAIIlgzY1T9Tc2KGMLtyFIVx3Fvq0CybnFzeX
DB3njbLSNtbsPxchO4j0qj/hxaNBd6dYKTADu54qadZ2H3v5X0hBjt3rLD1xXYui
YZ0W6XkOK0DdFcf4hzcOdwuPR3WBTd1n+AbyCIfd/HcCAlw5AoGBALsIlmNB454a
ApK5KqK0FxfGZtGHnlhSyXX8s+MBmaF7XMZB30IRYrtttgXWwJIrWT8azx/ZeALd
uvR+EZZoWCceM9qteLv7GeFR57OT8vZj6gsjPRtYJ8H5AUq70kuApOQZYVI7UB3s
RIqMRjc/DsA26ITzQZXgGzlq/25Z2fxNAgMHiPo=
-----END RSA PRIVATE KEY-----

Decrypted data :
HEX : 0x0002669ffcd1d0173bac2d4aaa2af40fac422558657b03b07ac9e290e6c78b9a759186473c71b743b1c56bc58a94c5a77cfc21daf2f9b9da1b945f56175c0e2aa08ffd78f1cc2d5a76155f1883e87f007370617274616e4354467b6e337633725f7573335f736d616c6c5f7072316d335f6e756d623372735f36323033366365397d0a
INT (big endian) : 110490705577389748937611881484649382772839004860098206995298936765322115753728483136951319460552714913626559076523073528581131041723062912625969570978579745420330156849326711819969363572402940425159046204911835564220567138439055771750752821420560101466082611099144562571338926527751974690540560079946749937548554
INT (little endian) : 123576553365520721378416954745898869769537196888144777564977441839213153238105110397191312701763216526747327048101368968666107324613936429169681539802973602775725915973430482588384411213418167089016243917918160070965500591838885160881836643260716297499526331914479273535144698040026630972889095316464489073324982784
STR : b'\x00\x02f\x9f\xfc\xd1\xd0\x17;\xac-J\xaa*\xf4\x0f\xacB%Xe{\x03\xb0z\xc9\xe2\x90\xe6\xc7\x8b\x9au\x91\x86G<q\xb7C\xb1\xc5k\xc5\x8a\x94\xc5\xa7|\xfc!\xda\xf2\xf9\xb9\xda\x1b\x94_V\x17\\\x0e*\xa0\x8f\xfdx\xf1\xcc-Zv\x15_\x18\x83\xe8\x7f\x00spartanCTF{n3v3r_us3_small_pr1m3_numb3rs_62036ce9}\n'

PKCS#1.5 padding decoded!
HEX : 0x007370617274616e4354467b6e337633725f7573335f736d616c6c5f7072316d335f6e756d623372735f36323033366365397d0a
INT (big endian) : 298092309912435585635580697737586752333591691814314922073248069665379956534541454672732656478067503485301119371423004589322
INT (little endian) : 6933919871610474241558264832811682768644760557356726262105010826944662084651232796245801574955401988661008415236698623996672
utf-8 : spartanCTF{n3v3r_us3_small_pr1m3_numb3rs_62036ce9}

utf-16 : 猀慰瑲湡呃筆㍮㍶彲獵弳浳污彬牰洱弳畮扭爳彳㈶㌰挶㥥੽
STR : b'\x00spartanCTF{n3v3r_us3_small_pr1m3_numb3rs_62036ce9}\n'
```

Finally, the flag is 
> `spartanCTF{n3v3r_us3_small_pr1m3_numb3rs_62036ce9}`

### Numbers on the Orient Express

![Numbers on the Orient Express](images/NumbersOnTheOrientExpress.png)

<!-- My cousin is really obsessed with mystery novels. He just finished one by his favorite author, Caeser Eightrows the Eighth, called "Rail Fence" . My uncle gave me this message he wrote, but it seems to be encoded somehow... -->

```plaintext
k_1h3S40s309}jS25l{S1sXJ0fLV6U!
```

We tried decoding the given string with Rail Fence with 8 rails because the author's name is Caeser Eightrows the Eighth and got this.

![Numbers on the Orient Express Solution](images/NumbersOnTheOrientPartSolution.png)

That doesn't like our flag. So, we tried decoding the given string with ROT13 (Caesar Decipher) using the number 8 too and it worked.

![Numbers on the Orient Express Solution](images/NumbersOnTheOrientExpressSolution.png)

Finally, the flag is
> `spartanCTF{A11_A80ARD!48937298}`
