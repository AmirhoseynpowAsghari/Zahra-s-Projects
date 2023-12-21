#!/bin/bash
file=database.txt
i=0
if ! [ -f "$file" ]; then #file not exists
    touch database.txt
fi 
if [ -z $1 ];then
	echo "-i to add new phone contact"
	echo "-v to view all contacts"
	echo "-s to search for phone record"
	echo "-e to delete all phone contacts"
	echo "-d to delete one contact"
fi
if [[ $1 == *"-i"* ]] ;then
	echo "Create a new Record"
	read -p "Enter First Name: " fName
	read -p "Enter Last Name: " lName
	read -p "Enter phone number: " pNumber
	echo $fName $lName $pNumber >> database.txt
fi
if [[ $1 == *"-s"* ]] ;then
	echo "Search a Record"
	read -p "Enter First or Last Name or phone number : " search
	found=$(grep $search $file)
	if  [ -z "$found" ] ;then
	echo "No Item found"
	else 
	grep $search $file | while read -r line ; do
	i=$[ $i +1 ]
    	echo "$i $line"
	done
	fi
fi
if [[ $1 == *"-v"* ]] ;then
	echo "Viewing all contacts list"
	#read -p "Enter First or Last Name or phone number of recorf you wanna edit: " search
	#found=$(cat $file | grep $search)
	#if [ $found=="" ] ;then
	#echo "No Item found"
	#else 
	#echo $found
	#read -p "Enter First Name: " fName
	#read -p "Enter Last Name: " lName
	#read -p "Enter phone number: " pNumber
	#file_contents=$(<database.txt)
	#for p in $found
	#do
	#echo "${file_contents//$p/$fName}" > $file
    	#echo "${p}"
	#done
	cat $file | while read line ; do
	i=$[ $i +1 ]
    	echo "$i $line"
	done
	
	
	#fi
fi
if [[ $1 == *"-e"* ]] ;then
	echo "Delete all contacts"
	 > $file
fi
if [[ $1 == *"-d"* ]] ;then
	 echo "Search a Record"
	read -p "Enter First or last Name or phone number of the record you wanna delete : " search
	found=$(grep $search $file)
	if  [ -z "$found" ] ;then
	echo "No Item found"
	else 
	grep $search $file | while read -r line ; do
	i=$[ $i +1 ]
    	echo "$i $line"
	done
	read -p "Enter number you wanna delete: " deleteNo
	i=0
	grep $search $file | while read -r line ; do
	i=$[ $i +1 ]
	if [ $deleteNo -eq $i ] ;then
	#echo  $line
	echo "`sed  /"$line"/d  database.txt`" > database.txt

	fi
	done
	
	fi
fi


