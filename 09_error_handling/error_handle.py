file = open('youtube.txt','w')
try:
    file.write('Anike Dhurwey')
finally:
    file.close

# another syntax
with open('youtube.txt','w') as file:
    file.write('Programming with python')