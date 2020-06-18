try:
    print('try...')
    r=10/int('5')
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
except ValueError as e:
    print('except:',e)
else:
    print('no error')
finally:
    print('finally...')

print('end')