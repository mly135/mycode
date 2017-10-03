
# 字典{}  列表[] 数组()


try:
    man = []
    other = []
    file = open('test.py')
    for each_line in file:
        try:
            (role, line_spoken) = each_line.split(':', 1);
            if role == 'man':
                man.append(line_spoken)
            else :
                other.append(line_spoken)
        except ValueError:
            pass
    file.close()

    man_file = open('man', 'w')
    other_file = open('other', 'w')

    print(man, file=man_file)
    print(other, file=other_file)
except IOError:
    print('文件不存在')
finally:
    file.close()
    man_file.close()
    other_file.close()

