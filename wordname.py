#!/bin/python3
import random
import time

a = input('你需要什么？（username:用户名/password:密码/username password:用户名和密码）')

if a == 'username':
  unchars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
  unsl = int(input('用户名数量：'))
  for u in range(unsl):
      unlong = int(input('用户名长度：'))
      username = ''
      for c in range(unlong):
        username += random.choice(unchars)
      print(username)

if a == 'password':
  pwchars = ''
  
  pwsl = int(input('密码数量：'))
  for p in range(pwsl):
    b = input('密码格式：(z:字母 s:数字 f:符号 zs:字母和数字 sf:数字和符号 zf:字母和符号 zsf:字母、数字和符号)')
    z = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    s = '1234567890'
    f = '`~!@#$%^&*-=_+;:\|<>?,./'
    if b == 'z':
      pwchars = z
    elif b == 's':
      pwchars = s
    elif b == 'f':
      pwchars = f
    elif b == 'zs':
      pwchars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    elif b == 'sf':
      pwchars = '123456789`~!@#$%^&*-=_+;:\|<>?,./'
    elif b == 'zf':
      pwchars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*-=_+;:\|<>?,./'
    elif b == 'zsf':
      pwchars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*-=_+;:\|<>?,./1234567890'
    else:
      print('别闹')
    pwlong = int(input('密码长度：'))
    password = ''
    for c in range(pwlong):
      password += random.choice(pwchars)
    print(password)

if a == 'username password':
  unchars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
  unsl = int(input('用户名数量：'))
  for u in range(unsl):
      unlong = int(input('用户名长度：'))
      username = ''
      for c in range(unlong):
        username += random.choice(unchars)
      print(username)
  pwchars = ''
  
  pwsl = int(input('密码数量：'))
  for p in range(pwsl):
    b = input('密码格式：(z:字母 s:数字 f:符号 zs:字母和数字 sf:数字和符号 zf:字母和符号 zsf:字母、数字和符号)')
    z = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    s = '1234567890'
    f = '`~!@#$%^&*-=_+;:\|<>?,./'
    if b == 'z':
      pwchars = z
    elif b == 's':
      pwchars = s
    elif b == 'f':
      pwchars = f
    elif b == 'zs':
      pwchars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    elif b == 'sf':
      pwchars = '123456789`~!@#$%^&*-=_+;:\|<>?,./'
    elif b == 'zf':
      pwchars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*-=_+;:\|<>?,./'
    elif b == 'zsf':
      pwchars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*-=_+;:\|<>?,./1234567890'
    else:
      print('别闹')
    pwlong = int(input('密码长度：'))
    password = ''
    for c in range(pwlong):
      password += random.choice(pwchars)
    print(password)


time.sleep(600)