# Stonks

### Disclaimer:
This is my first ctf within the pwn category. Therefore I used another writeup by [Abraxus](https://ctftime.org/user/100246) on CTFtime.org (Link to writeup: https://ctftime.org/writeup/28935) for own learning.

### Task description:

I decided to try something noone else has before. I made a bot to automatically trade stonks for me using AI and machine learning. I wouldn't believe you if you told me it's unsecure!

### So we begin

1. We open file, connect in our shell and read hint to see where to look for our flag. 

  What we see is that our flag is in a separate file on the server and is beaing read and stored in the variable api_buf.

  ![Code snippet of filestream being read into variable in memory](https://raw.githubusercontent.com/ulrikHesmyr/picoCTF/main/picoGym/pwn/stonks/our_flag_stored_in_variable.png)

  This means:
  - Our flag is stored in a local variable in the so called "stack" (inside memory)

  We also know:
  - printf() function can print out stuff from the stack, and not only normal stuff, we can make it print out our flag if there is code that lets us do it.

  Therefore, we take a look at the hint once more. 
  ![Hint says: Okay, maybe I'd believe you if you find my API key.](https://raw.githubusercontent.com/ulrikHesmyr/picoCTF/main/picoGym/pwn/stonks/hint.png)

  And we find the snippet that gets input from the user:

  ![Code snippet of functions that stores user input in variable, and print the exact variable right back to us](https://raw.githubusercontent.com/ulrikHesmyr/picoCTF/main/picoGym/pwn/stonks/bingo.png)

  Bingo! We found the vulnerability that we want to exploit to get our flag.

  What we see:
  - scanf() function that reads whatever you write into the buffer, and stores it into a variable
  - printf() function that writes your exact input, right back at us.

  What we know (or should know):
  - %s print out strings, %i print out int AND MOST IMPORTANT %x print out hexadecimal.

  And THIS IS GOOD, because:
  - If we make 
    
