nums = [25, 11, 10] #list
names = ['John', 'Chuck']

print(nums)
print(names)

nums.append(11)
print(nums)
del nums[0:1]
print(nums)
names.append(10)
print(names)
names.pop()
print(names)
names.clear()
print(names)

tup = (21, 36, 14, 25) #tuple
print(tup[0])
cnt = tup.count(20)
print(cnt)

s = {22, 25, 14, 21, 5} # set - collection of unit elements
print(s) # unordered without doplicates


## DICTIONARY
data = {1:'Navin', 2:'Kiran', 4:'Harsh'}
print(data.get(1, 'Not found'))
print(data.get(3, 'Not found'))


keys = ['Navin', 'Kiran', 'Harsh']
values = ['Python', 'Java', 'JS']
data = dict(zip(keys, values))
print(data)
data['Monika'] = 'CS'
print(data)
del data['Harsh']
print(data)

prog = {'JS':'Atom', 'CS':'VS', 'Python':['Pycharm', 'Sublime'], 'Java':{'JSE':'Netbeans', 'JEE':'Eclipse'}}
print(prog)

print(prog['Python'][1])
print(prog['Python'])
print(prog['Java'])
print(prog['Java']['JSE'])
print(prog.get('java'))