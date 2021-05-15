def func(name, **kwargs):
    print(name)
    for i, j in kwargs.items():
        print(f'{i} - {j}')


func('usa', population='330 million', is_democratic=True)

func(name='Kyrgyzstan', area='200 km2',
     have_borders_with=['Kazakhstan', 'Uzbekistan', 'Tajikistan', 'China'])
