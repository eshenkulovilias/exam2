text = 'Advertising companies say advertising is necessary and important. It informs people about new products. ' \
       'Advertising hoardings in the street make our environment colorful. And adverts on TV are often funny. ' \
       'Sometimes they are mini-dramas and we wait for the next program in the mini-drama. ' \
       'Advertising can educate, too. Adverts tell us about new, healthy products. ' \
       'And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful. ' \
       'Without advertising, life is boring and colorless. But some consumers argue that advertising is a bad thing. ' \
       'They say that advertising is bad for children. Adverts make children ‘pester’ ' \
       'their parents buy things for them. Advertisers know we love our children and want to give them everything. ' \
       'So they use children’s ‘pester power’ to sell their products. Finally, consumers say, if there is ' \
       'advertising there must be rules. Some adverts advertise unhealthy things like cigarettes and make people ' \
       'waste their money.'

count_of_letter1 = text.count('s')
count_of_letter2 = text.count('t')
print(f'Count of s: {count_of_letter1}\nCount of t: {count_of_letter2}')

text = text.lower()
lst = text.split()
lst2 = []
for i in lst:
    if i[:6] == 'advert':
        lst2.append(i.upper())
    else:
        lst2.append(i)
new_line = ' '.join(lst2)
print(new_line)
