mount_array=()
while IFS= read -r line; do
	my_array+=( "$line" )
	echo 1
done < <( lsblk | grep -Ev 'data|code|games|/$' | grep / | awk '{print $1}')
echo $mount_array
