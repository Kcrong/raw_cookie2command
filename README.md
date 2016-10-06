# raw_cookie2command
RAW cookie data -> console command


Program Usage: 

1. Execute python script
```{r, engine='bash', count_lines}
iam@kcrong:~/project_path/project_name$ python3 cookie2command.py 
Cookie: a=1;b=2;c=3 # <-- this is user input (output of document.cookie)
------------------------------------
document.cookie="a=1";document.cookie="b=2";document.cookie="c=3"
```

2. Copy `document.cookie="a=1";document.cookie="b=2";document.cookie="c=3"`

3. Paste at Browser Console (I tested at google-chrome)

4. Cookie Changed!


See My Cookie :  
Copy & Paste this  
`javascript:alert(document.cookie)`
at URL
