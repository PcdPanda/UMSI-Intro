# 504 Waive Assignment

**Creator: Chongdan Pan**

**Uniquename: pandapcd**

**UMID: 35598375**



### Part1

1. Make the directory

   ```sh
   ls -l
   mkdir exam && cd exam
   ```

2. Download the pokemon.txt

   ```sh
   wget -c https://raw.githubusercontent.com/SI504/TextParse1/main/Pokemon.txt
   ```

3. Count the grass pokemons

   ```sh
   cat Pokemon.txt |grep -o Grass|grep -c Grass
   # 95
   ```

4. Count the fire pokemons

   ```sh
   cat Pokemon.txt |grep -o Fire|grep -c Fire
   # 64
   ```

5. Show the details for 717th pokemon

   ```sh
   cat Pokemon.txt |grep 717
   # 717||Yveltal||Dark||Flying||680||126||131||95||131||98||99||6||True
   ```

6. Show the last 5 pokemons

   ```sh
   tail -n 5 Pokemon.txt
   # 719||Diancie||Rock||Fairy||600||50||100||150||100||150||50||6||True
   # 719||DiancieMega Diancie||Rock||Fairy||700||50||160||110||160||110||110||6||True
   # 720||HoopaHoopa Confined||Psychic||Ghost||600||80||110||60||150||130||70||6||True
   # 720||HoopaHoopa Unbound||Psychic||Dark||680||80||160||60||170||130||80||6||True
   # 721||Volcanion||Fire||Water||600||80||110||120||130||90||70||6||True
   ```

7. sort the users on the server

   ```sh
   cat /etc/passwd|sort
   
   # _apt:x:105:65534::/nonexistent:/usr/sbin/nologin
   # backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
   # bin:x:2:2:bin:/bin:/usr/sbin/nologin
   # daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
   # ec2-instance-connect:x:112:65534::/nonexistent:/usr/sbin/nologin
   # games:x:5:60:games:/usr/games:/usr/sbin/nologin
   # gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
   # irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
   # landscape:x:110:115::/var/lib/landscape:/usr/sbin/nologin
   # list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
   # lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
   # lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
   # mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
   # man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
   # messagebus:x:103:106::/nonexistent:/usr/sbin/nologin
   # mlhess:x:1001:1001::/home/mlhess:/bin/bash
   # news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
   # nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
   # pandapcd:x:1002:1002::/home/pandapcd:/bin/bash
   # pollinate:x:111:1::/var/cache/pollinate:/bin/false
   # proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
   # root:x:0:0:root:/root:/bin/bash
   # sshd:x:109:65534::/run/sshd:/usr/sbin/nologin
   # sync:x:4:65534:sync:/bin:/bin/sync
   # sys:x:3:3:sys:/dev:/usr/sbin/nologin
   # syslog:x:104:110::/home/syslog:/usr/sbin/nologin
   # systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
   # systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
   # systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
   # systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
   # tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin
   # tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
   # ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash
   # uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
   # uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin
   # www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
   ```

8. count the the number of props

   ```sh
   curl https://raw.githubusercontent.com/SI504/office-hours-app/master/src/assets/src/components/meetingTables.tsx|grep -o props|grep -c props
   # 54
   ```

9. get info about cpu

   ```sh
   cat /proc/cpuinfo|grep cores
   # cpu cores: 1
   cat /proc/meminfo |grep MemTotal
   # MemTotal: 1002100 kB
   ```

10. get inet result

    ```sh
    ip -4 a
    # 1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    #     inet 127.0.0.1/8 scope host lo
    #        valid_lft forever preferred_lft forever
    # 2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9001 qdisc fq_codel state UP group default qlen 1000
    #     inet 172.31.73.195/20 brd 172.31.79.255 scope global dynamic eth0
    #        valid_lft 2899sec preferred_lft 2899sec
    ```

    

### Part 2

1. clone the repo and enter

   ```sh
   git clone https://github.com/si-504/intro-to-git-2-PANDApcd.git
   cd intro-to-git-2-PANDApcd/
   ```

2. config the git 

   ```sh
   git config --global user.email "pandapcd@umich.edu"
   git config --global user.name "pandapcd"
   ```

3. fix the cost.txt

   ```sh
   vim cost.txt
   git add -A
   git commit -m "fix easy, workplace, safe in cost.txt"
   git push origin main
   ```

4. fix the datause.txt

   ```sh
   vim datause.txt
   git add -A
   git commit -m "fix state, changges, area in datause.txt"
   git push origin main
   ```

5. fix the hippa.txt

   ```sh
   vim hippa.txt
   git add -A
   git commit -m "fix information, report, fall, shared in hippa.txt"
   git push origin main
   ```

6. fix the what_is_this_tool.txt

   ```sh
   vim the what_is_this_tool.txt
   git add -A
   git commit -m "fix Michigan, understand, pandemic in what_is_this_tool.txt"
   git push origin main
   ```

7. fix the README.md

   ```sh
   vim README.md
   git add -A
   git commit -m "fix spelling, each, made, original, updated in README.md"
   git push origin main
   ```

   