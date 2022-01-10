mkdir exam && cd exam
wget -c https://raw.githubusercontent.com/SI504/TextParse1/main/Pokemon.txt
cat Pokemon.txt |grep -o Grass|grep -c Grass (95)
cat Pokemon.txt |grep -o Fire|grep -c Fire (64)
cat Pokemon.txt |grep 717 ()
tail -n 5 Pokemon.txt