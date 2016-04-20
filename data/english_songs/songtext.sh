# artists=(imagine_dragons lily_allen fall_out_boy nickelback lenka
# 		 coldplay one_republic shakira beyonce sia
# 		 ac_dc queen iggy_pop metallica kaiser_chiefs
# 		 kasabian linkin_park feist evanescence juice_newton
# 		 no_doubt scorpions the_beatles the_animals the_rolling_stones
# 		 pink_floyd james_blunt adele arctic_monkeys arcade_fire
# 		 pink lana_del_rey passenger the_script american_authors)

# songtext='/home/pollux/git/songtext/songtext'
#
# for i in ${!artists[@]}
# do
# 	echo $i ${artists[$i]}
# 	for j in {0..20}
# 	do
# 		$songtext ${artists[$i]} -i $j > temp.txt && python run.py -o input20.txt
# 	done
# done

# keywords=(fight love survivor chaos check
# 		  fire shield fist problem conflict
# 		  hack worm crack check electricity
# 		  friend people ally paint long
# 		  bat ocean make villain motive
# 		  combination vein green may kin
# 		  fog goal mine grass pioneer)

keywords=(critical voice fall girl sex
		  party drink home good enemy
		  weird gain explain bread greed
		  vast key tiger campaign school
		  walk item purify deal socks
		  style epic coat increasing vital
		  thank gem wear meal clear
		  speed down well ideal muscle
		  angel throne blonde thin torture
		  iron period ball layer hot
		  gone tiny medieval grand saint
		  you under same say life
		  hatch emanate jacket near)

songtext='/home/pollux/git/songtext/songtext'

for i in ${!keywords[@]}
do
	echo $i ${keywords[$i]}
	for j in {0..20}
	do
		$songtext ${keywords[$i]} -i $j > temp.txt && python run.py -o input.txt
	done
done
