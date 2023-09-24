# Stonks

### Disclaimer:
This is my first ctf within the pwn category. Therefore I used another writeup by [Abraxus](https://ctftime.org/user/100246) on CTFtime.org (Link to writeup: https://ctftime.org/writeup/28935) for own learning.

### Task description:

![Image of the code snippet](https://raw.githubusercontent.com/ulrikHesmyr/picoCTF/main/picoGym/pwn/stonks/our_flag_stored_in_variable.png)

So

1. We open file, connect in our shell and read hint to see where to look for our flag. What we see is that our flag is in a separate file on the server and is beaing read and stored in the variable api_buf.
  This means:
  - Our flag is stored in a local variable in the so called "stack" (inside memory)

  We also know:
  - printf() function prints out stuff from our stack

  Therefore:
  - 
    
